from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


b1 = KeyboardButton('Расположение')
b2 = KeyboardButton('Услуги')
b3 = KeyboardButton('Прайс')
b4 = KeyboardButton('Перманентный Макияж')
b5 = KeyboardButton('Лазер')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
                                # resize для того чтобы кнопки не были большими

kb_client.add(b1, b2, b3, b4, b5)

