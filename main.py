import telebot
from telebot import types


bot = telebot.TeleBot("1284427462:AAHPyWAvdRGT104ol7fCp4PXELJmAi55EwU")

#region variables
unity = [
"**Установка**\nДля начала работы с Unity требуется перейти на официальный сайт [Unity](https://unity.com) и нажать кнопку Get started",
"После перехода на новую страницу выбрать вкладку Individual и далее, нажать на кнопку Get Started ",
"После перехода на новую страницу выбрать Start Here на вкладке First-Time Users. После нажатия данной кнопки начнется скачивание установщика Unity Hub – специального установщика для продуктов Unity. В нем будет необходимо выбрать папку, в которую вы хотите в дальнейшем установить Unity Hub и сам Unity. После завершения откройте Unity Hub. Для дальнейшей установки Unity понадобится Unity ID. Регистрацию можно совершить либо на официальном сайте, либо в приложении, следуя подсказкам. При выборе лицензии Unity выбирайте индивидуальную бесплатную.",
"**Установка Unity Editor и создание проекта**\nВ открытом Unity Hub выберите вкладку Installs и далее нажмите на кнопку Add.",
"Вам будет предложено несколько версий Unity. Советуем установить версию, которую рекомендует сам Unity Hub. Нажмите на кнопку Next.  ",
"Далее вам будут представлены несколько модулей на установку. Так как наше AR-приложение будет на IOS/Android - выбирайте данные модули (как показано на скриншоте). ",
"После завершения установки Unity Editor Кликните на вкладку Projects, затем на кнопку New. Откроется Окно создания проекта. Выберите опцию 3D и нажмите кнопку Create",
"**Добавление Vuforia в Unity**\nПерейдите на [официальный сайт Vuforia](https://developer.vuforia.com). Зарегистрируйтесь, и после регистрации нажмите на вкладку Downloads",
"Далее нажмите на ссылку Add Vuforia to a Unity Project. Начнется скачивание файла Vuforia.unitypackage. После того, как загрузка завершится, откроется окно импорта Package (пакетов расширений для Unity). Нажмите кнопку Import.",
"После завершения всех операций, вы сможете пользоваться объектами Vuforia Engine. Но для их использования потребуется включение настроек в Unity Editor. Откройте Unity Editor, выберите вкладки Edit — Project Settings — Player — XR Settings и поставьте галочку Vuforia Augmented Reality Supported.",
"Далее необходимо получить лицензионный ключ и создать базу изображений для корректной работы Vuforia. Для этого переходим на [официальный сайт Vuforia](https://developer.vuforia.com) и кликаем на вкладку Develop.",
"Для того чтобы получить лицензионный ключ, зайдите в свой созданный аккаунт, и нажмите на кнопку Get Development Key. Дайте название этому ключу.",
"После этого, данный ключ появится в вашем списке лицензий",
"Нажмите на созданный ключ. Откроется страница с вашей лицензией. Вы увидите окно с различными символами, кликните на него.",
"Далее необходимо вернуться обратно в Unity Editor. Для начала работы с Vuforia удалите объект Main Camera. Это можно сделать с помощью клавиши Delete или нажав ПКМ и выбрав опцию Delete в контекстном меню",
"Далее переходим во вкладку GameObject — Vuforia Engine — AR Camera и выбираем эту опцию.",
"При появлении окна нажимаем кнопку Import. Теперь в нашем проекте есть AR Camera, которая является основой работы нашего приложения дополненной реальности. Камера используется непосредственно для отрисовки различных объектов.",
"Далее необходимо добавить ключ с сайта Vuforia в наше приложение. Для этого нажимаем на AR Camera, и в окне справа нажимаем на Open Device Configuration.",
"После этого справа появятся опции камеры, где будет место для добавления ключа с сайта Vuforia, который мы получили ранее. Вставляем ключ с сайта в место на скриншоте.",
"Далее необходимо создать базу распознаваемых изображений. Для этого переходим на [официальный сайт Vuforia](https://developer.vuforia.com). Переходим во вкладку Develop — Target Manager и нажимаем Add Database.",
"В появившемся окне выбираем Device и вводим имя базы данных. После этого она появится в списке баз данных, нажмите на нее.",
"Для того, чтобы добавить распознаваемое изображение, нажмите Add Target.",
"В появившемся окне выбираем Single Image, выбираем файл на вашем компьютере нужного формата (.jpg или .png), ставим в поле Width значение 5 и вписываем любое имя.",
"В дальнейшем, при необходимости, можно также добавлять распознаваемые изображения. После добавления изображений, нажмите Download Database(All) и выберите Unity Editor. Точно так же открываем скачанный файл формата Unity Package и нажимаем в появившемся окне Import.",
"Перейдите обратно в Unity Editor. Теперь можно начать добавлять распознаваемые объекты в наш проект. Для этого нажмите ПКМ на левой панели объектов и выберите Vuforia Engine — Image. ",
"После этого добавится изображение, которое будет распознаваться приложением. Для выбора разных распознаваемых изображений необходимо в Image Target Behaviour на вкладке Image Target выбрать другое изображение (если они имеются в базе). ",
"Чтобы добавить к этому изображению 3D модель, добавьте свой объект в формате .obj в Unity Editor, в нижнюю панель, а потом перенесите данную модель к ImageTarget как дочерний (как на скриншоте). Этот шаг можно повторять для каждого распознаваемого изображения/объекта.",
"**Сборка проекта**\nДля того чтобы превратить проект из Unity Editor в приложении на Android или IOS нужно совершить «сборку» проекта. Для этого перейдите во вкладку File — Build Settings",
"В появившемся окне выберите Android/IOS. Если кнопка Build and Run серая и не нажимается, то сначала нажмите кнопку Switch Platform, а затем кнопку Build and Run. Далее, выберите место на компьютере где вы хотите сохранить приложение в формате .apk. Далее, данный файл .apk переместите на телефон и установите. После установки на телефон и наведения на распознаваемые изображения вы будете видеть ваши модели. Поздравляем, вы сделали свое приложение с дополненной реальностью!"
]
#endregion

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, "Привет! Это бот-помощник по дисциплине Индивидуальный проект. Комманда /help поможет начать")


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, "Доступные команды: \n")


@bot.message_handler(commands=["Unity", "Юнити"])
def unity_start(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Далее", callback_data="u1")
    keyboard.add(callback_button)
    bot.send_photo(message.chat.id, photo=open("unityImages/1.png", "rb"), caption=unity[0], reply_markup=keyboard, parse_mode="Markdown")


def keyboard_builder(callback_data):
    keyboard = types.InlineKeyboardMarkup()
    next_button = types.InlineKeyboardButton(text="Далее", callback_data="u" + str(callback_data+1))
    prv_button = types.InlineKeyboardButton(text="Назад", callback_data="u" + str(callback_data-1))
    if callback_data != 0:
        keyboard.add(prv_button)
    if callback_data != 28:
        keyboard.add(next_button)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        call_data = int(call.data[1:])
        bot.edit_message_media(media=types.InputMedia(type="photo", media=open(f"unityImages/{call_data+1}.png", "rb")), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard_builder(call_data))
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard_builder(call_data), caption=unity[call_data], parse_mode="Markdown")


bot.polling(none_stop=True, interval=0)