from flask import Flask, request, send_from_directory
import subprocess
import MyChatGPT

app = Flask(__name__)
from urllib.parse import parse_qs
import user_session

ret_simulate = '\n\n#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <unistd.h>\n#include <sys/socket.h>\n#include <netinet/in.h>\n#include <arpa/inet.h>\n\n#define MAXLINE 1024\n\nint main(int argc, char *argv[])\n{\n    int sockfd, n;\n    char recvline[MAXLINE + 1];\n    struct sockaddr_in servaddr;\n\n    if (argc != 2)\n    {\n        printf("usage: a.out <IPaddress>\\n");\n        exit(1);\n    }\n\n    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)\n    {\n        printf("socket error\\n");\n        exit(1);\n    }\n\n    bzero(&servaddr, sizeof(servaddr));\n    servaddr.sin_family = AF_INET;\n    servaddr.sin_port = htons(80);\n    if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0)\n    {\n        printf("inet_pton error for %s\\n", argv[1]);\n        exit(1);\n    }\n\n    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0)\n    {\n        printf("connect error\\n");\n        exit(1);\n    }\n\n    char *request = "GET / HTTP/1.1\\r\\nHost: www.example.com\\r\\n\\r\\n";\n    write(sockfd, request, strlen(request));\n\n    while ((n = read(sockfd, recvline, MAXLINE)) > 0)\n    {\n        recvline[n] = 0;\n        if (fputs(recvline, stdout) == EOF)\n        {\n            printf("fputs error\\n");\n            exit(1);\n        }\n    }\n    if (n < 0)\n    {\n        printf("read error\\n");\n        exit(1);\n    }\n\n    exit(0);\n}'


@app.route('/')
def index():
    data = request.get_data()
    print(data)
    if "iPhone" in request.headers:
        return send_from_directory('./web', "index_mobile.html")
    return send_from_directory('./web', "index_mobile.html")


# return send_from_directory('./web', "index.html")

@app.route('/get_webid.cgi', methods=['GET'])
def cgi_get_webid():
    return user_session.create_user()


@app.route('/push_session.cgi', methods=['POST'])
def cgi_script():
    # return ret_simulate
    data = request.get_data()
    print("++++", data)
    params = parse_qs(data.decode())
    print(params)

    message = params.get('message', None)
    if message == None:
        return "网络出错"
    message = message[0]
    print("接收到的信息-->", message)

    session_id = params.get('session_id', None)
    if session_id != None:
        session_id = session_id[0]
    print("接收到的会话id-->", session_id)

    try:
        chatgpt = MyChatGPT.Gpt()
    except:
        print("创建gpt 错误")
        return "系统出错"

    all_msg = user_session.add_session(session_id, message, "you")
    try:
        output = chatgpt.get_session(all_msg)
    except:
        print("gpt 回复错误")
        return "gpt回复错误"
    user_session.add_session(session_id, output, "gpt")
    return output


@app.route('/<path:path>')
def serve_file(path):
    if path.endswith('.html'):
        return send_from_directory('./web', path)
    else:
        print("--------------", path)
        return "404 Not Found"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
