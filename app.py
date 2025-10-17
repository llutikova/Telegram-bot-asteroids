import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, FSInputFile, Message, InputFile
from aiogram.types import FSInputFile

API_TOKEN = "7987423461:AAESxawtQK8pksuQSKEsDXvkh59f5HGski4"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='опасные астероиды'),
            types.KeyboardButton(text='гистограмма'),
            types.KeyboardButton(text='визуализация'),
            types.KeyboardButton(text='топ-10 самых крупных астероидов')
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="выберите команду"
    )
    await message.answer("Здравствуйте! Я - визуализатор опасных астероидов.", reply_markup=keyboard)


@dp.message(F.text.lower() == "опасные астероиды")
async def get_qr_function(message: Message):
    chat_id = message.chat.id
    photo = "static/hazardous.png"
    await bot.send_photo(chat_id=chat_id, photo=FSInputFile(path=photo))


@dp.message(F.text.lower() == "гистограмма")
async def get_qr_function(message: Message):
    chat_id = message.chat.id
    photo = "static/histogram.png"
    await bot.send_photo(chat_id=chat_id, photo=FSInputFile(path=photo))


@dp.message(F.text.lower() == "визуализация")
async def get_qr_function(message: Message):
    chat_id = message.chat.id
    photo = "static/graph.png"
    await bot.send_photo(chat_id=chat_id, photo=FSInputFile(path=photo))


@dp.message(F.text.lower() == "топ-10 самых крупных астероидов")
async def get_qr_function(message: Message):
    chat_id = message.chat.id
    photo = 'static/table.png'
    await bot.send_photo(chat_id=chat_id, photo=FSInputFile(path=photo))

if __name__ == "__main__":
    asyncio.run(main())

