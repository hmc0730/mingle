import json
from flask import Flask
from info import slack_bot_token_1, slack_signing_secret_1
from mingle import mingle
from slackeventsapi import SlackEventAdapter

myBot = mingle(slack_bot_token_1)
app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(slack_signing_secret_1,'/slack', app)

@slack_event_adapter.on("app_mention")
def handle_mentions(event_data):
    channel = event_data["event"]["channel"]
    message = event_data["event"]["event_ts"]
    text = "일일호프를 진행하는 타 대학 정보를 보내드리겠습니다"
    myBot.post_message_in_thread(channel, message, text)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)

'''import json
from flask import Flask, request, make_response
from info import slack_bot_token_1
from mingle import mingle


myBot = mingle(slack_bot_token_1)
app = Flask(__name__)

channel_in = "C058BLQMZCG"
channel_out = "C0577FMPNB1"


def event_handler(event_type, slack_event):
    #쓰레드에 자동답장
    channel = slack_event["event"]["channel"]
    message = slack_event["event"]["event_ts"]
    
    text = "일일호프를 진행하는 타 대학 정보를 보내드리겠습니다"
    myBot.post_message_in_thread(channel, message, text)

    text2 = myBot.get_message(channel_in, 0)
    myBot.post_message_in_channel(channel_out, text2)


    message = "{%s} 이벤트 핸들러를 찾을 수 없습니다." % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})



@app.route("/slack", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)
    print(request.data)
    print("slack_event:", slack_event)
    if "challenge" in slack_event:
        response_dict = {"challenge": slack_event["challenge"]}
        return response_dict
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)


return make_response("출력 요청에 이벤트가 없습니다.", 404, {"X-Slack-No-Retry": 1})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
'''