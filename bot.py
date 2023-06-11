from imaplib import Commands
from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(token =  config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
     await message.answer("Hi")

@dp.message_handler(commands='help')
async def start(message: types.Message):
     await message.answer("Вот наши команды:")

@dp.message_handler(content_types=['text'], text = "Привет")
async def hello(message: types.Message):
      await message.answer("Привет!")


@dp.message_handler(content_types=['text'], text = "Как дела?")
async def how_are_you(message: types.Message):
      await message.answer("Хорошо, как сам?")

if __name__== "__main__":
    executor.start_polling(dp)