from telethon import TelegramClient , events
from const import *
import os

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(pattern='/check'))
async def check_group(event):
    try:
        # Get the group entity from the link
        group_link = event.message.message.split(' ')[1]
        group = await client.get_entity(group_link)
        
        # Fetch recent messages
        async for message in client.iter_messages(group, limit=100):
            # Check if the message has text
            if message.text and detect_adult_content(message.text):
                await event.reply("This group circulates adult content.")
                return

        await event.reply("This group does not seem to circulate adult content.")
    except Exception as e:
        await event.reply(f"Failed to analyze the group: {e}")

def detect_adult_content(text):
    keywords = ['adult', 'porn', 'NSFW'] 
    return any(keyword in text.lower() for keyword in keywords)


client.start()
client.run_until_disconnected()