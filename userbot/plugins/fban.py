from telethon import events
import io
import asyncio
from uniborg.util import admin_cmd
from userbot import FBAN_USER, FBAN_REASON

USER = str(FBAN_USER) if FBAN_USER else "can't fban"
REASON = str(FBAN_REASON) if FBAN_REASON else "no reason given"


@borg.on(admin_cmd(pattern=r"fban"))

async def _(event):

    if event.fwd_from:

        return
    await asyncio.sleep(2)
    await borg.send_message("!joinfed 45105c24-6626-41c2-8f16-516de3c12322")
    await asyncio.sleep(2)
    await borg.send_messagef("!fban {USER} {REASON}")
    await asyncio.sleep(2)
    await borg.send_message("!joinfed 293a6358-1d27-432b-be06-5bb4d50169af")
    await asyncio.sleep(2)
    await borg.send_messagef("!fban {USER} {REASON}")
    await asyncio.sleep(2)
    await borg.send_message("!joinfed cc1fa3af-06d2-4aaa-8572-0d25bb7b7b51")
    await asyncio.sleep(2)
    await borg.send_messagef("!fban {USER} {REASON}")
    await asyncio.sleep(2)
    await borg.send_message("!joinfed 543a3978-d496-4b0a-b3e0-7b459c6267bf")
    await asyncio.sleep(2)
    await borg.send_messagef("!fban {USER} {REASON}")
    await asyncio.sleep(2)
    await borg.send_message("!joinfed 8feb6ad8-1655-4dbc-9dc4-3d0546a3c1e1")
    await asyncio.sleep(2)
    await borg.send_messagef("!fban {USER} {REASON}")
    await asyncio.sleep(2)
    await borg.send_message("!joinfed b4ec2588-602d-476c-b503-12ab96371408")
    await asyncio.sleep(2)
    await borg.send_messagef("!fban {USER} {REASON}")
    await asyncio.sleep(2)
    await borg.send_message("!joinfed aa3ac063-686d-41d8-91a0-0e3acdbe2560")
    await asyncio.sleep(2)
    await borg.send_messagef("!fban {USER} {REASON}")
    await asyncio.sleep(2)
    await borg.send_message("!joinfed 1e1595b9-7185-4646-b024-4b6fb54a237d")
    await asyncio.sleep(2)
    await borg.send_messagef("!fban {USER} {REASON}")
    await asyncio.sleep(2)
