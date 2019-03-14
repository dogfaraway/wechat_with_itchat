#!usr/bin/env python3
# -*- coding:utf-8-*-

import itchat
import json
import requests

# 回复好友
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

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
        print(data['userInfo']['userId'] , text)
        url = 'http://openapi.tuling123.com/openapi/api/v2'
        response = requests.post(url=url, data=json.dumps(data))
        response.encoding = 'utf-8'
        result = response.json()
        answer = result['results'][0]['values']['text']
        print('机器人回复：' + answer)  # 打印机器人回复
        return answer


    myUserName = itchat.get_friends(update=True)[0]["UserName"]  ##获取自己的username
    print('myUserName=', myUserName)
    print('opponentUserName=', msg['FromUserName'])  ##获取发消息的好友的username
    return "我是tao的图灵机器人：" + get_answer(msg["Text"] )

# 发送群聊
@itchat.msg_register(itchat.content.TEXT, isGroupChat=False)
def group_text_reply(msg):

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
        print(data['userInfo']['userId'], text)
        url = 'http://openapi.tuling123.com/openapi/api/v2'
        response = requests.post(url=url, data=json.dumps(data))
        response.encoding = 'utf-8'
        result = response.json()
        answer = result['results'][0]['values']['text']
        print('机器人回复：' + answer)  # 打印机器人回复
        return answer


    return "我是tao的图灵机器人：" + get_answer(msg["Text"])



itchat.auto_login(hotReload=True, enableCmdQR=False)
itchat.run()

# 作者：mocokoo
# 链接：https://www.jianshu.com/p/62fe9dbe64c6
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
