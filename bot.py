# -*- coding: utf-8 -*-

import config, settings
import telebot, eventlet, logging, requests
from telebot import TeleBot, types
from database import select_field

bot = telebot.TeleBot(config.telegramToken)
previousStep = str()

@bot.message_handler(commands = ["start"])
def Start(message):
    print(message.chat.id)
    settings.Start(message)

@bot.message_handler(content_types = ['text'])
def FirstStep(message):
    global previousStep

    if message.text == 'Задачи':
        messageText = 'Создай задачу или выбери интересующую профессию, чтобы увидеть список задач'
        settings.Buttons(message, config.buttonsSpec, messageText, 'Создать задачу')

    elif message.text == 'Список пользователей':
        messageText = 'Выбери специальность'
        #Add list for buttonsUser or something like this
        settings.Buttons(message, config.buttonsSpec, messageText, 'Зарегестрироваться')

    elif message.text == 'Создать задачу':
        messageText = 'Выбери специальность для задачи. Если не знаешь куда отнести задачу, нажми "Пропустить"'
        previousStep = 'Создать задачу'
        settings.AddNew(message, config.buttonsSpec, messageText, 'Пропустить')

    elif previousStep == 'Создать задачу':
        messageText = 'Напиши название и с новой строки текст задачи одним сообщением'
        backBut = types.KeyboardButton(text = 'Назад')
        toStartBut = types.KeyboardButton(text = 'В начало')
        keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
        keyboard.add(backBut, toStartBut)
        bot.send_message(message.chat.id, text = messageText, reply_markup = keyboard)
        bot.message_handler(content_types = ['text'])
        i = 0
        nameProblem = str()
        while message.text[i] != '\n':
            if '\n' not in message.text:
                bot.send_message(message.chat.id, text = 'Делай как написано, не будь оленем!')
                break
            else:
                nameProblem = nameProblem + message.text[i]
                i = i + 1
        textProblem = message.text[i:]
        print(nameProblem)
        print(textProblem)

    else:
        bot.send_message(message.chat.id, 'Не выебывайся, жми на кнопки!')

if __name__ == '__main__':
    bot.polling(none_stop = True)