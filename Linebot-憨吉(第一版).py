from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('4rhwwxhnHMXuHocQo/cDlkU4wT46Awv+IFvdRJeDef7kqjCDpGBeGkwKEzXSW1fDs8ESUGShD5lRnQHtSGiWlBf87oQc2o3+R3X5cnC0TsgnzwuCmWLzV7dDZh+XAJLckOnWh44rB9P11RuJ3Cu/iAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cd1137084b9fc84198e7813e2e310151')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = event.message.text

    if message_text == 'help':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='指令:\n'
                                 '作者\n'
                                 '憨吉\n'
                                 '好香\n'
                                 '笑話仔爛梗'))

    if message_text == '作者':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='to by foxicetw(小冰)'))
    elif message_text == '憨吉':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='阿利憨吉!'))
    elif message_text == '好香':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='真香啊!'))
    elif message_text == '笑話仔爛梗':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="先進船的人會先說什麼？\n"
                                 " \n"
                                 "會說online\n"
                                 " \n"
                                 ".\n"
                                 " \n"
                                 ".\n"
                                 " \n"
                                 ".\n"
                                 " \n"
                                 "因為仙境傳說online。\n"
                                 "XDDDDD"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='請打指令!'))

if __name__ == "__main__":
    app.run()
