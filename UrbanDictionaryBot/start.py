from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(udbot, msg):
	print("/start")
	user = await udbot.get_me()
	mention = user["mention"]
	await udbot.send_message(
		msg.chat.id,
		Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons),
	)
