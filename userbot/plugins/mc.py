from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("wtf"))
async def _(event):
    if event.fwd_from:

    await event.edit("madarchod")
   
