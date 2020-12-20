# This Python file uses the following encoding: utf-8

import telebot
from telebot import types


bot = telebot.TeleBot("1284427462:AAHPyWAvdRGT104ol7fCp4PXELJmAi55EwU", parse_mode="Markdown")

#region variables

#region keyboards
main_menu_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
main_menu_keyboard.add('Unity', 'Blender', 'РУПД', 'Загрузка документов')

download_menu_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
download_menu_keyboard.add('РУПД', 'Назад')

rupd_menu_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_keyboard.add('Пояснительная записка', 'Результаты освоения дисциплины',
                       'Содержание учебного предмета', 'Тематическое планирование с указанием количества часов',
                       'Оценка индивидуального проекта', 'Учебно-методическое обеспечение дисциплины', 'Назад')

rupd_menu_block2_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block2_keyboard.add('Метапредметные результаты', 'Предметные результаты', 'Назад', 'В главное меню')

rupd_menu_block2_block1_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block2_block1_keyboard.add('Регулятивные универсальные учебные действия',
                                     'Познавательные универсальные учебные действия',
                                     'Коммуникативные универсальные учебные действия', 'Назад', 'В главное меню')

rupd_menu_block2_block2_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block2_block2_keyboard.add('Обучаемый получит представление', 'Обучаемый сможет',
                                     'Обучаемый научится', 'Назад', 'В главное меню')

rupd_menu_block3_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block3_keyboard.add('Часть 1. Основы проектной деятельности',
                              'Часть 2. Выполнение обучаемым индивидуального проекта', 'Назад', 'В главное меню')

rupd_menu_block3_block1_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block3_block1_keyboard.add('Тема 1. Введение в проектную культуру', 'Тема 2. Инициализация проекта',
                                     'Тема 3. Базовое проектирование и исследование',
                                     'Тема 4. Информационные ресурсы проектной и исследовательской деятельности',
                                     'Тема 5. Презентация результатов проектной деятельности',
                                     'Тема 6. Защита результатов проектной и исследовательской деятельности',
                                     'Тема 7. Коммуникативные навыки',
                                     'Тема 8. Рефлексия проекта. Индивидуальный прогресс', 'Назад', 'В главное меню')

rupd_menu_block5_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block5_keyboard.add('Оценка метапредметных результатов обучения по уровню '
                              'сформированности Универсальных Учебных Действий (УУД)',
                              'Оценка сформированности ключевых компетенций учащихся, '
                              'которые относятся к общему (метапредметному) содержанию образования',
                              'Оценка сформированности ключевых компетенций учащихся «4к»', 'Назад', 'В главное меню')

rupd_menu_block5_block1_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block5_block1_keyboard.add('Требования, устанавленные ФГОС к результатам образования '
                                     '(ФГОС ООО, п.II.8, ФГОС СОО, п.II.6)',
                                     'Метапредметные результаты включают освоенные обучающимися',
                                     'Основные особенности оценки личностных, метапредметных и предметных '
                                     'результатов обучения',
                                     'Особенности индивидуального проекта',
                                     'Материалы, которые должны быть представлены к защите итогового проекта',
                                     'Организация защиты проекта',
                                     'Процедура оценивания сформированности УУД при защите реализованного проекта',
                                     'Критерии оценивания итогового проекта',
                                     'Подходы к оцениванию результатов итогового процесса',
                                     'Уровни сформированности навыков проектной деятельности (интегральный подход)',
                                     'Назад', 'В главное меню')

rupd_menu_block5_block2_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block5_block2_keyboard.add('Компетентность отличается', 'Три уровня компетенций', 'Ключевые компетенции',
                                     'Уровни компетенций и способы деятельности учащихся', 'Назад', 'В главное меню')

rupd_menu_block5_block3_keyboard = types.ReplyKeyboardMarkup(True, row_width=1)
rupd_menu_block5_block3_keyboard.add('К 2020 году каждый востребованный сотрудник должен будет уметь',
                                     'Система “4К”', 'Подробнее о каждом из четырех «К»',
                                     'Оценка прогресса в критическом мышлении, креативности, коммуникации и кооперации',
                                     'Назад', 'В главное меню')
#endregion

#region block_messages
main_menu_message = "Содержание:\n" \
                    "1. Unity\n" \
                    "2. Blender\n" \
                    "3. РУПД\n" \
                    "4. Загрузка документов"
download_menu_message = "Содержание:\n" \
                        "1. РУПД"
rupd_main_menu_message = "Содержание:\n" \
                         "1. Пояснительная записка\n" \
                         "2. Результаты освоения дисциплины\n" \
                         "3. Содержание учебного предмета\n" \
                         "4. Тематическое планирование с указанием количества часов\n" \
                         "5. Оценка индивидуального проекта\n" \
                         "6. Учебно-методическое обеспечение дисциплины"
