from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards import commands_default_keyboard, commands_small_keyboard
from loader import dp
from loader import db


@dp.message_handler(text=['привет', 'хай'])
@dp.message_handler(commands=['start'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'и снова здравствуйте'
                              f'\nсписок команд:'
                              f'\nоНас'
                              f'\nконтакты'
                              f'\nграфикДоставки',
                         reply_markup=commands_default_keyboard)


@dp.message_handler(text=['Меню'])
@dp.message_handler(commands=['menu'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'главное меню',
                         reply_markup=commands_default_keyboard)


@dp.message_handler(text=['Скрыть меню'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'чтобы вернуть меню, воспользуйтесь командой /menu',
                         # reply_markup=ReplyKeyboardRemove())
                         reply_markup=commands_small_keyboard)


@dp.message_handler(content_types=['contact'])
async def answer_start_command(message: types.Message):
    print(message)
    if message.from_user.id == message.contact.user_id:
        await message.answer(text=f'Благодарим за активацию аккаунта',
                             reply_markup=commands_default_keyboard)
        db.add_user(int(message.from_user.id), str(message.contact.phone_number))
    else:
        await message.answer(text=f'Это чужой контакт',
                             reply_markup=commands_default_keyboard)

@dp.message_handler(text=['Удалить аккаунт'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Ваш аккаунт удален',
                         reply_markup=commands_default_keyboard)
    db.delete_user(id=message.from_user.id)


# @dp.message_handler()
# async def answer_start_command(message: types.Message):
#     await message.answer(text=f'неизвестная команда',
#                          reply_markup=commands_default_keyboard)
