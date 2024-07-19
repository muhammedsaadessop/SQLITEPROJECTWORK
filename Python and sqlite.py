1

 import sqlite3
connection = sqlite3.connect('northwind.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Category')
first_row = cursor.fetchone()
print(first_row)
connection.close()

2
import sqlite3
conn = sqlite3.connect('northwind.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Category")
first_row = cursor.fetchone()
second_row = cursor.fetchone()
print(first_row)
print(second_row)
conn.close()

3

import sqlite3
conn = sqlite3.connect('northwind.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Category")
rows = cursor.fetchall()
print(rows)
conn.close()

4

import sqlite3
conn = sqlite3.connect('northwind.db')
cur = conn.cursor()
cur.execute('''SELECT * FROM Category''')
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()

5

import sqlite3
conn = sqlite3.connect('northwind.db')
cur = conn.cursor()
cur.execute('''SELECT * FROM Category''')
rows = cur.fetchall()
for row in rows:
    print(row[1])
conn.close()

import sqlite3
conn = sqlite3.connect('northwind.db')
cur = conn.cursor()
cur.execute('''SELECT * FROM Category''')
rows = cur.fetchall()
for category_id, category_name, description in rows:
    print(category_name)
conn.close()

6
import sqlite3
conn = sqlite3.connect('northwind.db')
cur = conn.cursor()
cur.execute('''SELECT FirstName, LastName, Title, City FROM Employee''')
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()

7

import sqlite3
conn = sqlite3.connect('northwind.db')
cur = conn.cursor()
cur.execute('''SELECT FirstName, LastName, Title, City FROM Employee''')
rows = cur.fetchmany(3)
for row in rows:
    print(row)
conn.close()