rupd_menu_block2_message = "Содержание:\n" \
                           "1. Метапредметные результаты\n" \
                           "2. Предметные результаты"
rupd_menu_block2_block1_message = "Содержание:\n" \
                                  "1. Регулятивные универсальные учебные действия\n" \
                                  "2. Познавательные универсальные учебные действия\n" \
                                  "3. Коммуникативные универсальные учебные действия"
rupd_menu_block2_block2_message = "Содержание:\n" \
                                  "1. Обучаемый получит представление\n" \
                                  "2. Обучаемый сможет\n" \
                                  "3. Обучаемый научится"
rupd_menu_block3_message = "Содержание:\n" \
                           "1. Часть 1. Основы проектной деятельности\n" \
                           "2. Часть 2. Выполнение обучаемым индивидуального проекта с применением " \
                           "AR-технологии-проекта «оживление учебника» в виде простого AR-приложения " \
                           "для Android-устройства с помощью ПО Blender, Unity3D и Vuforia"
rupd_menu_block3_block1_message = "Содержание:\n" \
                                  "1. Введение в проектную культуру\n" \
                                  "2. Инициализация проекта\n" \
                                  "3. Базовое проектирование и исследование\n" \
                                  "4. Информационные ресурсы проектной и исследовательской деятельности\n" \
                                  "5. Презентация результатов проектной деятельности\n" \
                                  "6. Защита результатов проектной и исследовательской деятельности\n" \
                                  "7. Коммуникативные навыки\n" \
                                  "8. Рефлексия проекта. Индивидуальный прогресс"
rupd_menu_block5_message = "Содержание:\n" \
                           "1. Оценка метапредметных результатов обучения по уровню сформированности Универсальных Учебных Действий (УУД)\n" \
                           "2. Оценка сформированности ключевых компетенций учащихся, которые относятся к общему (метапредметному) содержанию образования\n" \
                           "3. Оценка сформированности ключевых компетенций учащихся «4к»"
rupd_menu_block5_block1_message = "Содержание:\n" \
                                  "1. Требования, устанавленные ФГОС к результатам образования " \
                                  "(ФГОС ООО, п.II.8, ФГОС СОО, п.II.6)\n" \
                                  "2. Метапредметные результаты включают освоенные обучающимися\n" \
                                  "3. Основные особенности оценки личностных, метапредметных и предметных " \
                                  "результатов обучения\n" \
                                  "4. Особенности индивидуального проекта\n" \
                                  "5. Материалы, которые должны быть представлены к защите итогового проекта\n" \
                                  "6. Организация защиты проекта\n" \
                                  "7. Процедура оценивания сформированности УУД при защите реализованного проекта\n" \
                                  "8. Критерии оценивания итогового проекта\n" \
                                  "9. Подходы к оцениванию результатов итогового процесса\n" \
                                  "10. Уровни сформированности навыков проектной деятельности (интегральный подход)"
rupd_menu_block5_block2_message = "Содержание:\n" \
                                  "1. Компетентность отличается\n" \
                                  "2. Три уровня компетенций\n" \
                                  "3. Ключевые компетенции\n" \
                                  "4. Уровни компетенций и способы деятельности учащихся"
rupd_menu_block5_block3_message = "Содержание:\n" \
                                  "1. К 2020 году каждый востребованный сотрудник должен будет уметь\n" \
                                  "2. Система “4К”\n" \
                                  "3. Подробнее о каждом из четырех «К»\n" \
                                  "4. Оценка прогресса в критическом мышлении, креативности, коммуникации и кооперации"
rupd_menu_block6_message = "[1.Индивидуальный проект. 10-11 классы: учебное пособие для общеобразовательных " \
                           "организаций / М. В. Половкова, А. В. Носов, Т. В. Половкова, М. В. Майсак. - " \
                           "Москва: Просвещение, 2019. - 159 с.](https://www.labirint.ru/books/649611/) \n\n" \
                           "[2.Индивидуальный проект: рабочая тетрадь. 10-11 классы. Учебное пособие/Л.Е.Спиридонова," \
                           " Б.А. Комаров,О.В.Маркова,В.М.Стацунова. – СПб.КАРО, 2019. – 104с.]" \
                           "(https://cutt.ly/bgnU3d7)\n\n" \
                           "[3.Компетентностный подход в обучении: учебно-методическое пособие / авт.-сост." \
                           " О.В. Еремкина, Н.Б. Федорова, Д.В. Морин, М.А. Борисова; Ряз. гос. ун-т им. " \
                           "С.А. Есенина. – Рязань, 2010 – 48 с.]" \
                           "(https://www.rsu.edu.ru/wp-content/uploads/2015/11/Kompetentnostny-podhod-v-obuchenii.pdf)\n\n" \
                           "[4. Компетенции “4К”: формирование и оценка на уроке: Практические рекомендации" \
                           "/ авт.-сост. М. А. Пинская, А. М. Михайлова. – 76с.]" \
                           "(https://publications.hse.ru/mirror/pubs/share/direct/345295660.pdf)\n\n" \
                           "[5.Проектная и исследовательская деятельность школьников в контексте требований ФГОС" \
                           "/Материалы Л.И.Асановой, к.п.н., доцента ГБОУ ДПО " \
                           "«Нижегородский институт развития образования».]" \
                           "(https://rosuchebnik.ru/upload/iblock/733/733b6b3d76aab4abae1ff92989545fbf.pdf)"
