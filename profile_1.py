from telethon import TelegramClient , events
from const import *
import os


client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(outgoing=True,pattern='hello'))
async def handler(event):
    chat = await event.get_chat()
    # await client.send_message(chat, 'Hello bro first step completed')
    await client.edit_message(event.message, 'Hello!! it is edited')


@client.on(events.NewMessage(outgoing=True,pattern=r'\.alive'))
async def handler(event):
    chat = await event.get_chat()
    await client.delete_messages(chat, event.message)
    photo = await client.download_profile_photo('me')
    await client.send_file(chat, file=photo,caption='This is my profile picture')
    os.remove(photo)
client.start()
client.run_until_disconnected()