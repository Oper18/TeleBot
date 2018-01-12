# -*- coding: utf-8 -*-

import sqlite3

nameDB = ''

connect = sqlite3.connect(nameDB)

cursor = connect.cursor()

def SelectUsers(field):
    answer = []
    cursor.execute("SELECT * FROM users WHERE name='%s'" % field)
    userID = cursor.fetchall()
    if len(userID) != 0:
        for i in range(len(userID)):
            userID[i] = userID[i][1:]
            answer.append(['Имя: ', 'Контакты: ', 'Профессия: '])
            for j in range(len(userID[i])):
                answer[i][j] = answer[i][j] + userID[i][j]
    else:
        answer = ['Специалистов не найдено']

    return answer

def SelectProblem(field):
    answer = []
    cursor.execute("SELECT * FROM problems WHERE name='%s'" % field)
    problemID = cursor.fetchall()
    if len(problemID) != 0:
        for i in range(len(problemID)):
            problemID[i] = problemID[i][1:]
            answer.append(['Название: ', 'Пользователь: ', 'Специализация: ', 'Суть проблемы: ', 'Контакт: '])
            for j in range(len(problemID[i])):
                if j == 2:
                    cursor.execute("SELECT contact FROM users WHERE name='%s'" % problemID[i][j])
                    contact = cursor.fetchall()
                    answer[i][5] = answer[i][5] + contact
                answer[i][j] = answer[i][j] + problemID[i][j]
    else:
        answer = ['Задач не найдено']

    return answer

def SelectSpecializations():
    cursor.execute("SELECT * FROM specializations")
    specID = cursor.fetchall()
    if len(specID) != 0:
        for i in range(len(specID)):
            specID[i] = specID[i][1:]
    return specID

def SelectProfessions():
    cursor.execute("SELECT * FROM professions")
    profID = cursor.fetchall()
    if len(profID) != 0:
        for i in range(len(profID)):
            profID[i] = profID[i][1:]
    return profID