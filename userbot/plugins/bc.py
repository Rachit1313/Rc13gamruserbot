from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("bc"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
            "Chup",
            "Chup Bc",
            "Chup Behnchod",
           
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %5 ])
