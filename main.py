from telethon import TelegramClient , events
from const import *


client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(outgoing=True,pattern='hello'))
async def handler(event):
    chat = await event.get_chat()
    await client.send_message(chat, 'Hello bro first step completed')

client.start()
client.run_until_disconnected()