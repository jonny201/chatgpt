import socket
import json
# 设置服务器地址和端口号
SERVER_NAME = 't35977451f.zicp.vip'
SERVER_PORT = 48041
prompt = "我是说，我在那，我在干什么"
data = {
            "prompt": prompt,
            "max_tokens": 300,
            "n": 1,
            "stop": ".",
            "temperature": 0.1,
        }
json_data = json.dumps(data, indent=4)
# 解析域名获取 IP 地址
SERVER_ADDRESS = socket.gethostbyname(SERVER_NAME)

# 创建一个 TCP 客户端套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# 发送数据
message = 'Hello, server!'
client_socket.send(message.encode())

# 接收数据
response = client_socket.recv(1024)
print(response.decode())

# 关闭套接字
client_socket.close()