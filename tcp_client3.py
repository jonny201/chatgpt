import socket
import json

SERVER_NAME = 't35977451f.zicp.vip'
SERVER_PORT = 48041
class TCPClient:
    def __init__(self, host = SERVER_NAME, port = SERVER_PORT):
        self.host = host
        self.port = port

    def send_message(self, message):
        print("发送数据：",message)
        self.host = socket.gethostbyname(SERVER_NAME)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(message.encode())
            response = sock.recv(1024).decode()
            print("接收数据：",response)
            return response

    def send_json(self,json_data):
        return self.send_message(json.dumps(json_data, indent=4))

if __name__ == '__main__':
    prompt = "我是说，我在那，我在干什么"
    data = {
        "prompt": prompt,
        "max_tokens": 300,
        "n": 1,
        "stop": ".",
        "temperature": 0.1,
    }
    client = TCPClient()
    ret=client.send_json(data)

    print(ret)