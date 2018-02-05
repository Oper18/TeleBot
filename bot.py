# -*- coding: utf-8 -*-

import config
import telebot, eventlet, logging, requests
from telebot import TeleBot, types
from database import select_field

bot = telebot.TeleBot(config.telegramToken)

HelloText = 'Приветствую тебя! Зарегестрируйся для возможности просмотра заказов. ' \
            'Другие участники иогут видеть специальность и контакты только зарегистрированных пользователей.'

# @bot.message_handler(func = lambda message: True, content_types=["start"])
@bot.message_handler(commands = ["start"])
def sendMessage(message):
    # bot.send_message(message.chat.id, HelloText)
    keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
    TaskBut = types.KeyboardButton(text = 'Задачи')
    UserBut = types.KeyboardButton(text = 'Список пользователей')
    keyboard.add(TaskBut, UserBut)
    bot.send_message(message.chat.id, text = HelloText, reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def Answer(message):
    buttons = []
    for i in range(len(config.buttonsSpec)):
        buttons.append('Button'+str(i))
    for i in range(len(buttons)):
        buttons[i] = types.KeyboardButton(text = '{}'.format(config.buttonsSpec[i]))
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    BackBut = types.KeyboardButton(text = 'Назад')
    ToStartBut = types.KeyboardButton(text = 'В начало')
    for i in range(len(buttons)):
        keyboard.add(buttons[i])
    keyboard.add(ToStartBut, BackBut)
    bot.send_message(message.chat.id, message.text, reply_markup = keyboard)
    if message.text == 'В начало':
        sendMessage(message)
    if message.text == 'Назад':
        sendMessage(message)
    if message.text != 'В начало' or message.text != 'Назад':
        UserList(message)

def UserList(message):
    users = config.Users
    buttons = []
    print(type(message))
    print(config.buttonsProf)
    for i in range(len(config.buttonsProf)):
        buttons.append('Buttons' + str(i))
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    createBut = types.KeyboardButton(text = 'Создать задачу')
    for i in range(len(buttons)):
        buttons[i] = types.KeyboardButton(text = '{}'.format(config.buttonsProf[i]))
    keyboard.add(createBut)
    for i in range(len(buttons)):
        keyboard.add(buttons[i])
    bot.send_message(message.chat.id, message.text, reply_markup = keyboard)
        # if message == config.but(tonsProf[i]:
        #     for j in range(len(users)):
        #         print(users[j][-1])
        #         if users[j][-1] == 'Профессия: {}'.format(message):
        #             print(users[j])
    # bot.reply_to(message, select_field.SelectUsers())

if __name__ == '__main__':
    bot.polling(none_stop = True)