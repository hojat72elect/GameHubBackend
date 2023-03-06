import requests

from bots.tokens import TELEGRAM_BOT_TOKEN

# We need to first find the chat ID for target user

url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"

print(requests.get(url).json())

# now we have the Chat_ID and can send a message to them
chatId = "2005055437"
message = "Hey man!\ni have made an Android app, please have a look at it " \
          "here:\nhttps://play.google.com/store/apps/details?id=ca.on.hojat.gamenews&hl=en_CA&gl=US"

url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={chatId}&text={message}"

# this sends the message:
result = requests.get(url).json()
print(result)
