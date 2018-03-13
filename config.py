# -*- coding: utf-8 -*-

from database import select_field

#Telegram
telegramToken = '502817073:AAGzlHYifcRQfIyf1I8qKaHFUFlqkEHpiso'

#Buttons for menu
# Users = select_field.SelectUsers()
# Proffessions = select_field.SelectProfessions()
# Specializaions = select_field.SelectSpecializations()
# Problems = select_field.SelectProblem()
# ChatId = select_field.SelectUsersChatId()

# Users = select_field.SelectFieldClass().SelectUsers()
# Proffessions = select_field.SelectFieldClass().SelectProfessions()
# Specializaions = select_field.SelectFieldClass().SelectSpecializations()
# Problems = select_field.SelectFieldClass().SelectProblem()
# ChatId = select_field.SelectFieldClass().SelectUsersChatId()

buttonsSpec = Specializaions
for i in range(len(buttonsSpec)):
    buttonsSpec[i] = buttonsSpec[i][1]

buttonsProf = Proffessions
for i in range(len(buttonsProf)):
    buttonsProf[i] = buttonsProf[i][0]