#endregion

#endregion


def inline_keyboard_builder_and_image_path(call_data, max):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    next_button = types.InlineKeyboardButton(text="Далее",
                                             callback_data=f"{call_data[0]} {call_data[1]} {call_data[2]} {call_data[3]} {int(call_data[4]) + 1} {max}")
    prv_button = types.InlineKeyboardButton(text="Назад",
                                             callback_data=f"{call_data[0]} {call_data[1]} {call_data[2]} {call_data[3]} {int(call_data[4]) - 1} {max}")
    if int(call_data[4]) != 1:
        keyboard.add(prv_button)
    if int(call_data[4]) != max and int(call_data[4]) != max + 1:
        keyboard.add(next_button)
    return keyboard, f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        call_data = call.data.split(' ')
        max = int(call_data[5])
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{call_data[4]}.JPG".replace("/block0", "")
        try:
            bot.edit_message_media(message_id=call.message.message_id,
                               chat_id=call.message.chat.id,
                               media=types.InputMedia(type="photo", media=open(image_path, "rb")),
                               reply_markup=inline_keyboard_builder_and_image_path(call_data, max)[0])
        except FileNotFoundError:
            return

@bot.message_handler(commands=['start'])
def start_handler(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/menu")
    bot.send_message(message.from_user.id, "Привет! Это бот-помощник по дисциплине Индивидуальный проект. Команда /menu поможет начать", reply_markup=keyboard)


@bot.message_handler(commands=['menu'])
def main_menu_handler(message):
    send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
    bot.register_next_step_handler(send, menu_handler)

@bot.message_handler(content_types=['text'])
def menu_handler(message):
    if message.text == 'РУПД':
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == 'Unity':
        bot.send_message(message.from_user.id, text="В разработке")
    if message.text == 'Blender':
        bot.send_message(message.from_user.id, text="В разработке")
    if message.text == 'Загрузка документов':
        send = bot.send_message(message.from_user.id, text=download_menu_message, reply_markup=download_menu_keyboard)
        bot.register_next_step_handler(send, download_handler)


@bot.message_handler(content_types=['text'])
def download_handler(message):
    if message.text == 'РУПД':
        send = bot.send_document(message.from_user.id, open('RUPD_Individualny_proekt.docx', 'rb'))
        bot.register_next_step_handler(send, download_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_main_menu_handler(message):
    if message.text == "Пояснительная записка":
        callback_data = "rupdImages block1 block0 block0 2 5"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "Результаты освоения дисциплины":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)
    if message.text == "Содержание учебного предмета":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_message, reply_markup=rupd_menu_block3_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_handler)
    if message.text == "Тематическое планирование с указанием количества часов":
        callback_data = "rupdImages block4 block0 block0 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "Оценка индивидуального проекта":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message, reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "Учебно-методическое обеспечение дисциплины":
        callback_data = "rupdImages block6 block0 block0 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard, caption=rupd_menu_block6_message)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)

@bot.message_handler(content_types="text")
def rupd_menu_block2_handler(message):
    if message.text == "Метапредметные результаты":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_block1_message, reply_markup=rupd_menu_block2_block1_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block1_handler)
    if message.text == "Предметные результаты":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_block2_message, reply_markup=rupd_menu_block2_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block2_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=["text"])
def rupd_menu_block2_block1_handler(message):
    if message.text == "Регулятивные универсальные учебные действия":
        callback_data = "rupdImages block2 block1 block1 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block1_handler)
    if message.text == "Познавательные универсальные учебные действия":
        callback_data = "rupdImages block2 block1 block2 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block1_handler)
    if message.text == "Коммуникативные универсальные учебные действия":
        callback_data = "rupdImages block2 block1 block3 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=["text"])
def rupd_menu_block2_block2_handler(message):
    if message.text == "Обучаемый получит представление":
        callback_data = "rupdImages block2 block2 block1 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block2_handler)
    if message.text == "Обучаемый сможет":
        callback_data = "rupdImages block2 block2 block2 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block2_handler)
    if message.text == "Обучаемый научится":
        callback_data = "rupdImages block2 block2 block3 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block2_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types="text")
