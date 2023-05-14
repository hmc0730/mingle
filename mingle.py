from slack_sdk import WebClient
from info import slack_bot_token

class mingle:
    def __init__(self, token):
        self.client = WebClient(token)

    def get_channel_id(self, channel_name):
        result = self.client.conversations_list()
        channels = result.data['channels']
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        channel_id = channel["id"]
        return channel_id

    def get_message_id(self, channel_id, query):
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data["messages"]
        message = list(filter(lambda m: m['text'] == query, messages))[0]
        message_id = message["ts"]
        return message_id

    def get_user_id(self, channel_id):
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data["messages"]
        return messages[0]['user']

    def get_recent_n_message(self, channel_id, n):
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data["messages"]
        message = []
        for i in messages:
            message.append(i["text"])
        return message[:n]

    def get_message(self, channel_id, i):
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data["messages"]
        message = []
        for n in messages:
            message.append(n["text"])
        return str(message[i])

    def get_recent_n_messages(self, channel_id, n):
        result = self.client.conversations_history(channel=channel_id)
        messages = result.data["messages"]
        message = []
        for i in messages:
            message.append(i["text"])

        return str(' '.join(message[:n]))

    def post_message_in_thread(self, channel_id, message, text):
        result = self.client.chat_postMessage(
            channel=channel_id,
            thread_ts=message,
            text=text
        )

    def post_message_in_channel(self, channel_id, text):
        result = self.client.chat_postMessage(
            channel=channel_id,
            text=text
        )


myBot = mingle(slack_bot_token)
'''channel_id = myBot.get_channel_id("답변")
myBot.post_message_in_channel(channel_id, "Hi")'''

channel_id = myBot.get_channel_id("일일호프")
print(myBot.get_recent_n_message(channel_id, 3))
'''
user1_id = "U057778KW15"
user2_id = "U057776GZ47"

channel_id = myBot.get_channel_id("스터디")
print(myBot.get_message(channel_id))
message = myBot.get_message_id(channel_id, "#일일호프")
result = myBot.post_message_in_thread(channel_id, message, ".... 정보를 보내드릴게요")'''