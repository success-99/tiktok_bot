from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from tiktok import tiktokdow

# from keyboards.default.vid_mus import button
from states.dowloand import Dow
@dp.message_handler(commands='boshla')
async def boshla(message:types.Message):
    await message.answer('TikTok havolasini tashlang')

# @dp.message_handler(Text(startswith="https"))
# async def send_link1(message:types.Message):
#
#     link1 = message.text
#     k = link1[17:]
#     data1 = youtubemp4(k)
#     if data1 != "bed":
#         await message.answer_video(data1)
#         # await message.answer_video(data1)
#     else:
#         await message.answer("Hechnarsa t 😔")

# @dp.message_handler()
# async def send_link1(message:types.Message):
#     audio=message.text
#     a3=text_to_speech(audio)
#     await message.answer_video(a3)

@dp.message_handler(Text(startswith="https://www.tiktok.com"))
async def send_link(message:types.Message):
    link = message.text
    data = tiktokdow(link)
    if data == "bed":
        await message.answer("Hechnarsa topilmadi 😔")
    else:
        await message.answer_video(data)


