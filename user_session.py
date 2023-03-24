import random
import datetime
session_index = 0

default_sesion = "\n"

def set_def_session(question,answer):
    global default_sesion
    default_sesion+= "\nyou:"+ question +"\n懒人:"+answer

http_server =""" from ChttpServer import CHttpServer
 def main():
     http_server = CHttpServer.CHttpServer()
     http_server.bind(8000)
     http_server.start()
 
 if __name__ == "__main__":
     main()"""
set_def_session("python 写一个HTTP服务器",http_server)
set_def_session("你是谁？","你就叫我大哥哥吧")
set_def_session("大熊猫是熊还是猫","大熊猫是体积大一点的猫")
set_def_session("你今年多大？","过来今晚我就是貌美如花的18岁")
set_def_session("你是傻子？","不，你比我更傻")
set_def_session("你爱吃什么？","我爱吃青菜")
set_def_session("请用幽默的语句回答下面所有问题","我知道了")
set_def_session("你会什么","我最擅长的技能是让你快乐")
set_def_session("杨干是谁？","杨干是一个上知天文地理，下晓母猪难产野牛繁殖,温柔有爱心的大哥哥")
set_def_session("我是谁","你是一个可爱的小朋友")
set_def_session("陆冬铭是谁","是一个脾气暴躁的小朋友，有时很淘气，有时又很可爱")

user_id_session_dict = {"00000000": {"session_str": default_sesion, "session_str_len": 0, "last_time": 1123, } }

def is_login_session(session_id):
    if user_id_session_dict.get(session_id) ==None:
        return False
    else:
        return True

def create_user():
    global session_index
    global user_id_session_dict
    now = datetime.datetime.now()
    userid = str(random.randint(1000000000, 10000000000)) + str(session_index)
    session_index += 1
    user_id_session_dict[userid] = {"session_str": default_sesion, "session_str_len": 1, "last_time": now }

    return userid

def add_session(userid, session,is_you):
    if is_you:
        temp_session ="you:" + session + "\n"
    else:
        temp_session =  session + "\n"
    temp_session_len = len(temp_session)
    if temp_session_len + user_id_session_dict[userid]["session_str_len"] > 2000:
        user_id_session_dict[userid]["session_str"] = user_id_session_dict[userid]["session_str"][temp_session_len:]
        user_id_session_dict[userid]["session_str_len"] -= temp_session_len

        first_you_index = user_id_session_dict[userid]["session_str"].find("\nyou:")
        user_id_session_dict[userid]["session_str"] = user_id_session_dict[userid]["session_str"][first_you_index:]
        user_id_session_dict[userid]["session_str_len"] -= first_you_index

    user_id_session_dict[userid]["session_str"] += temp_session
    user_id_session_dict[userid]["session_str_len"] += temp_session_len

    user_id_session_dict[userid]["last_time"] = datetime.datetime.now()

    return user_id_session_dict[userid]["session_str"]

if __name__ == '__main__':
    ret = add_session("00000000","ddddd",True)
    ret = add_session("00000000", "12312312", False)
    ret = add_session("00000000", "dddeqweqwdd", True)
    ret = add_session("00000000", "ewqe", False)
    ret = add_session("00000000", "dddereredd", True)
    print(ret)
