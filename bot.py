from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards import kb_client
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

foto = open('upgrade.jpg', 'rb')
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, foto)
    await bot.send_message(message.from_user.id,  '<b>Здравствуйте!</b> \nВас приветствует команда UP GRADE! <i>Можем чем-то помочь?</i>', reply_markup=kb_client, parse_mode='HTML')



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Мы можем чем-то помочь?")


@dp.message_handler(lambda message: 'Расположение' in message.text.title())
async def place(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы находимся по адрессу:\n'
                                                 ' г. Волковыск ул. Панковой 47б 2-ой этаж')


@dp.message_handler(lambda message: 'Услуги' in message.text.title())
async def services(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы оказываем услуги:\n'
                                                 '-лазерного удаления волос\n'
                                                 '-лазерного удаления некачественного ПМ\n'
                                                 '-карбонового пилинга\n'
                                                 '-лазерного удаления тату\n'
                                                 '-макияжа\n'
                                                 '-коррекция и окрашивание хной/краской\n'
                                                 '-обучению окрашиванию бровей краской/хной\n'
                                                 ' -обучению перманентному макияжу')

ikb_price = InlineKeyboardMarkup(row_width=1)
ikb_PM = InlineKeyboardButton(text='Прайс на ПМ', callback_data='price_permanent')
ikb_laser = InlineKeyboardButton(text='Прайс на лазер', callback_data='price_laser')
ikb_brow = InlineKeyboardButton(text='Прайс на окрашивание хной/краской', callback_data='brow')
ikb_price.add(ikb_PM, ikb_laser, ikb_brow)


@dp.message_handler(lambda message: 'Прайс' in message.text.title())
async def price(message: types.Message):
    await bot.send_message(message.from_user.id, text='Выберите услугу:', reply_markup=ikb_price)


ikb_choice_master = InlineKeyboardMarkup(row_width=2)
ikb_Margo_price = InlineKeyboardButton(text='мастер\n Маргарита', callback_data='pm_margo')
ikb_Nata_price = InlineKeyboardButton(text='мастер\n Наталья', callback_data='pm_nata')
ikb_back_price = InlineKeyboardButton(text='назад', callback_data='Прайс')
ikb_choice_master.add(ikb_Nata_price, ikb_Margo_price)
ikb_choice_master.row(ikb_back_price)


@dp.callback_query_handler(text='Прайс')
async def back_choice_master(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, text='Выберите услугу:', reply_markup=ikb_price)


@dp.callback_query_handler(text='pm_margo')
async def price_margo(call: types.CallbackQuery):
    await call.message.answer('Стоимость перманентного макияжа с коррекцией 230BYN')
    await call.answer()


@dp.callback_query_handler(text='pm_nata')
async def price_nata(call: types.CallbackQuery):
    await call.message.answer('Стоимость перманентного макияжа с коррекцией 240BYN')
    await call.answer()


@dp.callback_query_handler(text='price_permanent')
async def choice_master(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, text='Выберете мастера:', reply_markup=ikb_choice_master)
    await call.answer()


@dp.callback_query_handler(text='brow')
async def price_brow(call: types.CallbackQuery):
    await call.message.answer('Стоимость услуги 20BYN В неё входит:\n'
                              '-Моделирование формы бровей пинцетом\n'
                              '-Окрашивание хной/краской\n'
                              '-Тридинг')
    await call.answer()


laser_choice = InlineKeyboardMarkup(row_width=2)
laser_man = InlineKeyboardButton(text='Мужской прайс', callback_data='laser_man')
laser_women = InlineKeyboardButton(text='Женский прайс', callback_data='laser_women')
laser_choice.add(laser_man, laser_women)


@dp.callback_query_handler(text='price_laser')
async def price_laser(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, text='Какой прайс интересует?', reply_markup=laser_choice)


photo_2 = open('photo_2.jpg', 'rb')
@dp.callback_query_handler(text='laser_man')
async def price_laser_man(call: types.CallbackQuery):
    await bot.send_photo(call.from_user.id, photo_2)
    await call.answer()


