# This Python file uses the following encoding: utf-8

import telebot
from telebot import types


bot = telebot.TeleBot("1284427462:AAHPyWAvdRGT104ol7fCp4PXELJmAi55EwU", parse_mode="Markdown")

#region variables

#region keyboards
main_menu_keyboard = types.ReplyKeyboardMarkup(row_width=1)
main_menu_keyboard.add('Unity', 'Blender', 'РУПД', 'Загрузка документов')

rupd_menu_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_keyboard.add('Пояснительная записка', 'Результаты освоения дисциплины',
                       'Содержание учебного предмета', 'Тематическое планирование с указанием количества часов',
                       'Оценка индивидуального проекта', 'Учебно-методическое обеспечение дисциплины', 'Назад')

rupd_menu_block2_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_block2_keyboard.add('Метапредметные результаты', 'Предметные результаты', 'Назад')

rupd_menu_block2_block1_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_block2_block1_keyboard.add('Регулятивные универсальные учебные действия',
                                     'Познавательные универсальные учебные действия',
                                     'Коммуникативные универсальные учебные действия', 'Назад')

rupd_menu_block2_block2_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_block2_block2_keyboard.add('Обучаемый получит представление', 'Обучаемый сможет',
                                     'Обучаемый научится', 'Назад')

rupd_menu_block3_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_block3_keyboard.add('Часть 1. Основы проектной деятельности',
                              'Часть 2. Выполнение обучаемым индивидуального проекта с применением '
                              'AR-технологии-проекта «оживление учебника» в виде простого AR-приложения для'
                              ' Android-устройства с помощью ПО Blender, Unity3D и Vuforia', 'Назад')

rupd_menu_block3_block1_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_block3_block1_keyboard.add('Тема 1. Введение в проектную культуру', 'Тема 2. Инициализация проекта',
                                     'Тема 3. Базовое проектирование и исследование',
                                     'Тема 4. Информационные ресурсы проектной и исследовательской деятельности',
                                     'Тема 5. Презентация результатов проектной деятельности',
                                     'Тема 6. Защита результатов проектной и исследовательской деятельности',
                                     'Тема 7. Коммуникативные навыки',
                                     'Тема 8. Рефлексия проекта. Индивидуальный прогресс', 'Назад')

rupd_menu_block5_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_block5_keyboard.add('Оценка метапредметных результатов обучения по уровню '
                              'сформированности Универсальных Учебных Действий (УУД)',
                              'Оценка сформированности ключевых компетенций учащихся, '
                              'которые относятся к общему (метапредметному) содержанию образования',
                              'Оценка сформированности ключевых компетенций учащихся «4к»', 'Назад')

rupd_menu_block5_block1_keyboard = types.ReplyKeyboardMarkup(row_width=1)
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
                                     'Назад')

rupd_menu_block5_block2_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_block5_block2_keyboard.add('Компетентность отличается', 'Три уровня компетенций', 'Ключевые компетенции',
                                     'Уровни компетенций и способы деятельности учащихся', 'Назад')

rupd_menu_block5_block3_keyboard = types.ReplyKeyboardMarkup(row_width=1)
rupd_menu_block5_block3_keyboard.add('К 2020 году каждый востребованный сотрудник должен будет уметь',
                                     'Система “4К”', 'Подробнее о каждом из четырех «К»',
                                     'Оценка прогресса в критическом мышлении, креативности, коммуникации и кооперации',
                                     'Назад')
#endregion

#region block_messages
main_menu_message = "Содержание\n" \
                    "1. Unity\n" \
                    "2. Blender\n" \
                    "3. РУПД\n" \
                    "4. Загрузка документов"
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
                           "1. \n" \
                           "2. \n" \
                           "3. "
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
                           "организаций / [М. В. Половкова, А. В. Носов, Т. В. Половкова, М. В. Майсак]. - " \
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

@bot.message_handler(commands=['start'])
def start_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data="m0"))
    bot.send_message(message.from_user.id, "Привет! Это бот-помощник по дисциплине Индивидуальный проект. Команда /menu поможет начать", reply_markup=keyboard)


@bot.message_handler(commands=['menu'])
def main_menu_handler(message):
    send = bot.send_message(message.from_user.id, main_menu_message, reply_markup=main_menu_keyboard)
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
        bot.send_message(message.from_user.id, text="В разработке")


@bot.message_handler(content_types=['text'])
def rupd_main_menu_handler(message):
    if message.text == "Пояснительная записка":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок 1", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "Результаты освоения дисциплины":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)
    if message.text == "Содержание учебного предмета":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_message, reply_markup=rupd_menu_block3_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_handler)
    if message.text == "Тематическое планирование с указанием количества часов":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок 4", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_handler)
    if message.text == "Оценка индивидуального проекта":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message, reply_markup=rupd_menu_block5_message)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)
    if message.text == "Учебно-методическое обеспечение дисциплины":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок 6", reply_markup=keyboard)
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
        bot.register_next_step_handler(send, rupd_main_menu_message)


