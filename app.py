slack_token = "xoxp-373219160785-374655318694-377498875543-54c303547e1d2dae997eb6a7509a48cd"
from slackclient import SlackClient

# Explain later
# slack_token = os.environ["SLACK_API_TOKEN"]

# Utility Functions:
def send_message_to_slack(channel, message):
    sc = SlackClient(slack_token)
    sc.api_call( "chat.postMessage", channel=channel, text=message )


# Main code starts here:
