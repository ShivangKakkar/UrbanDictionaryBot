from UrbanDictionaryBot.heart import rand
from pyrogram import Client, filters


# Random (For Private Chat, Group Chats and Inline Mode)
@Client.on_message((filters.private | filters.group) & filters.incoming & filters.command(["random", "random@TheUrbanDictBot"]))
async def answer(udbot, msg):
    word, rand_string = await rand()
    await msg.reply(rand_string, quote=True)
