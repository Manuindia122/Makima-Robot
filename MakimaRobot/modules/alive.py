# ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
# sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
# ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
# ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

import random

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import Button
from telethon import __version__ as tlhver

from MakimaRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from MakimaRobot import telethn as tbot

PHOTO = [
    "https://telegra.ph/file/413d85f75e2d012a77f90.jpg",
    "https://telegra.ph/file/413d85f75e2d012a77f90.jpg",
]


async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ {dispatcher.bot.first_name}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ＪＵＭＰＭＡＮ ＢＯＹ⁪⁬⁮](https://t.me/{OWNER_USERNAME})** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)



