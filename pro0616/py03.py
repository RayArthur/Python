import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.execute('SELECT * FROM scores')
rows = cursor.fetchall()

print(rows)

for row in rows:
    print(row[0], row[1], row[2], row[3], row[4])

conn.close()



