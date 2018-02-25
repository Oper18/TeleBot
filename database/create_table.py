# -*- coding: utf-8 -*-

import sqlite3

nameDB = '/home/data/documents/python/app_bot/TeleBot/database/botDB'

connect = sqlite3.connect(nameDB)

cursor = connect.cursor()

#Create specialization table
try:
    cursor.execute('''CREATE TABLE specializations
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name text NOT NULL)''')
except:
    print('Table was created earlier')

#Create profession table with reference to specialization
try:
    cursor.execute('''CREATE TABLE professions
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name text NOT NULL, specialization int NOT NULL,
                    FOREIGN KEY (specialization) REFERENCES specializations (id))''')
except:
    print('Table was created earlier')

#Create users table with reference to profession
try:
    cursor.execute('''CREATE TABLE users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, chatid INTEGER NOT NULL, name text NOT NULL,
                    contact text NOT NULL, profession int NOT NULL, 
                    FOREIGN KEY (profession) REFERENCES professions (id))''')
except:
    print('Table was created earlier')

#Create problem table with reference to specialization and user
try:
    cursor.execute('''CREATE TABLE problems
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name text NOT NULL, user int NOT NULL,
                    specialization int NOT NULL, problem text NOT NULL, FOREIGN KEY (user) REFERENCES users (id),
                    FOREIGN KEY (specialization) REFERENCES specializations (id))''')
except:
    print('Table was created earlier')

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
cursor.execute('''PRAGMA table_info(specializations)''')
tableSpec = cursor.fetchall()
cursor.execute('''PRAGMA table_info(professions)''')
tableProf = cursor.fetchall()
cursor.execute('''PRAGMA table_info(users)''')
tableUser = cursor.fetchall()
cursor.execute('''PRAGMA table_info(problems)''')
tableProblem = cursor.fetchall()

print('tables: %s' % tables)
print('Specializations: %s' % tableSpec)
print('Professions: %s' % tableProf)
print('Users: %s' % tableUser)
print('Problems: %s' % tableProblem)

connect.commit()
connect.close()