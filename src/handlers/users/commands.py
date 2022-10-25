from aiogram import types
from aiogram.types import ReplyKeyboardRemove, InputFile, InputMediaPhoto

from keyboards import commands_default_keyboard, commands_small_keyboard, navigation_items_callback, \
    get_item_inline_keyboard
from loader import dp
from loader import db, bot


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


@dp.message_handler(text=['Список товаров','item','Овощи'])
@dp.message_handler(commands=['item'])
async def answer_menu_command(message: types.Message):
    first_item_info = db.select_items_info(id=1)
    first_item_info = first_item_info[0]
    _, name, count, photo_path = first_item_info
    item_text = f"Название товара: {name}" \
                f"\nКол-во товара: {count}"
    photo = InputFile(path_or_bytesio=photo_path)
    await message.answer_photo(photo=photo,
                               caption=item_text,
                               reply_markup=get_item_inline_keyboard())


@dp.callback_query_handler(navigation_items_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_items_info(id=current_item_id)
    first_item_info = first_item_info[0]
    _, name, count, photo_path = first_item_info
    item_text = f'Название товара: {name}' \
                f'\nКол-во товара: {count}'
    photo = InputFile(path_or_bytesio=photo_path)
    await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                       caption=item_text),
                                 chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 reply_markup=get_item_inline_keyboard(id=current_item_id))





# @dp.message_handler()
# async def answer_start_command(message: types.Message):
#     await message.answer(text=f'неизвестная команда',
#                          reply_markup=commands_default_keyboard)
