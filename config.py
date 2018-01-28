# -*- coding: utf-8 -*-

from database import select_field

#Telegram
telegramToken = '502817073:AAGzlHYifcRQfIyf1I8qKaHFUFlqkEHpiso'

#Buttons for menu
buttonsProf = select_field.SelectProfessions()
for i in range(len(buttonsProf)):
    buttonsProf[i] = buttonsProf[i][0]

def callDatabase(fields):
    usersList = select_field.SelectUsers(fields)
    return usersList