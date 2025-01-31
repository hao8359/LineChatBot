import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, MessageTemplateAction, FlexSendMessage

from fsm import TocMachine
from utils import send_text_message, send_button_message

load_dotenv()


machine = TocMachine(
    states=["user", "state1", "state2", "state3", "state4", "state5", "state6", "state7", "state8", "state9", "state10", "state11", "state12", "state13", "state14", "state15", "state16","state17"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state3",
            "conditions": "is_going_to_state3",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state4",
            "conditions": "is_going_to_state4",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state5",
            "conditions": "is_going_to_state5",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state6",
            "conditions": "is_going_to_state6",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state7",
            "conditions": "is_going_to_state7",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state8",
            "conditions": "is_going_to_state8",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state9",
            "conditions": "is_going_to_state9",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state10",
            "conditions": "is_going_to_state10",
        },
	{
            "trigger": "advance",
            "source": "user",
            "dest": "state11",
            "conditions": "is_going_to_state11",
        },
	    {
            "trigger": "advance",
            "source": "user",
            "dest": "state12",
            "conditions": "is_going_to_state12",
        },
	    {
            "trigger": "advance",
            "source": "user",
            "dest": "state13",
            "conditions": "is_going_to_state13",
        },
	    {
            "trigger": "advance",
            "source": "user",
            "dest": "state14",
            "conditions": "is_going_to_state14",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state15",
            "conditions": "is_going_to_state15",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state16",
            "conditions": "is_going_to_state16",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state17",
            "conditions": "is_going_to_state17",
        },
        {"trigger": "go_back", "source": ["state1", "state2", "state3", "state4", "state5", "state6", "state7", "state8", "state9", "state10", "state11", "state12", "state13", "state14", "state15", "state16", "state17"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True, 
)
'''machine.get_graph().draw("fsm.png", prog="dot", format="png")'''
app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "請輸入[幫助]獲取更多資訊呦~")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)