@bot.message_handler(content_types=["text"])
def rupd_menu_block2_block1_handler(message):
    if message.text == "Регулятивные универсальные учебные действия":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок2 блок1 1", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block1_handler)
    if message.text == "Познавательные универсальные учебные действия":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок2 блок1 2", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block1_handler)
    if message.text == "Коммуникативные универсальные учебные действия":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок2 блок1 3", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)


@bot.message_handler(content_types=["text"])
def rupd_menu_block2_block2_handler(message):
    if message.text == "Обучаемый получит представление":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок2 блок2 1", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block2_handler)
    if message.text == "Обучаемый сможет":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок2 блок2 2", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block2_handler)
    if message.text == "Обучаемый научится":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок2 блок2 3", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_block2_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block2_message, reply_markup=rupd_menu_block2_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block2_handler)


@bot.message_handler(content_types="text")
def rupd_menu_block3_handler(message):
    if message.text == "Метапредметные результаты":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_block1_message, reply_markup=rupd_menu_block3_block1_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Часть 2. Выполнение обучаемым индивидуального проекта с применением AR-технологии-проекта " \
                       "«оживление учебника» в виде простого AR-приложения для Android-устройства с помощью " \
                       "ПО Blender, Unity3D и Vuforia":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок2", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_main_menu_message, reply_markup=rupd_menu_keyboard)
        bot.register_next_step_handler(send, rupd_main_menu_message)


@bot.message_handler(content_types=['text'])
def rupd_menu_block3_block1_handler(message):
    if message.text == "Тема 1. Введение в проектную культуру":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок1 1", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 2. Инициализация проекта":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок1 2", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 3. Базовое проектирование и исследование":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок1 3", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 4. Информационные ресурсы проектной и исследовательской деятельности":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок1 4", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 5. Презентация результатов проектной деятельности":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок1 5", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 6. Защита результатов проектной и исследовательской деятельности":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок1 6", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 7. Коммуникативные навыки":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок1 7", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Тема 8. Рефлексия проекта. Индивидуальный прогресс":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок3 блок1 8", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block3_message, reply_markup=rupd_menu_block3_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block3_handler)


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
        bot.register_next_step_handler(send, rupd_main_menu_message)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block1_handler(message):
    if message.text == "Требования, устанавленные ФГОС к результатам образования (ФГОС ООО, п.II.8, ФГОС СОО, п.II.6)":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 1", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Метапредметные результаты включают освоенные обучающимися":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 2", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Основные особенности оценки личностных, метапредметных и предметных результатов обучения":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 3", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Особенности индивидуального проекта":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 4", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Материалы, которые должны быть представлены к защите итогового проекта":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 5", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Организация защиты проекта":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 6", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Процедура оценивания сформированности УУД при защите реализованного проекта":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 7", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Критерии оценивания итогового проекта":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 8", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Подходы к оцениванию результатов итогового процесса":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 9", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Уровни сформированности навыков проектной деятельности (интегральный подход)":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок1 10", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block1_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message,
                                reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block2_handler(message):
    if message.text == "Компетентность отличается":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок2 1", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Три уровня компетенций":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок2 2", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Ключевые компетенции":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок2 3", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Уровни компетенций и способы деятельности учащихся":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок2 4", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block2_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message,
                                reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)


@bot.message_handler(content_types=['text'])
def rupd_menu_block5_block3_handler(message):
    if message.text == "К 2020 году каждый востребованный сотрудник должен будет уметь":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок3 1", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Система “4К”":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок3 2", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Подробнее о каждом из четырех «К»":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок3 3", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Оценка прогресса в критическом мышлении, креативности, коммуникации и кооперации":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="block1"))
        send = bot.send_message(message.from_user.id, text="Презентация блок5 блок3 4", reply_markup=keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_block3_handler)
    if message.text == "Назад":
        send = bot.send_message(message.from_user.id, text=rupd_menu_block5_message,
                                reply_markup=rupd_menu_block5_keyboard)
        bot.register_next_step_handler(send, rupd_menu_block5_handler)



def keyboard_builder(callback_data, manual):
    keyboard = types.InlineKeyboardMarkup()
    next_button = types.InlineKeyboardButton(text="Далее", callback_data=manual + str(callback_data+1))
    prv_button = types.InlineKeyboardButton(text="Назад", callback_data=manual + str(callback_data-1))
    to_begin = types.InlineKeyboardButton(text="В начало", callback_data=manual + str(0))
    if callback_data != 0:
        keyboard.add(prv_button)
    if callback_data != 28:
        keyboard.add(next_button)
    if callback_data == 28:
        keyboard.add(to_begin)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:



        if call.data == "":
            send = bot.send_message(call.message.from_user.id, text="")
            bot.register_next_step_handler(send, menu_handler)
        #bot.edit_message_media(media=types.InputMedia(type="photo", media=open(imagePath, "rb")), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard_builder(call_data, manual_data))
        #bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard_builder(call_data, manual_data), caption=caption, parse_mode="Markdown")


bot.polling(none_stop=True, interval=0)