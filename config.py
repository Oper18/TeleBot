# -*- coding: utf-8 -*-

from database import select_field

#Telegram
telegramToken = '502817073:AAGzlHYifcRQfIyf1I8qKaHFUFlqkEHpiso'

#Buttons for menu
buttonsProf = select_field.SelectSpecializations()
for i in range(len(buttonsProf)):
    buttonsProf[i] = buttonsProf[i][0]

Users = select_field.SelectUsers('profession')

Problems = select_field.SelectProblem('specialization')