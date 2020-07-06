import csv
import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

with open('data.csv', encoding='utf8') as file:
    readCSV = csv.reader(file, delimiter=',')
    # print(list(readCSV))
    for row in readCSV:
        id = row[0]
        name = row[1]
        chinese = row[2]
        english = row[3]
        math = row[4]
        print(id, name, chinese, english, math)
        cursor.execute('INSERT INTO scores VALUES({}, "{}", {}, {}, {})'.format(id, name, chinese, english, math))
        conn.commit()
conn.close()