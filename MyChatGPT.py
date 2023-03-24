key_list = {
    "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": "free",
    "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": "free",
    "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": "free"
}

key_list_index = 0
key_list_max = len(key_list)
proxies = {'http': 'http://127.0.0.1:40880', 'https': 'http://127.0.0.1:40880'}
import requests
import json
import time


class Gpt():

    def __init__(self):
        self.prompt = "你今年多大？"
        self.openai_api_key = list(key_list.keys())[2]
        # self.openai_engine = "davinci-codex"
        self.openai_engine = "text-davinci-003"
        self.url = "https://api.openai.com/v1/engines/" + self.openai_engine + "/completions"
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
                key_list_index += 1
                index = key_list_index % key_list_max
                key = list(key_list.keys())[index]
                status = key_list[key]
                if status == "free":
                    key_list[key] = "used"
                    return key
            time.sleep(0.1)
        print("获取key超时")
        return None

    def free(self, key):
        global key_list
        key_list[key] = "free"

    def get_session(self, text=""):
        if text != "":
            self.prompt = text

        data = {
            "prompt": self.prompt,
            "max_tokens": 3000,
            "n": 1,
            "stop": ["\nyou:", "\ngpt:"],
            "temperature": 0.1,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.6,
        }
        return self.get_session_with_param(data)

    def get_session_with_param(self, param):
        print("chatgpt in:", param)
        if param == "":
            return "参数错误", False

        prompt = param.get("prompt")
        if prompt == None:
            return "参数错误", False

        self.data = {
            "prompt": prompt,
            "max_tokens": param.get("max_tokens", 3000),
            "n": param.get("max_tokens", 1),
            "temperature": param.get("temperature", 0.1),
        }
        stop = param.get("stop")
        if stop != None:
            self.data["stop"] = stop

        frequency_penalty = param.get("frequency_penalty")
        if frequency_penalty != None:
            self.data["frequency_penalty"] = frequency_penalty

        presence_penalty = param.get("presence_penalty")
        if presence_penalty != None:
            self.data["presence_penalty"] = presence_penalty

        for cnt in range(5):
            self.openai_api_key = self.get_free_key()
            print("key:", self.openai_api_key)
            if self.openai_api_key == None:
                return "连接数量过多，获取不到key", False

            self.headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai_api_key}"
            }

            self.data = param
            response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data), proxies=proxies)
            self.free(self.openai_api_key)

            if response.status_code == 200:
                result = response.json()
                ret_data = result['choices'][0]['text']
                print("chatgpt out:", ret_data)
                return ret_data, True
            else:
                print(cnt, response)

        return "链接错误", False


if __name__ == '__main__':
    chatgpt = Gpt()
    t = "你今年多少岁？"
    ret = chatgpt.get_session(t)
    print(ret)
