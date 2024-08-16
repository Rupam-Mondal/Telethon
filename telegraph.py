
from telethon import TelegramClient , events
from const import *
import os
from html_telegraph_poster.upload_images import upload_image

client = TelegramClient('session_name', api_id, api_hash)
@client.on(events.NewMessage(outgoing=True,pattern=r'\.tu'))
async def handler(event):
    replied = await event.get_reply_message()
    img = await replied.download_media()
    link = upload_image(img)
    await client.send_message(event.chat_id, link)
    os.remove(img)
