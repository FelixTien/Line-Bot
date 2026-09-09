from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    Emoji
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
import os

app = Flask(__name__)

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))
line_handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    # Line emoji documentation (The index is the String index) 
    # https://developers.line.biz/en/docs/messaging-api/emoji-list/

    text = event.message.text
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        
        if text == "我想獲取 Coachlinks 技術筆記":
            skill_note_text_1 = "收到！\n請問您想獲取哪項運動項目的技術筆記呢？$"
            skill_note_text_1_indices = [i for i, char in enumerate(skill_note_text_1) if char == '$']
            skill_note_emojis_1 = [
                Emoji(index=skill_note_text_1_indices[0], product_id="670e0cce840a8236ddd4ee4c", emoji_id="071")
            ]

            skill_note_text_2 = "幫我輸入1~4\n我就會提供官方技術筆記的筆記 ID 給您囉！$\n1. 桌球\n2. 羽球\n3. 健身\n4. 匹克球"
            skill_note_text_2_indices = [i for i, char in enumerate(skill_note_text_2) if char == '$']
            skill_note_emojis_2 = [
                Emoji(index=skill_note_text_2_indices[0], product_id="670e0cce840a8236ddd4ee4c", emoji_id="041")
            ]

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text=skill_note_text_1, emojis=skill_note_emojis_1),
                        TextMessage(text=skill_note_text_2, emojis=skill_note_emojis_2)
                    ]
                )
            )

if __name__ == "__main__":
    app.run()