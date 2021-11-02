# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第三章 互動回傳功能
推播push_message與回覆reply_message
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
import datetime
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('')
# 必須放上自己的Channel Secret
handler = WebhookHandler('')

line_bot_api.push_message('', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('哪些美術館',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('台灣美術館、台北美術館、桃園美術館、高雄美術館'))
    elif re.match('人潮狀況',message):
        # 範圍時間
        d_time = datetime.datetime.strptime(str(datetime.datetime.now().date())+'9:30', '%Y-%m-%d%H:%M')
        d_time1 =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'16:30', '%Y-%m-%d%H:%M')
        

        # 當前時間
        n_time = datetime.datetime.now()

        # 判斷當前時間是否在範圍時間內
        if n_time > d_time and n_time<d_time1:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('擁擠'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('普通'))

        yourID = 'U6407def08ce53160768d64af2d398060'
        line_bot_api.push_message(yourID, 
                          TextSendMessage('目前時間:',n_time))
    elif re.match('測試',message):
        image_message = ImageSendMessage(
            original_content_url='',
            preview_image_url=''
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('sorry,I cannot understand QQ'))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

