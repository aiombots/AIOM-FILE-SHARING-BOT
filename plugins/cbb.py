#(©)Codexbotz | @ajvadntr

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b>╭────[ Vɪɴᴄᴇɴᴢ๏ ]───⍟
│
├ Bᴏᴛ Nᴀᴍᴇ : <a href="https://t.me/VINCENZO_CASSANO_ROBOT">Vɪɴᴄᴇɴᴢ๏</a>
│
├ Cʜᴀɴɴᴇʟ : <a href="https://t.me/AIOM_BOTS">ƛƖƠM ƁƠƬƧ"</a>
│
├ Vᴇʀsɪᴏɴ : 1.0.2.2  Bᴇᴛᴀ
│
├ Sᴇʀᴠᴇʀ : <a href="https://www.heroku.com">Hᴇʀᴏᴋᴜ</a>
│
├ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href="https://t.me/ajvadntr">Cʟɪᴄᴋ Hᴇʀᴇ</a>
│
├ Pᴏᴡᴇʀᴇᴅ Bʏ : <a href="https://t.me/AIOM_BOTS">ƛƖƠM ƁƠƬƧ"</a>
│
╰──────[ Tʜᴀɴᴋ Yᴏᴜ ]───⍟</b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/AIOM_BOTS"),
                        InlineKeyboardButton("Gʀᴏᴜᴘ", url="https://t.me/AllinOneMoviesTalks")
                    ],[
                        InlineKeyboardButton("Cʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
