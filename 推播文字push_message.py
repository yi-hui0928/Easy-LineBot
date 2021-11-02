# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 21:37:37 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第三章 互動回傳功能
推播push_message與回覆reply_message
"""
from linebot import LineBotApi
from linebot.models import TextSendMessage
import time

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('')
# 請填入您的ID
yourID = ''
# 主動推播訊息
line_bot_api.push_message(yourID, 
                          TextSendMessage(text='台灣美術館即將推出 9/22 開學大禮包 特別活動喔!!'))
# 用迴圈推播訊息
for i in [1,2,3,4,5]:
    line_bot_api.push_message(yourID, 
                              TextSendMessage(text='我們來倒數：'+str(i)))
    time.sleep(1)