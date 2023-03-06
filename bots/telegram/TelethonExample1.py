from sys import excepthook

from telethon import TelegramClient, events, sync

from bots.tokens import TELEGRAM_API_ID, TELEGRAM_API_HASH

# given that you already have your telegram API ID and API hash,
# here you can create a telegram client.

client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
client.start()

print(client.get_me().stringify())  # just returns info about myself

# the message to be sent
message = f"Hey there! 👋\n This is an Android app for following all the latest news about video games; I promise " \
          f"you'll enjoy it a lot:\nhttps://play.google.com/store/apps/details?id=ca.on.hojat.gamenews"

# All the recipients
try:
    client.send_message('hojat72elect', message)
    client.send_message('dmikots', message)
    client.send_message('mksmyoucan', message)
    client.send_message('Ilsave7', message)
    client.send_message('kylichist', message)
except:
    print("an error occurred")
