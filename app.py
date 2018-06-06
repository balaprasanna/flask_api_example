slack_token = "xoxp-373219160785-374655318694-376231293956-a6532fb79f77b6a1fa1ece2ed374d5db"
from slackclient import SlackClient

# Explain later
# slack_token = os.environ["SLACK_API_TOKEN"]

# Utility Functions:
def send_message_to_slack(channel, message):
    sc = SlackClient(slack_token)
    print ("Sending message ??")
    print (channel, message)
    sc.api_call( "chat.postMessage", channel=channel, text=message )


# Main code starts here:

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/sendmessage', methods=['GET'])
def postMessage():
    text = request.args.get('text')
    print (text)
    channel = "general"
    send_message_to_slack(channel, text)
    return "Message sent successfully : {}".format(text)


@app.route('/sendmessage_to_channel', methods=['GET'])
def postMessagetoAChannel():
    channel = request.args.get('channel')
    text = request.args.get('text')
    
    send_message_to_slack(channel, text)
    return "Message sent successfully to {} channel".format(channel)

# to make sure everyone can access
app.run(host= '0.0.0.0')