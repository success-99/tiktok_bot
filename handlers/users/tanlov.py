from aiogram import types,Dispatcher,Bot,executor
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from tiktok import tiktokdow


@dp.message_handler(commands='boshla')
async def boshla(message:types.Message):
    await message.answer('TikTok havolasini tashlang')


@dp.message_handler(Text(startswith="https://",))
async def send_link(message:types.Message):
    link = message.text
    data = tiktokdow(link)
    if data == "bed":
        await message.answer("Hechnarsa topilmadi 😔")
    else:
        await message.delete()
        xabar =await bot.send_message(chat_id=message.chat.id,text="kuting")
        for i in range(1,11):
            text0= i*10
            text1=i*"▪️"
            text2=(10-i)*"▫️️"
            await xabar.edit_text(f"{text0}%\n{text1}{text2}")
        await xabar.delete()
        await message.answer_video(data)


