import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS scores(
'id' INTEGER PRIMARY KEY NOT NULL,
'name' TEXT NOT NULL,
'chinese' INTEGER NOT NULL,
'english' INTEGER NOT NULL,
'math' INTEGER NOT NULL)'''

cursor.execute(sql)

cursor.execute('INSERT INTO scores VALUES(1, "Amy", 65, 65, 40)')
cursor.execute('INSERT INTO scores VALUES(2, "Tom", 85, 90, 99)')
cursor.execute('INSERT INTO scores VALUES(3, "Lisa", 90, 92, 86)')
conn.commit()

conn.close()

