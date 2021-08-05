from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def help(udbot, msg):
    print("/help")
    await udbot.send_message(
        msg.chat.id,
        "**Here's How to use me**\n" + Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
