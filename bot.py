# -*- coding: utf-8 -*-

import config
import telebot, eventlet, logging, requests, types

bot = telebot.TeleBot(config.telegramToken)

HelloText = 'Приветствую тебя! Зарегестрируйся для возможности просмотра заказов. ' \
            'Другие участники иогут видеть специальность и контакты только зарегистрированных пользователей.'

@bot.message_handler(func = lambda message: True, content_types=["text"])
def sendMessage(message):
    # bot.send_message(message.chat.id, 'Heil')
    # bot.send_message('@testapibotchan', 'Heil')
    # if message.text == '/heil':
    #     bot.send_message(message.chat.id, 'Heil')
    bot.send_message(message.chat.id, HelloText)

def StartList(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    FirstKey = types.KeyboardButton(text="1st Button", request_contact=True)
    keyboard.add(FirstKey)

if __name__ == '__main__':
    bot.polling(none_stop = True)