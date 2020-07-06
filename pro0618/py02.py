import pymssql

conn = pymssql.connect(server='127.0.0.1:1433', user='gjun', password='12345', database='pythondb', charset='utf8')
cursor = conn.cursor()

sql = """
IF OBJECT_ID('scores', 'U') IS NOT NULL
  DROP TABLE scores
  CREATE TABLE scores (
  id INT NOT NULL IDENTITY,
  name VARCHAR(20),
  chinese INT,
  english INT,
  math INT,
  PRIMARY KEY(id))"""

cursor.execute(sql)
conn.commit()
conn.close()

