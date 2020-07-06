import pymssql

conn = pymssql.connect(server='127.0.0.1:1433', user='gjun', password='12345', database='pythondb', charset='utf8')
cursor = conn.cursor()

while True:
    name = input('Name：')
    if name == '': break
    chinese = int(input('Chinese：'))
    english = int(input('English：'))
    math = int(input('Math：'))

    sql = '''INSERT INTO scores(name, chinese, english, math) VALUES('{}', {}, {}, {})'''.format(name, chinese, english, math)
    print(sql)
    cursor.execute(sql)
    conn.commit()

    sql = 'SELECT * FROM scores'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print('-----------------------------------')

conn.close()