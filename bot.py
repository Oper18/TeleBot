# -*- coding: utf-8 -*-

import config, settings
import telebot, eventlet, logging, requests
from telebot import TeleBot, types
from database import select_field

bot = telebot.TeleBot(config.telegramToken)

@bot.message_handler(commands = ["start"])
def Start(message):
    settings.Start(message)

@bot.message_handler(content_types = ['text'])
def FirstStep(message):
    if message.text == 'Задачи':
        messageText = 'Создай задачу или выбери интересующую профессию, чтобы увидеть список задач'
        settings.Buttons(message, config.buttonsSpec, messageText)
    else:
        bot.send_message(message.chat.id, 'stay there')

if __name__ == '__main__':
    bot.polling(none_stop = True)