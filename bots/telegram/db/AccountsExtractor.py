from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

from bots.tokens import TELEGRAM_PHONE_NUMBER, TELEGRAM_API_ID, TELEGRAM_API_HASH

"""
I'm giving it my own telegram handle so it can extract the users in all of groups that I'm logged in.
"""

# create the client
client = TelegramClient(
    TELEGRAM_PHONE_NUMBER,
    TELEGRAM_API_ID,
    TELEGRAM_API_HASH
)

# log in
client.connect()
if not client.is_user_authorized():
    client.send_code_request(TELEGRAM_PHONE_NUMBER)
    client.sign_in(TELEGRAM_PHONE_NUMBER, input("Enter the code: "))

# get all of the user's chats
chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup or chat.broadcast:
            groups.append(chat)
    except:
        continue

# All the channels that users is a part of
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1