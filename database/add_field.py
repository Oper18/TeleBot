# -*- coding: utf-8 -*-

import sqlite3

result = 'FAIL'

nameDB = ''

connect = sqlite3.connect(nameDB)

cursor = connect.cursor()

def Specialization(nameSpec):
    cursor.execute("INSERT INTO specializations VALUES (NULL, ?)", (nameSpec,))

def Profession(nameProf, nameSpec):
    cursor.execute("SELECT * FROM specializations")
    specID = cursor.fetchall()
    for i in range(len(specID)):
        if specID[i][1] == nameSpec:
            cursor.execute("INSERT INTO professions VALUES (NULL, ?, ?)", (nameProf, specID[i],))
            result = 'OK'
            break
    return result

def Users(nameUser, contact, nameProf):
    cursor.execute("SELECT * FROM professions")
    profID = cursor.fetchall()
    for i in range(len(profID)):
        if profID[i][1] == nameProf:
            cursor.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (nameUser, contact, profID[i],))
            result = 'OK'
            break
    return result

def Problems(nameProblem, textProblem, nameUser, nameSpec):
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
    return result