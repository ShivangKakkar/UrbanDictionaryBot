from UrbanDictionaryBot.heart import ud_search
from pyrogram import Client, filters


# Private Chat
@Client.on_message(
    filters.private
    & filters.incoming
    & ~filters.command(["start", "ud", "search", "help", "random"])
    & ~filters.via_bot
)
async def answer(udbot, msg):
    string = msg.text
    print("Query: ", string)
    word, rep = await ud_search(string)
    await msg.reply(rep, quote=True)
    # + random in "randomly.py"
