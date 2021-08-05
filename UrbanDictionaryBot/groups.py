from UrbanDictionaryBot.heart import ud_search
from pyrogram import Client, filters


# Group Chats
@Client.on_message(filters.group & filters.incoming & filters.command(["ud", "search"]))
async def search(udbot, msg):
    replied = msg.reply_to_message
    if len(msg.command) != 1:
        if msg.command[0] == "ud":
            the_text = msg.text[4:]
            word, rep = await ud_search(the_text)
            await msg.reply(rep)
        elif msg.command[0] == "search":
            the_text = msg.text[8:]
            word, rep = await ud_search(the_text)
            await msg.reply(rep)
    elif replied:
        string = replied.text
        word, rep = await ud_search(string)
        await msg.reply(rep)
    else:
        await msg.reply("`Please reply to a message!`")
    # + random in "randomly.py"
