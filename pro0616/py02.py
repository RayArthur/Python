import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# conn.execute('UPDATE scores SET name="AmyLee" WHERE id=1')
conn.execute('DELETE FROM scores WHERE id=2')

conn.commit()
conn.close()