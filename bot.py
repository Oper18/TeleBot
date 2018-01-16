# -*- coding: utf-8 -*-

import config
import telebot, eventlet, logging, requests
from telebot import TeleBot, types
from database import select_field

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
    keyboard.add(TaskBut, UserBut)
    bot.send_message(message.chat.id, HelloText, reply_markup=keyboard)
    print(message.chat.id)

@bot.message_handler(func = lambda message: True, content_types=['text'])
def Answer(message):
    # bot.reply_to(message, message.text)
    buttons = []
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    NewBut = types.KeyboardButton(text='Здесь будет продолжение дерева')
    BackBut = types.KeyboardButton(text='Назад')
    keyboard.add(NewBut, BackBut)
    bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    if message.text == 'Назад':
        sendMessage(message)

if __name__ == '__main__':
    bot.polling(none_stop = True)