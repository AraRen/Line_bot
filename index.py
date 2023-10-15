from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['cD2clxRIfykPoyplgp8b/OUO/W7zWcBydw1KkQ7kj7mdXSWP44p9g2c6XBZ3jPr4yslO4j0a2PmiDa0nHsZYbL1WQ/5VMsF2vevoFDanA8ZDqAXP301sb8EFbAQfEzgXISuyVhMjxuoc3mMjiE7xWwdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['e4781621730cfa0a215bf26cdec323e5'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)