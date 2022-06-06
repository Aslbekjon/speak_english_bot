import logging


from googletrans import Translator
from word_id import getDefination
from aiogram import Bot, Dispatcher, executor, types

translator = Translator()

API_TOKEN = '5384599272:AAGCl4Hg_rREWxspeXhpuXoWKbIoEFN530s'

logging.basicConfig(level=logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.botCommand("start", "Botni ishga tushirish"),
            types.botCommand("help", "Yordam"),
        ]
    )

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = types.User.get_current()
    await message.reply(f"{user.first_name} english speak botimizga xush kelibsiz")

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    user = types.User.get_current()
    await message.reply(f"so'z yoki gap junating")


@dp.message_handler()
async def translate(message: types.Message):    
    ln = len((message.text).split())
    user = types.User.get_current()
    lang = translator.detect(message.text).lang
    if ln>1:  
        dest = 'uz' if lang=='en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text
    
        lookup = getDefination(word_id)
        if lookup:
            await message.reply(f"word: {word_id} \n Definations: \n{lookup['definations']}")
            if lookup.get('audioFile'):
                await message.answer_audio(lookup['audioFile'])
        else:
            await message.reply("Bunday so'z topilmadi")
    print(user.first_name,"---", message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)