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
        elif text in ["2", "2.", "2. 羽球"]:
            pingpang_text = (
                "以下為 Coachlinks 的官方「羽球」技術筆記$\n"
                "$請幫我選擇您有興趣的技術項目名稱~\n\n"
                "2-1. 網前勾對角\n"
                "2-2. 後場過渡球\n"
                "2-3. 正手發球\n"
                "2-4. 反手發球\n"
                "2-5. 雙打防守\n"
                "2-6. 握拍 & 發力\n"
                "2-7. 反手長球\n"
                "2-8. 滑拍\n"
                "2-9. 殺球\n"
                "2-10. 切球\n"
                "2-11. 長球\n"
                "2-12. 挑球\n"
                "2-13. 平抽球\n"
                "2-14. 網前放小球\n"
                "2-15. 網前推球"
            )

            pingpang_text_indices = [i for i, char in enumerate(pingpang_text) if char == '$']

            pingpang_text_emojis = [
                Emoji(index=pingpang_text_indices[0], product_id="5ac21a18040ab15980c9b43e", emoji_id="136"),
                Emoji(index=pingpang_text_indices[1], product_id="5ac21a18040ab15980c9b43e", emoji_id="087")
            ]

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text=pingpang_text, emojis=pingpang_text_emojis)
                    ]
                )
            )
        elif "2-" in text:
            product_id_0 = "5ac218e3040ab15980c9b43c"
            emoji_id_0 = "037"
            product_id_1 = "5ac21a18040ab15980c9b43e"
            emoji_id_1 = "087"

            if text in ["2-1", "2-1.", "2-1. 網前勾對角"]:

                # 1. 網前勾對角：
                # 8B8B720D-D8C0-4D67-ADCB-246E85970F5E

                badminton_1_text = "$網前勾對角\n$技術筆記 ID"
                badminton_1_text_indices = [i for i, char in enumerate(badminton_1_text) if char == '$']
                badminton_1_emoji = [
                    Emoji(index=badminton_1_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_1_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_1_id = "8B8B720D-D8C0-4D67-ADCB-246E85970F5E"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_1_text, emojis=badminton_1_emoji),
                            TextMessage(text=badminton_1_id)
                        ]
                    )
                )
            elif text in ["2-2", "2-2.", "2-2. 後場過渡球"]:

                # 2. 後場過渡球：
                # d3d98ac8-4c7c-47d5-ab5f-cd80ddee895f

                badminton_2_text = "$後場過渡球\n$技術筆記 ID"
                badminton_2_text_indices = [i for i, char in enumerate(badminton_2_text) if char == '$']
                badminton_2_emoji = [
                    Emoji(index=badminton_2_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_2_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_2_id = "d3d98ac8-4c7c-47d5-ab5f-cd80ddee895f"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_2_text, emojis=badminton_2_emoji),
                            TextMessage(text=badminton_2_id)
                        ]
                    )
                )
            elif text in ["2-3", "2-3.", "2-3. 正手發球"]:
                
                # 3. 正手發球：
                # 5611242e-7c45-4be5-b83d-f15785904584

                badminton_3_text = "$正手發球\n$技術筆記 ID"
                badminton_3_text_indices = [i for i, char in enumerate(badminton_3_text) if char == '$']
                badminton_3_emoji = [
                    Emoji(index=badminton_3_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_3_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_3_id = "5611242e-7c45-4be5-b83d-f15785904584"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_3_text, emojis=badminton_3_emoji),
                            TextMessage(text=badminton_3_id)
                        ]
                    )
                )
            elif text in ["2-4", "2-4.", "2-4. 反手發球"]:

                # 4. 反手發球：
                # 61f0314e-f39e-4c89-a331-7dfee1529a19

                badminton_4_text = "$反手發球\n$技術筆記 ID"
                badminton_4_text_indices = [i for i, char in enumerate(badminton_4_text) if char == '$']
                badminton_4_emoji = [
                    Emoji(index=badminton_4_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_4_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_4_id = "61f0314e-f39e-4c89-a331-7dfee1529a19"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_4_text, emojis=badminton_4_emoji),
                            TextMessage(text=badminton_4_id)
                        ]
                    )
                )
            elif text in ["2-5", "2-.5", "2-5. 雙打防守"]:

                # 5. 雙打防守：
                # 6d76f5c0-695f-4352-a0da-183ea946cede

                badminton_5_text = "$雙打防守\n$技術筆記 ID"
                badminton_5_text_indices = [i for i, char in enumerate(badminton_5_text) if char == '$']
                badminton_5_emoji = [
                    Emoji(index=badminton_5_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_5_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_5_id = "6d76f5c0-695f-4352-a0da-183ea946cede"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_5_text, emojis=badminton_5_emoji),
                            TextMessage(text=badminton_5_id)
                        ]
                    )
                )
            elif text in ["2-6", "2-6.", "2-6. 握拍 & 發力"]:

                # 6. 握拍 & 發力：
                # 22e9c2f8-705d-423e-ab46-d2764abcbacb

                badminton_6_text = "$握拍 & 發力\n$技術筆記 ID"
                badminton_6_text_indices = [i for i, char in enumerate(badminton_6_text) if char == '$']
                badminton_6_emoji = [
                    Emoji(index=badminton_6_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_6_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_6_id = "22e9c2f8-705d-423e-ab46-d2764abcbacb"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_6_text, emojis=badminton_6_emoji),
                            TextMessage(text=badminton_6_id)
                        ]
                    )
                )
            elif text in ["2-7", "2-7.", "2-7. 反手長球"]:

                # 7. 反手長球：
                # b81b3f3a-6823-4ed0-9f07-feffc58a02c4

                badminton_7_text = "$反手長球\n$技術筆記 ID"
                badminton_7_text_indices = [i for i, char in enumerate(badminton_7_text) if char == '$']
                badminton_7_emoji = [
                    Emoji(index=badminton_7_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_7_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_7_id = "b81b3f3a-6823-4ed0-9f07-feffc58a02c4"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_7_text, emojis=badminton_7_emoji),
                            TextMessage(text=badminton_7_id)
                        ]
                    )
                )
            elif text in ["2-8", "2-8.", "2-8. 滑拍"]:

                # 8. 滑拍：
                # b6077bda-c5ce-45fb-b8b2-cab9561ac2b8

                badminton_8_text = "$滑拍\n$技術筆記 ID"
                badminton_8_text_indices = [i for i, char in enumerate(badminton_8_text) if char == '$']
                badminton_8_emoji = [
                    Emoji(index=badminton_8_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_8_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_8_id = "b6077bda-c5ce-45fb-b8b2-cab9561ac2b8"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_8_text, emojis=badminton_8_emoji),
                            TextMessage(text=badminton_8_id)
                        ]
                    )
                )
            elif text in ["2-9", "2-9.", "2-9. 殺球"]:

                # 9. 殺球：
                # 7f538213-291c-4332-b90b-b107ff3b146d

                badminton_9_text = "$殺球\n$技術筆記 ID"
                badminton_9_text_indices = [i for i, char in enumerate(badminton_9_text) if char == '$']
                badminton_9_emoji = [
                    Emoji(index=badminton_9_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_9_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_9_id = "7f538213-291c-4332-b90b-b107ff3b146d"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_9_text, emojis=badminton_9_emoji),
                            TextMessage(text=badminton_9_id)
                        ]
                    )
                )
            elif text in ["2-10", "2-10.", "2-10. 切球"]:

                # 10. 切球：
                # 6f04aa32-fd21-4bdb-8eed-be12786d3452

                badminton_10_text = "$切球\n$技術筆記 ID"
                badminton_10_text_indices = [i for i, char in enumerate(badminton_10_text) if char == '$']
                badminton_10_emoji = [
                    Emoji(index=badminton_10_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_10_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_10_id = "6f04aa32-fd21-4bdb-8eed-be12786d3452"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_10_text, emojis=badminton_10_emoji),
                            TextMessage(text=badminton_10_id)
                        ]
                    )
                )
            elif text in ["2-11", "2-11.", "2-11. 長球"]:

                # 11. 長球：
                # 2D7F49F1-3116-4F91-BBF6-F33C738920E4

                badminton_11_text = "$長球\n$技術筆記 ID"
                badminton_11_text_indices = [i for i, char in enumerate(badminton_11_text) if char == '$']
                badminton_11_emoji = [
                    Emoji(index=badminton_11_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_11_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_11_id = "2D7F49F1-3116-4F91-BBF6-F33C738920E4"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_11_text, emojis=badminton_11_emoji),
                            TextMessage(text=badminton_11_id)
                        ]
                    )
                )
            elif text in ["2-12", "2-12.", "2-12. 挑球"]:

                # 12. 挑球：
                # 950C3C0B-BA7F-4118-B414-A2F9279A7F9B

                badminton_12_text = "$挑球\n$技術筆記 ID"
                badminton_12_text_indices = [i for i, char in enumerate(badminton_12_text) if char == '$']
                badminton_12_emoji = [
                    Emoji(index=badminton_12_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_12_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_12_id = "950C3C0B-BA7F-4118-B414-A2F9279A7F9B"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_12_text, emojis=badminton_12_emoji),
                            TextMessage(text=badminton_12_id)
                        ]
                    )
                )
            elif text in ["2-13", "2-13.", "2-13. 平抽球"]:

                # 13. 平抽球：
                # 22A1CF6B-68E4-4F0B-938B-E4171347558B

                badminton_13_text = "$平抽球\n$技術筆記 ID"
                badminton_13_text_indices = [i for i, char in enumerate(badminton_13_text) if char == '$']
                badminton_13_emoji = [
                    Emoji(index=badminton_13_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_13_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_13_id = "22A1CF6B-68E4-4F0B-938B-E4171347558B"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_13_text, emojis=badminton_13_emoji),
                            TextMessage(text=badminton_13_id)
                        ]
                    )
                )
            elif text in ["2-14", "2-14.", "2-14. 網前放小球"]:

                # 14. 網前放小球：
                # CF71E691-7F6D-495A-A657-AD0DCEDE108F

                badminton_14_text = "$網前放小球\n$技術筆記 ID"
                badminton_14_text_indices = [i for i, char in enumerate(badminton_14_text) if char == '$']
                badminton_14_emoji = [
                    Emoji(index=badminton_14_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_14_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_14_id = "CF71E691-7F6D-495A-A657-AD0DCEDE108F"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_14_text, emojis=badminton_14_emoji),
                            TextMessage(text=badminton_14_id)
                        ]
                    )
                )
            elif text in ["2-15", "2-15.", "2-15. 網前推球"]:

                # 15. 網前推球：
                # E2400424-6EA5-45DE-9282-5CD7E8434840

                badminton_15_text = "$網前推球\n$技術筆記 ID"
                badminton_15_text_indices = [i for i, char in enumerate(badminton_15_text) if char == '$']
                badminton_15_emoji = [
                    Emoji(index=badminton_15_text_indices[0], product_id=product_id_0, emoji_id=emoji_id_0),
                    Emoji(index=badminton_15_text_indices[1], product_id=product_id_1, emoji_id=emoji_id_1)
                ]

                badminton_15_id = "E2400424-6EA5-45DE-9282-5CD7E8434840"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(text=badminton_15_text, emojis=badminton_15_emoji),
                            TextMessage(text=badminton_15_id)
                        ]
                    )
                )

if __name__ == "__main__":
    app.run()