def rupd_menu_block3_handler(message):
    if message.text == "Часть 1. Основы проектной деятельности":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_block1_message, reply_markup=rupd_menu_block3_block1_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Часть 2. Выполнение обучаемым индивидуального проекта":
        callback_data = "rupdImages block3 block2 block0 2 3"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block3_block1_handler(message):
    if message.text == "Тема 1. Введение в проектную культуру":
        callback_data = "rupdImages block3 block1 block1 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 2. Инициализация проекта":
        callback_data = "rupdImages block3 block1 block2 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 3. Базовое проектирование и исследование":
        callback_data = "rupdImages block3 block1 block3 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 4. Информационные ресурсы проектной и исследовательской деятельности":
        callback_data = "rupdImages block3 block1 block4 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 5. Презентация результатов проектной деятельности":
        callback_data = "rupdImages block3 block1 block5 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 6. Защита результатов проектной и исследовательской деятельности":
        callback_data = "rupdImages block3 block1 block6 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 7. Коммуникативные навыки":
        callback_data = "rupdImages block3 block1 block7 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 8. Рефлексия проекта. Индивидуальный прогресс":
        callback_data = "rupdImages block3 block1 block8 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_message, reply_markup=rupd_menu_block3_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_handler(message):
    if message.text == "Оценка метапредметных результатов обучения по уровню сформированности Универсальных Учебных Действий (УУД)":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_block1_message, reply_markup=rupd_menu_block5_block1_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Оценка сформированности ключевых компетенций учащихся, которые относятся к общему (метапредметному) содержанию образования":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_block2_message, reply_markup=rupd_menu_block5_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Оценка сформированности ключевых компетенций учащихся «4к»":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_block3_message, reply_markup=rupd_menu_block5_block3_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block1_handler(message):
    if message.text == "Требования, устанавленные ФГОС к результатам образования (ФГОС ООО, п.II.8, ФГОС СОО, п.II.6)":
        callback_data = "rupdImages block5 block1 block1 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Метапредметные результаты включают освоенные обучающимися":
        callback_data = "rupdImages block5 block1 block2 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Основные особенности оценки личностных, метапредметных и предметных результатов обучения":
        callback_data = "rupdImages block5 block1 block3 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Особенности индивидуального проекта":
        callback_data = "rupdImages block5 block1 block4 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Материалы, которые должны быть представлены к защите итогового проекта":
        callback_data = "rupdImages block5 block1 block5 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Организация защиты проекта":
        callback_data = "rupdImages block5 block1 block6 2 3"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Процедура оценивания сформированности УУД при защите реализованного проекта":
        callback_data = "rupdImages block5 block1 block7 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Критерии оценивания итогового проекта":
        callback_data = "rupdImages block5 block1 block8 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Подходы к оцениванию результатов итогового процесса":
        callback_data = "rupdImages block5 block1 block9 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Уровни сформированности навыков проектной деятельности (интегральный подход)":
        callback_data = "rupdImages block5 block1 block10 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message,
                                reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block2_handler(message):
    if message.text == "Компетентность отличается":
        callback_data = "rupdImages block5 block2 block1 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Три уровня компетенций":
        callback_data = "rupdImages block5 block2 block2 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Ключевые компетенции":
        callback_data = "rupdImages block5 block2 block3 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Уровни компетенций и способы деятельности учащихся":
        callback_data = "rupdImages block5 block2 block4 2 3"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message,
                                reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block3_handler(message):
    if message.text == "К 2020 году каждый востребованный сотрудник должен будет уметь":
        callback_data = "rupdImages block5 block3 block1 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Система “4К”":
        callback_data = "rupdImages block5 block3 block2 2 1"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Подробнее о каждом из четырех «К»":
        callback_data = "rupdImages block5 block3 block3 2 2"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Оценка прогресса в критическом мышлении, креативности, коммуникации и кооперации":
        callback_data = "rupdImages block5 block3 block4 2 3"
        call_data = callback_data.split(' ')
        image_path = f"{call_data[0]}/{call_data[1]}/{call_data[2]}/{call_data[3]}/{int(call_data[4]) - 1}.JPG".replace(
            "/block0", "")
        keyboard = types.InlineKeyboardMarkup()
        if int(call_data[4]) <= int(call_data[5]):
            keyboard.add(types.InlineKeyboardButton(text="Далее", callback_data=callback_data))
        send = bot.send_photo(message.from_user.id, photo=open(image_path, "rb"), reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message,
                                reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "В главное меню":
        send = bot.send_message(message.from_user.id, text=main_menu_message, reply_markup=main_menu_keyboard)
        bot.register_next_step_handler(send, menu_handler)


bot.polling(none_stop=True, interval=0)
