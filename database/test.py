# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('testDB.db')

#conn.executescript('''PRAGMA foreign_keys=on''')

curs = conn.cursor()

curs.execute("DROP TABLE specializations")
curs.execute("DROP TABLE users")

name = 'specializations'
columnname = 'name'

try:
    curs.execute('''CREATE TABLE %s
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, %s text NOT NULL)''' % (name, columnname))
except:
    print('Table specializations was created earlier')

#curs.execute('''CREATE TABLE specializations
                    #(id INTEGER PRIMARY KEY AUTOINCREMENT, namespec text NOT NULL)''')

name2 = 'users'
columns = ['name', 'contact']
print(columns)

try:
    curs.execute('''CREATE TABLE %s
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, %s text NOT NULL, %s text NOT NULL, namespec int NOT NULL,
                        FOREIGN KEY (namespec) REFERENCES specializations (id))''' % (name2, columns[0], columns[1]))
except:
    print('Table users was created earlier')

curs.execute("INSERT INTO specializations VALUES (NULL, 'electronic')")

curs.execute("SELECT * FROM specializations WHERE name='electronic'")

specID = curs.lastrowid

print(specID)

name = 'bob'
contact = 'contact'

curs.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (name, contact, specID,))

curs.execute("SELECT * FROM users")

users = curs.fetchall()

curs.execute("INSERT INTO users VALUES (NULL, 'jane', 'nocont', ?)", (specID,))

curs.execute("SELECT * FROM users")

users = curs.fetchall()

print(users)

curs.execute("SELECT contact FROM users WHERE name='%s'" % name)
cont = curs.fetchall()
print(cont)

curs.execute("SELECT * FROM specializations")

spec = curs.fetchall()

print(spec)

curs.execute("SELECT name FROM sqlite_master WHERE type='table'")

tables = curs.fetchall()

print(tables)

curs.execute('''PRAGMA table_info(users)''')
usertable = curs.fetchall()

print(usertable)

#curs.execute('''DELETE FROM specializations WHERE id=1''')
#curs.execute('''DELETE FROM specializations WHERE id=2''')
#curs.execute('''DELETE FROM specializations WHERE id=3''')
#curs.execute('''DELETE FROM users WHERE id=1''')
#curs.execute('''DELETE FROM users WHERE id=2''')
#curs.execute('''DELETE FROM users WHERE id=3''')

#conn.commit()

#a = [(1,2,3), (4,5,6)]
#b = []

#for i in range(len(a)):
    #a[i]=a[i][1:]
    #b.append(['num1: ', 'num2: '])
    #print(i)
    #for j in range(len(a[i])):
        #print(b[i][j])
        #b[i][j] = b[i][j]+str(a[i][j])
#print(b)