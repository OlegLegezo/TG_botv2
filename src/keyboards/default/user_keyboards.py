from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start')
        ],
        [
            KeyboardButton(text='оНас'),
            KeyboardButton(text='контакты'),
            KeyboardButton(text='графикДоставки')
        ],
        [
            KeyboardButton(text='Активация аккаунта',
                           request_contact=True),
            KeyboardButton(text='Поделиться местоположением',
                           request_location=True),
        ],
        [
            KeyboardButton(text='Скрыть меню')
        ],
        [
            KeyboardButton(text='Удалить аккаунт')
        ]
    ],
    resize_keyboard=True

)

commands_small_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню')
        ]
    ],
    resize_keyboard=True

)
