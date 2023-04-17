from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import FORCE_SUB

async def not_subscribed(_, client, message):
    if not client.force_channel:
        return False
    try:             
        user = await client.get_chat_member(client.force_channel, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[ InlineKeyboardButton(text="📢ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ📢", url=f"https://t.me/{FORCE_SUB}") ]]
    text = "**ꜱᴏʀʀʏ ᴅᴜᴅᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴍʏ ᴄʜᴀɴɴᴇʟ 😔. 𝙿𝙻𝙴𝙰𝚂𝙴 ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ 🙏 **"
    try:
        user = await client.get_chat_member(client.force_channel, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



