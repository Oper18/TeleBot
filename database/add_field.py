# -*- coding: utf-8 -*-

import sqlite3

result = 'FAIL'

nameDB = '/home/data/documents/python/app_bot/TeleBot/database/botDB'

# connect = sqlite3.connect(nameDB)
#
# cursor = connect.cursor()

def Specialization(nameSpec):
    connect = sqlite3.connect(nameDB)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO specializations VALUES (NULL, ?)", (nameSpec,))
    connect.commit()
    connect.close()

def Profession(nameProf, nameSpec):
    result = 'FAIL'
    connect = sqlite3.connect(nameDB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM specializations")
    specID = cursor.fetchall()
    for i in range(len(specID)):
        if specID[i][1] == nameSpec:
            cursor.execute("INSERT INTO professions VALUES (NULL, ?, ?)", (nameProf, specID[i][0],))
            result = 'OK'
            break
    connect.commit()
    connect.close()
    return result

def Users(chatid, nameUser, contact, nameProf):
    result = 'FALSE from Users'
    connect = sqlite3.connect(nameDB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM professions")
    profID = cursor.fetchall()
    for i in range(len(profID)):
        if profID[i][1] == nameProf:
            cursor.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", (chatid, nameUser, contact, profID[i][1],))
            result = 'OK'
            break
    connect.commit()
    connect.close()
    return result

def Problems(nameProblem, textProblem, nameUser, nameSpec):
    connect = sqlite3.connect(nameDB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM users")
    userID = cursor.fetchall()
    for i in range(len(userID)):
        if userID[i][1] == nameUser:
            cursor.execute("SELECT *FROM specializations")
            specID = cursor.fetchall()
            for j in range(len(specID)):
                if specID[j][1] == nameSpec:
                    cursor.execute("INSERT INTO problems VALUES (NULL, ?, ?, ?, ?", (nameProblem, userID[i],
                        specID[j], textProblem,))
                    result = 'OK'
                    break
    connect.commit()
    connect.close()
    return result