photo_3 = open('photo_3.jpg', 'rb')
@dp.callback_query_handler(text='laser_women')
async def price_laser_women(call: types.CallbackQuery):
    await bot.send_photo(call.from_user.id, photo_3)



ikb_PM1 = InlineKeyboardMarkup(row_width=1)
ikb_about_pm = InlineKeyboardButton(text='Что такое ПМ?', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B5%D0%BD%D1%82%D0%BD%D1%8B%D0%B9_%D0%BC%D0%B0%D0%BA%D0%B8%D1%8F%D0%B6')
ikb_care = InlineKeyboardButton(text='Уход за ПМ', callback_data='уход')
ikb_cont = InlineKeyboardButton(text='Противопоказания к  ПМ', callback_data='противопоказания')
ikb_preparation = InlineKeyboardButton(text='Подготовка к процедуре ПМ', callback_data='подготовка')

ikb_PM1.add(ikb_about_pm, ikb_care, ikb_cont, ikb_preparation)


@dp.message_handler(lambda message: 'Перманентный' in message.text.title())
async def pm(message: types.Message):
    await bot.send_message(message.from_user.id, text='Выберете, что вас интересует:', reply_markup=ikb_PM1)


@dp.callback_query_handler(text='уход')
async def care(call: types.CallbackQuery):
    await call.message.answer('УХОД ЗА ПЕРМАНЕНТНЫМ МАКИЯЖЕМ:\n'
                              'В течение 2-7 дней после процедуры перманентного макияжа (процесс первичного заживления, отхождение корочек), необходимо придерживаться некоторых правил по уходу за кожей. На самом деле, еще до процедуры татуажа следует задуматься, что после, придется некоторое время соблюдать ряд ограничений и быть к ним подготовленной.\n'
                              'Общими (для всех зон) рекомендациями по уходу после татуажа являются:\n'
                              '-Не отрывать корочки, не чесать зону татуажа.\n'
                              '-Не поддавать зону татуажа распариванию и сильному намоканию: не посещать сауну, солярий и бассейн. При умывании использовать ватные диски, сильно не мочить.\n'
                              '-Ограничить использование декоративной косметики, кремов, категорически воздержаться от пилингов.\n'
                              '-Для ухода после татуажа рекомендуется использовать мази с противовоспалительным и ранозаживляющим эффектом. При этом категорически противопоказано применение мазей: содержащих антибиотики, гормоны и прочие стимуляторы заживления, так как они влияют на качество имплантации красящего мигмента в кожу.\n'
                              '-В постпроцедурный уход после татуажа входить промывание поверхности татуажа утром и вечером - хлоргексидином.\n'
                              '-Идеальным способом ухода после процедуры татуажа является применение ухаживающего крема, обогащенного витаминами А и D\n'
                              '-После заживления, посещение солярия возможно не раньше чем через 2 недели с применением солнцезащитных средств, т.к. пигмент постепенно выцветает от ультрафиолетовых лучей.\n'
                              '-Коррекцию можно проводить не ранее через 3-4 недели после первой процедуры.\n'
                              '-В течение всего периода заживления исключить: лекарственные препараты на основе антибиотиков, в том числе медикаменты - разжижающие кровь (аспирин, анальгин и т.д.), косметические кремы и гели в области перманента (посоветоваться с врачом)\n'
                              '-Использовать минимальное количество жирных кремов\n'
                              )

    await call.answer()


@dp.callback_query_handler(text='противопоказания')
async def cont(call: types.CallbackQuery):
    await call.message.answer('Противопоказания к процедуре перманентного макияжа:\n'
                              'Абсолютные противопоказания к процедуре ПМ:\n'
                              '* Инсулинозависимая форма сахарного диабета\n'
                              '* Болезни, связанные со значительным снижением свертываемости крови\n'
                              '* Тяжелые соматические заболевания\n'
                              '* Острые воспалительные заболевания\n'
                              '* Психические расстройства\n'
                              '* Эпилепсия\n'
                              '* Гепатит, ВИЧ, СПИД\n\n'
                              'Относительные противопоказания к процедуре:\n'
                              '* Беременность\n'
                              '* Период лактации\n'
                              '* Родинки, бородавки, папилломы в зоне татуажа\n'
                              '* Дерматиты\n'
                              '* Герпес, заеды\n'
                              '* Бронхиальная астма\n'
                              '* Келоидные рубцы\n'
                              '* Период менструального цикла\n'
                              '* Перенесенные операции менее 7 месяцев назад\n'
                              '* Ожоги ( менее 1 года)')
    await call.answer()


@dp.callback_query_handler(text='подготовка')
async def preparation(call: types.CallbackQuery):
    await call.message.answer('ПОДГОТОВКА К ПРОЦЕДУРЕ ПЕРМАНЕНТНОГО МАКИЯЖА\n\n'
                              '* В течение двух недель до и после процедуры нельзя принимать антибиотики, иначе организм не будет позволять пигменту приживаться.\n'
                              '* За день-два до процедуры не желательно употребление спиртных напитков. А в день процедуры лучше не пить кофе. Часто возникает вопрос: «Почему?». Дело в том, что алкоголь и кофе разжижают кровь, что может приводить к выделению сукровицы при проведении процедуры перманентного макияжа. Это, в свою очередь, осложняет работу мастера.\n'
                              '* Так же не желательно посещение за день до процедуры солярия, дабы кожа не грубела и была восприимчива к пигменту\n'
                              'Брови. Перед процедурой не стоит выщипывать, обрезать или сбривать волосы на бровях. Мастеру необходимо видеть линию роста волос, наполняемость брови волосками и их цвет.\n\n'
                              'Губы. Перед тем, как делать перманентный макияж губ, рекомендуется пропить препарат «Гевиран», «Валацикловир» либо «Валтрекс». Начинать приём препарата необходимо в день процедуры (далее принимать по аннотации). В данном случае таблетки – это профилактика герпеса, поэтому приём препарата не будет лишним.\n\n'
                              'Веки. Перед процедурой перманентного макияжа век не нужно никакой специальной подготовки. Но есть один нюанс: не всем рекомендуется данная процедура. Если на веках тонкая кожа с обилием ярко выраженных сосудов, процедуру лучше не делать. В противном случае результат может быть не таким, как хотелось бы клиенту: сосуд, например, может лопнуть, и краска «поплывёт». Если вы ухаживаете за кожей век специальными кремами, которые делают кожу более «крепкой», завершите уход за день до посещения студии, чтобы позволить веку «принять» пигмент.\n\n'
                              'И помните, что правильная подготовка к перманентному макияжу и качественный послепроцедурный уход – залог прекрасного внешнего вида!')


ikb_laser = InlineKeyboardMarkup(row_width=2)
ikb_piling = InlineKeyboardButton(text='Карбоновый пилинг', callback_data='пилинг')
ikb_laser_del = InlineKeyboardButton(text='Лазерное удаление волос', callback_data='удаление')
ikb_laser.add(ikb_laser_del, ikb_piling)


@dp.message_handler(lambda message: 'Лазер' in message.text.title())
async def laser(message: types.Message):
    await bot.send_message(message.from_user.id, text='Что Вас интересует?', reply_markup=ikb_laser)


@dp.callback_query_handler(text='пилинг')
async def piling(call: types.CallbackQuery):
    await call.message.answer('Карбоновый пилинг – это косметическая процедура омоложения и глубокого очищения кожи под воздействием лазера. Также известен под названием «углеродный пилинг» за счет использования специального наногеля на основе карбона (диоксида углерода).\n\n'
                              'Карбоновый пилинг уменьшает избыточную выработку кожного сала и снимает покраснения и воспаления, что важно при угрях и акне. Быстрый результат. Эффект от карбонового пилинга будет заметен уже после первой процедуры')
    await call.answer()


@dp.callback_query_handler(text='удаление')
async def laser_del(call: types.CallbackQuery):
    await call.message.answer('Лазерная эпиляция — процедура удаления волос с помощью воздействия импульсов лазерного излучения, разрушающие волосяной фолликул\n'
                              'Лазерная эпиляция проводится курсом, в который входит серия процедур с паузами между ними, чтобы уничтожить «проснувшиеся» волосяные луковицы. После курса в течение нескольких лет волосы не растут — это зависит от индивидуальных особенностей организма.')
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp)

