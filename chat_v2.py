#!usr/bin/env python3
# -*- coding:utf-8-*-

import itchat
import json
import requests


def get_data(text):
    userId = 'userId'
    inputText = {'text': text}
    key = 'e655ad4711b543e4b1dba7a7dc4a531c'
    userInfo = {'apiKey': key, 'userId': userId}
    perception = {'inputText': inputText}
    data = {'perception': perception, 'userInfo': userInfo}
    return data


def get_answer(text):
    data = get_data(text)
    print(text)
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    response = requests.post(url=url, data=json.dumps(data))
    response.encoding = 'utf-8'
    result = response.json()
    answer = result['results'][0]['values']['text']
    print('机器人回复：' + answer)  # 打印机器人回复
    return answer

# 回复好友
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return "我是tao的图灵机器人：" + get_answer(msg["Text"])

#     myself = itchat.get_friends(update=True)[0]['NickName']
#     content = msg['Content']
#     friend = msg['User']['NickName']
#     # 给特定的人的回复，并且自己发的 不回复
#     if friend != myself and friend!= 'FRIEND':
#         print('%s: %s' % (friend, content))
#         answer = get_answer(msg['Text'])
#         itchat.send(answer, msg['FromUserName'])
#         print('我：%s' % answer)
#     else:
#         itchat.send('您好', msg['FromUserName'])

# 获得群聊ID
def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']

# 发送群聊
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_text_reply(msg):
    group_name = msg['User']['NickName']                                # 获取群聊名称
    group = ['一起啃回忆', 'itchat']                                 # 设置聊天的群
    group_info = itchat.search_chatrooms(name='一起啃回忆')
    item = group_info[0]['UserName']
    if group_name in group:
        itchat.send(get_answer(msg['Text']), item)

itchat.auto_login(hotReload=True)
itchat.run()
