# -*- coding: utf-8 -*-

import sqlite3
from database import add_field, select_field

# add_field.Specialization('Инженер')
# add_field.Profession('Электроника', 'Инженер')
# print(select_field.SelectProfessions())
# add_field.Users('Bob', '@Bob', 'Электроника')
# add_field.Users('Jane', '@Jane', 'Электроника')
# print(select_field.SelectAllUsers())
# print(select_field.SelectUsers())

# add_field.Specialization('Неуказана')
# add_field.Profession('Без профессии', 'Неуказана')

# nameDB = '/home/data/documents/python/app_bot/TeleBot/database/botDB'
# connect = sqlite3.connect(nameDB)
#
# cursor = connect.cursor()
# cursor.execute("DELETE FROM users WHERE name='Wookie'")
# connect.commit()
# connect.close()

# print(select_field.SelectSpecializations())
# print(select_field.SelectProfessions())
print(select_field.SelectUsers())