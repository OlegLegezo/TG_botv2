from aiogram import types

from loader import dp


@dp.message_handler(text=['оНас'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'бот-магазин')


@dp.message_handler(text=['контакты'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'телефон: 123-22-22')


@dp.message_handler(text=['графикДоставки'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'ежедневно с 18 до 20')

@dp.message_handler()
async def answer_start_command(message: types.Message):
    await message.answer(text=f'неизвестная команда')
