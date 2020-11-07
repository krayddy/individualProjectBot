import telebot
from telebot import types


bot = telebot.TeleBot("1284427462:AAHPyWAvdRGT104ol7fCp4PXELJmAi55EwU")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, "Привет! Это бот-помощник по дисциплине Индивидуальный проект.")


bot.polling(none_stop=True, interval=0)