from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("gand"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("**Gand**")
    animation_chars = [
            "**Na phulao**",
            "**Jyada**",
            "**Maa chud jaegi**",
            "**Tumhari**",
            "**Gand na phulao jyada ma chod di jaigi tumari**""
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %5 ])
