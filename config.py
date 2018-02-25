# -*- coding: utf-8 -*-

from database import select_field

#Telegram
telegramToken = '502817073:AAGzlHYifcRQfIyf1I8qKaHFUFlqkEHpiso'

#Buttons for menu

Users = select_field.SelectUsers()
Proffessions = select_field.SelectProfessions()
Specializaions = select_field.SelectSpecializations()
Problems = select_field.SelectProblem()
ChatId = select_field.SelectUsersChatId()

buttonsSpec = Specializaions
for i in range(len(buttonsSpec)):
    buttonsSpec[i] = buttonsSpec[i][1]

buttonsProf = Proffessions
for i in range(len(buttonsProf)):
    buttonsProf[i] = buttonsProf[i][0]