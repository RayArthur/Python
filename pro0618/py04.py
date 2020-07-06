import pymssql

conn = pymssql.connect(server='127.0.0.1:1433', user='gjun', password='12345', database='pythondb', charset='utf8')

with conn.cursor() as cursor:
    id = input('Id：')
    name = input('Name：')
    sql = "SELECT * FROM scores WHERE id={} AND name='{}'".format(id, name)
    print(sql)
    cursor.execute(sql)
    row = cursor.fetchone()
    if row != None:
        print(row)
        keyin = input('1.修改 2.刪除 0.結束：')
        if keyin == '1':
            print('修改...')
            id, name, chinese, english, math = row
            temp = input('[' + name + '] Name：')
            if temp != '':
                name = temp
            temp = input('[' + str(chinese) + '] Chinese：')
            if temp != '':
                chinese = temp
            temp = input('[' + str(english) + '] nglish：')
            if temp != '':
                english = temp
            temp = input('[' + str(math) + '] Math：')
            if temp != '':
                math = temp
            sql = "UPDATE scores SET name='{}', chinese={}, english={}, math={} WHERE id={}".format(name, chinese,english, math,id)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        elif keyin == '2':
            print('刪除...')
            sql = "DELETE FROM scores WHERE id={}".format(id)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        else:
            print('結束!')

conn.close()

