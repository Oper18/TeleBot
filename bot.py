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
    messageText = 'Sieg'
    settings.Buttons(message, config.buttonsSpec, messageText)

if __name__ == '__main__':
    bot.polling(none_stop = True)