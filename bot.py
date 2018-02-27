# -*- coding: utf-8 -*-

import config, settings
import telebot, eventlet, logging, requests
from telebot import TeleBot, types
from database import add_field

bot = telebot.TeleBot(config.telegramToken)
previousStep = str()

@bot.message_handler(commands = ["start"])
def Start(message):
    result = settings.DetectUser(message.chat.id)
    if result == 'OK':
        print(message.chat.id)
        settings.Start(message)
    elif result == 'FAIL':
        messageText = 'Зарегестрируйся, чтобы продолжить'
        keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
        RegBut = types.KeyboardButton(text = 'Зарегестрироваться')
        keyboard.add(RegBut)
        # previousStep = 'Register'
        bot.send_message(message.chat.id, text = messageText, reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def FirstStep(message):
    global previousStep, problemSpec, nameUser, contact, profession

    if message.text == 'Задачи':
        messageText = 'Создай задачу или выбери интересующую профессию, чтобы увидеть список задач'
        settings.Buttons(message, config.buttonsSpec, messageText, 'Создать задачу')

    elif message.text == 'Список пользователей':
        messageText = 'Выбери специальность'
        #Add list for buttonsUser or something like this
        settings.Buttons(message, config.buttonsSpec, messageText, 'Зарегестрироваться')

    elif message.text == 'Создать задачу':

        if result == 'OK':
            messageText = 'Выбери специальность для задачи. Если не знаешь куда отнести задачу, нажми "Пропустить"'
            previousStep = 'Create problem'
            settings.AddNew(message, config.buttonsSpec, messageText, 'Пропустить')

        else:
            messageText = 'Создавать задачи могут только зарегистрированные пользователи. Зарегистрируйся'
            keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
            RegBut = types.KeyboardButton(text = 'Зарегестрироваться')
            BackBut = types.KeyboardButton(text = 'Назад')
            ToStartBut = types.KeyboardButton(text = 'В начало')
            keyboard.add(RegBut, BackBut, ToStartBut)
            previousStep = 'Register'
            bot.send_message(message.chat.id, text = messageText, reply_markup = keyboard)
            #To next tests need to add add user step!!!

    elif previousStep == 'Create problem':
        messageText = 'Напиши название и с новой строки текст задачи одним сообщением'
        backBut = types.KeyboardButton(text = 'Назад')
        toStartBut = types.KeyboardButton(text = 'В начало')
        keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
        keyboard.add(backBut, toStartBut)
        bot.send_message(message.chat.id, text = messageText, reply_markup = keyboard)
        previousStep = 'Create problem at spec'
        problemSpec = message.text

    elif previousStep == 'Create problem at spec':
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
        textProblem = message.text[i + 1:]

        for i in range(len(config.ChatId)):
            if message.chat.id in config.ChatId[i]:
                nameUser = config.ChatId[i][2]
                break

        for i in range(len(config.Specializaions)):
            if problemSpec in config.Specializaions[i]:
                problemSpec = config.Specializaions[i][0]
                break

        add_field.Problems(nameProblem, textProblem, nameUser, problemSpec)

    elif message.text == 'Зарегестрироваться':
        bot.message_handler(content_types = ['text'])
        messageText = 'Введи свое имя'
        previousStep = 'Name'
        bot.send_message(message.chat.id, text = messageText)

    elif previousStep == 'Name':
        bot.message_handler(content_types = ['text'])
        messageText = 'Введи свой username начиная с @'
        # while message.text[0] != '@':
        #     bot.send_message(message.chat.id, text = 'Делай как написано, не будь оленем!')
        previousStep = 'Contact'
        nameUser = message.text
        bot.send_message(message.chat.id, text = messageText)

    elif previousStep == 'Contact':
        bot.message_handler(content_types = ['text'])
        messageText = 'Выбери профессию'
        settings.Buttons(message, config.buttonsProf, messageText, 'Без профессии')
        previousStep = 'add'
        contact = message.text

    elif previousStep == 'add':
        print(message.text)
        profession = message.text
        add_field.Users(message.chat.id, nameUser, contact, profession)
        Start(message)

    else:
        bot.send_message(message.chat.id, 'Не выебывайся, жми на кнопки!')

if __name__ == '__main__':
    bot.polling(none_stop = True)