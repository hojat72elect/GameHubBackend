import asyncio

from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from bots.tokens import TELEGRAM_API_ID, TELEGRAM_API_HASH


async def getMembers() -> asyncio.coroutine:
    # Make the client
    client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    client.start()

    channels = ["kotlinmpp"]

    for channel in channels:
        # join the channel
        await client(JoinChannelRequest(channel))

    print("finished")


asyncio.run(getMembers())
