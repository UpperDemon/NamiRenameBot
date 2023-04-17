from pyrogram import Client, filters 
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ꜱᴇᴛ.__\n\nᴇxᴀᴍᴘʟᴇ:- `/set_caption {filename}\n\n💾 ꜱɪᴢᴇ: {filesize}\n\n⏰ ᴅᴜʀᴀᴛɪᴏɴ: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**✅ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ɪꜱ ꜱᴇᴛ ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ**__")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("__**😔 ʏᴏᴜʀ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴀ ᴄᴀᴘᴛɪᴏɴ**__")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("__**❌️ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ɪꜱ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ**__")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ:-**\n\n`{caption}`")
    else:
       await message.reply_text("__**😔 ʏᴏᴜʀ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴀɴʏ ᴄᴀᴘᴛɪᴏɴ**__")
