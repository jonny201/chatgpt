"""
没登录情况下，不处理参数
带参数请求帧
    data = {
        "session_type": "question",
        "prompt": prompt,
        "param":{
            "max_tokens": 300,
            "n": 1,
            "stop": ".",
            "temperature": 0.1,
        },
        "session_id":session_id,
    }
不带参数请求帧
    data = {
        "session_type": "question",
        "prompt": prompt,
        "session_id":session_id,
    }
登录帧
    data = {
        "session_type": "login",
        "username": "admin",
        "password":"Admin@9000"
    }
"""
def_msg = {
    "key":None,

    "data": {
            "prompt": None,
            "max_tokens": 3000,
            "n": 1,
            "stop": ["\nyou:", "\ngpt:"],
            "temperature": 0.1,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.6,
        }
}