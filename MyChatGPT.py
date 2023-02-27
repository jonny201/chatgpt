key = "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"
proxies = { 'http': 'http://127.0.0.1:40880','https': 'http://127.0.0.1:40880'}
import requests
import json
class Gpt():
    def __init__(self):
        self.prompt = "你今年多大？"
        self.openai_api_key = key
        self.openai_engine = "text-davinci-002"
        self.url = "https://api.openai.com/v1/engines/"+self.openai_engine+"/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_api_key}"
        }
        self.data = {
            "prompt": self.prompt,
            "max_tokens": 300,
            "n": 1,
            "stop": ".",
            "temperature": 0.1,
        }

    def get_session(self, text = ""):
        if text != "":
            self.prompt = text

        self.data = {
            "prompt": self.prompt,
            "max_tokens": 300,
            "n": 1,
            "stop": "\n",
            "temperature": 0.1,
        }
        response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data), proxies=proxies)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['text']
        else:
            return "链接错误"

if __name__ == '__main__':
    chatgpt = Gpt()
    t = "用python 写一个http server"
    ret=chatgpt.get_session(t)
    print(ret)