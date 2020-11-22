import telebot
from telebot import types


bot = telebot.TeleBot("1284427462:AAHPyWAvdRGT104ol7fCp4PXELJmAi55EwU")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, "Привет! Это бот-помощник по дисциплине Индивидуальный проект. Комманда /help поможет начать")


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, "Доступные команды: \n /file \n /start")


@bot.message_handler(commands=['file'])
def file_handler(message):
    doc = open('requirements.txt', 'rb')
    bot.send_document(message.from_user.id, doc)


@bot.message_handler(commands=['check'])
def help_handler(message):
    bot.send_message(message.from_user.id, "Автоматическая привязка")


bot.polling(none_stop=True, interval=0)