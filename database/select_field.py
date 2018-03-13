# -*- coding: utf-8 -*-

import sqlite3

class SelectFieldClass:
    def __init__(self):
        self.nameDB = '/home/data/documents/python/app_bot/TeleBot/database/botDB'

        self.connect = sqlite3.connect(self.nameDB)

        self.cursor = self.connect.cursor()

    def SelectUsers(self):
        answer = []
        self.cursor.execute("SELECT * FROM users")
        userID = self.cursor.fetchall()
        if len(userID) != 0:
            for i in range(len(userID)):
                userID[i] = userID[i][2:]
                answer.append(['Имя: ', 'Контакты: ', 'Профессия: '])
                for j in range(len(userID[i])):
                    answer[i][j] = answer[i][j] + userID[i][j]
        else:
            answer = ['Специалистов не найдено']

        return answer

    def SelectUsersChatId(self):
        answer = []
        self.cursor.execute("SELECT * FROM users")
        userID = self.cursor.fetchall()
        for i in range(len(userID)):
            userID[i] = userID[i][0:3]
            answer.append(userID[i])

        return answer

    def SelectProblem(self):
        answer = []
        self.cursor.execute("SELECT * FROM problems")
        problemID = self.cursor.fetchall()
        if len(problemID) != 0:
            for i in range(len(problemID)):
                problemID[i] = problemID[i][1:]
                answer.append(['Название: ', 'Пользователь: ', 'Специализация: ', 'Суть проблемы: ', 'Контакт: '])
                for j in range(len(problemID[i])):
                    if j == 2:
                        self.cursor.execute("SELECT contact FROM users WHERE name='%s'" % problemID[i][j])
                        contact = cursor.fetchall()
                        answer[i][5] = answer[i][5] + contact
                    answer[i][j] = answer[i][j] + problemID[i][j]
        else:
            answer = ['Задач не найдено']

        return answer

    def SelectSpecializations(self):
        self.cursor.execute("SELECT * FROM specializations")
        specID = self.cursor.fetchall()
        # if len(specID) != 0:
        #     for i in range(len(specID)):
        #         specID[i] = specID[i][1:]
        return specID

    def SelectProfessions(self):
        self.cursor.execute("SELECT * FROM professions")
        profID = self.cursor.fetchall()
        if len(profID) != 0:
            for i in range(len(profID)):
                profID[i] = profID[i][1:]
        return profID