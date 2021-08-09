from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nI can search words from Urban Dictionary and give them to you. I will provide it's definition as well as example \n\nYou can send any word here or Try using my inline mode. \n\nBy @StarkBots"

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔍 Search Inline 🔍", switch_inline_query_current_chat="")],
        [
            InlineKeyboardButton(
                "➕ Add to your Group ➕", url="https://t.me/TheUrbanDictBot?startgroup=True"
            )
        ],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("Search Inline 🔍", switch_inline_query_current_chat=""),
            InlineKeyboardButton("How to Use ❔", callback_data="help")
        ],
        [
            InlineKeyboardButton("🎪 About The Bot 🎪", callback_data="about")
        ],
        [
            InlineKeyboardButton(
                "➕ Add to your Group ➕", url="https://t.me/TheUrbanDictBot?startgroup=True"
            )
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
1) **Inline Mode** (recommended)
 ~ Search any word or word sequence in inline mode, any time.
 ~ Use "`-r`" to get random word

2) **Private Chat**
 ~ Send any word or word sequence privately, any time.
 ~ Send "/random" to get random word.

3) **Group Chats**
 ~ Add in group and reply to any message with /ud or /search".
 ~ You can also use: "/ud text here" or "/search text here" in groups.
 ~ Send "/random" to get random word.
(If doesn't responds in group then make it admin. Telegram is weird)
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/UrbanDictionaryBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """