import telebot
from telebot import types

token = '7384184406:AAF-kbng8DTneTN75WPA5_ZgG9yUgI8ZFzE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я - ваш электронный помощник по документации. Чем я могу вам помочь?")

bot.infinity_polling()
