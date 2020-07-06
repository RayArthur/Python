import pymssql

conn = pymssql.connect(server='127.0.0.1:1433', user='gjun', password='12345', database='pythondb')

cursor = conn.cursor()

# # 新建、插入操作
# cursor.execute("""
# IF OBJECT_ID('persons', 'U') IS NOT NULL
#   DROP TABLE persons
# CREATE TABLE persons (
#   id INT NOT NULL,
#   name VARCHAR(100),
#   salesrep VARCHAR(100),
#   PRIMARY KEY(id)
# )
# """)
# cursor.executemany(
#   "INSERT INTO persons VALUES (%d, %s, %s)",
#   [(1, 'John Smith', 'John Doe'),
#    (2, 'Jane Doe', 'Joe Dog'),
#    (3, 'Mike T.', 'Sarah H.')])
# # 如果沒有指定autocommit屬性為True的話就需要呼叫commit()方法
# conn.commit()

# 查詢操作
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

# 也可以使用for迴圈來迭代查詢結果
# for row in cursor:
#   print("ID=%d, Name=%s" % (row[0], row[1]))

# 關閉連線
conn.close()