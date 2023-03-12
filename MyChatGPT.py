key = "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"
key_list = {
    "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": "free",
    "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": "free",
    "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": "free"
}
demo_ret_data = {'id': 'cmpl-6smEjmNkLnQOdEJZfRcgwCakey03M', 'object': 'text_completion', 'created': 1678513153, 'model': 'text-davinci-003', 'choices': [{'text': '\n\n#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <unistd.h>\n#include <sys/socket.h>\n#include <netinet/in.h>\n#include <arpa/inet.h>\n\n#define MAXLINE 1024\n\nint main(int argc, char *argv[])\n{\n    int sockfd, n;\n    char recvline[MAXLINE + 1];\n    struct sockaddr_in servaddr;\n\n    if (argc != 2)\n    {\n        printf("usage: a.out <IPaddress>\\n");\n        exit(1);\n    }\n\n    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)\n    {\n        printf("socket error\\n");\n        exit(1);\n    }\n\n    bzero(&servaddr, sizeof(servaddr));\n    servaddr.sin_family = AF_INET;\n    servaddr.sin_port = htons(80);\n    if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0)\n    {\n        printf("inet_pton error for %s\\n", argv[1]);\n        exit(1);\n    }\n\n    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0)\n    {\n        printf("connect error\\n");\n        exit(1);\n    }\n\n    char *request = "GET / HTTP/1.1\\r\\nHost: www.example.com\\r\\n\\r\\n";\n    write(sockfd, request, strlen(request));\n\n    while ((n = read(sockfd, recvline, MAXLINE)) > 0)\n    {\n        recvline[n] = 0;\n        if (fputs(recvline, stdout) == EOF)\n        {\n            printf("fputs error\\n");\n            exit(1);\n        }\n    }\n    if (n < 0)\n    {\n        printf("read error\\n");\n        exit(1);\n    }\n\n    exit(0);\n}', 'index': 0, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 13, 'completion_tokens': 523, 'total_tokens': 536}}

key_list_index =0
key_list_max = len(key_list)
proxies = { 'http': 'http://127.0.0.1:40880','https': 'http://127.0.0.1:40880'}
import requests
import json
import time
class Gpt():

    def __init__(self):
        self.prompt = "你今年多大？"
        self.openai_api_key = list(key_list.keys())[1]
        #self.openai_engine = "davinci-codex"
        self.openai_engine = "text-davinci-003"
        self.url = "https://api.openai.com/v1/engines/"+self.openai_engine+"/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_api_key}"
        }
        self.data = {
            "prompt": self.prompt,
            "max_tokens": 100,
            "n": 1,
            "stop": ".",
            "temperature": 0.1,
        }
    def get_free_key(self):
        global key_list
        global key_list_index
        global key_list_max

        for i in range(5):
            for cnt in range(key_list_max):
                key_list_index+=1
                index = key_list_index % key_list_max
                key =list(key_list.keys())[index]
                status = key_list[key]
                if status == "free":
                    key_list[key] = "used"
                    return key
            time.sleep(0.1)
        print("获取key超时")
        return None

    def free(self,key):
        global key_list
        key_list[key] = "free"

    def get_session(self, text = ""):
        if text != "":
            self.prompt = text

        self.data = {
            "prompt": self.prompt,
            "max_tokens": 3000,
            "n": 1,
         #   "stop": "。",
            "temperature": 0.1,
        }
        print( self.data)
        response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data), proxies=proxies)
        print(response)
        if response.status_code == 200:
            result = response.json()
            print(result)
            return result['choices'][0]['text']
        else:
            return "链接错误"

    def get_session_with_param(self, param):
        print("chatgpt in:",param)
        if param == "":
            return "参数错误"
        for cnt in range(5):
            self.openai_api_key = self.get_free_key()
            print("key:",self.openai_api_key)
            if self.openai_api_key == None:
                return "连接数量过多，获取不到key"

            self.headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai_api_key}"
            }

            self.data = param
            response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data), proxies=proxies)
            self.free(self.openai_api_key)

            if response.status_code == 200:
                result = response.json()
                ret_data =result['choices'][0]['text']
                print("chatgpt out:",ret_data)
                return ret_data
            else:
                print(cnt,response)

        return "链接错误"

if __name__ == '__main__':
    chatgpt = Gpt()
    t = "你今年多少岁？"
    ret=chatgpt.get_session(t)
    print(ret)