from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest

from bots.tokens import TELEGRAM_API_ID, TELEGRAM_API_HASH

# create the client
client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
client.start()

result =  printMembers()


def printMembers():
    # list of telegram groups that we want to scrape
    targetGroup = 'kotlinmpp'
    await client(JoinChannelRequest(targetGroup))
    allMembers = client.get_participants(targetGroup, aggressive=True)

    return allMembers
