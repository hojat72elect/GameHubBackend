from telethon import TelegramClient
import asyncio

from telethon.tl.types import InputPeerUser

from bots.tokens import TELEGRAM_API_ID, TELEGRAM_API_HASH

"""
Don't pay attention to other files in this directory, 
this is the correct way to send a message in python.
"""


async def sendMessage() -> asyncio.coroutine:
    client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    await client.start()

    receiver = InputPeerUser(user_id=2005055437, access_hash=-300479617109090590)

    # print(client.get_me().stringify())  # just returns info about myself

    # the message to be sent
    message = f"Hey there! 👋\nThis is an Android app for following all the latest news about video games; I promise " \
              f"you'll enjoy it a lot:\nhttps://play.google.com/store/apps/details?id=ca.on.hojat.gamenews"

    # All the recipients
    await client.send_message(receiver, message)


asyncio.run(sendMessage())
