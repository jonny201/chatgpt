import random

session_index = 0
user_id_session_dict = {"00000000": [{"you": "我是谁？", "gpt": "你是你妈妈的孩子"}, {"you": "我在哪？", "gpt": "你在地球上"}]
                        }


def create_user():
    global session_index
    global user_id_session_dict
    userid = str(random.randint(1000000000, 10000000000)) + str(session_index)
    session_index += 1
    user_id_session_dict[userid] = []
    return userid


def add_session(userid, you_session, gpt_session):
    if len(user_id_session_dict[userid]) >= 10:
        user_id_session_dict[userid].pop(0)
    user_id_session_dict[userid].append({"you": you_session, "gpt": gpt_session})


def get_session(userid):
    statement = ""
    session_list = user_id_session_dict[userid]
    for session in session_list:
        statement += "you:" + session["you"] + "\n"
        statement += "gpt:" + session["gpt"] + "\n"
    return statement


if __name__ == '__main__':
    ret = get_session("00000000")
    print(ret)
