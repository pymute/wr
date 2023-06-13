from aiogram.utils import executor
import logging
import random
from aiogram import types
logging.basicConfig(level=logging.INFO)



from aiogram import Bot,Dispatcher
bot = Bot(token='5600436666:AAE7oRd8rR_VOqsPtA6IIf1739GdNefE6ZE')
dp = Dispatcher(bot)


aralash = ['mampar','osh','mastava','moshhorda','pegodi','gamburger','kaklet','tovuq','qovurma']
quyuq = ['xonim','manti','somsa','makaron','tuxum','uy lavash','uy pitsa','norin']
suyuq = ['mastava',"lag'mon",'uxa shorva','qaynatma',"moxora","chuchvara"]

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Dushanba')
    button2 = types.KeyboardButton('Seshanba')
    button3 = types.KeyboardButton('Chorshanba')
    button4 = types.KeyboardButton('Payshanba')
    button5 = types.KeyboardButton('Juma')
    button6 = types.KeyboardButton('Shanba')
    button7 = types.KeyboardButton('Yakshanba')
    keyboard.add(button1, button2, button3, button7, button6, button5, button4)

    # Send a message with the keyboard
    await message.answer('bugun qaysi kun?', reply_markup=keyboard)

# Define a message handler for button 1
@dp.message_handler(lambda message: message.text == 'Dushanba')
async def button1_handler(message: types.Message):
    await message.answer(random.choice(quyuq))
# Define a message handler for button 2
@dp.message_handler(lambda message: message.text == 'Seshanba')
async def button2_handler(message: types.Message):
    await message.answer(random.choice(quyuq))
@dp.message_handler(lambda message: message.text == 'Chorshanba')
async def button3_handler(message: types.Message):
    await message.answer(random.choice(quyuq))
@dp.message_handler(lambda message: message.text == 'Yakshanba')
async def button4_handler(message: types.Message):
    await message.answer(random.choice(aralash))
@dp.message_handler(lambda message: message.text == 'Shanba')
async def button5_handler(message: types.Message):
    await message.answer(random.choice(aralash))
@dp.message_handler(lambda message: message.text == 'Juma')
async def button6_handler(message: types.Message):
    await message.answer(random.choice(suyuq))
@dp.message_handler(lambda message: message.text == 'Payshanba')
async def button7_handler(message: types.Message):
    await message.answer(random.choice(aralash))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
