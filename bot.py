# -*- coding: utf-8 -*-

import config
import datetime
import telebot, eventlet, logging, requests
from telebot import TeleBot, types

bot = telebot.TeleBot(config.telegramToken)

HelloText = 'Приветствую тебя! Зарегестрируйся для возможности просмотра заказов. ' \
            'Другие участники иогут видеть специальность и контакты только зарегистрированных пользователей.'

# @bot.message_handler(func = lambda message: True, content_types=["start"])
@bot.message_handler(commands=["start"])
def sendMessage(message):
    # bot.send_message(message.chat.id, HelloText)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    TaskBut = types.KeyboardButton(text='Задачи')
    UserBut = types.KeyboardButton(text='Список пользователей')
    SpecBut = types.KeyboardButton(text='Специализация')
    keyboard.add(TaskBut, UserBut, SpecBut)
    bot.send_message(message.chat.id, HelloText, reply_markup=keyboard)

if __name__ == '__main__':
    bot.polling(none_stop = True)