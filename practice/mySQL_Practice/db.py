import pymysql

conn = pymysql.connect(host="localhost", user="root", password="1234", db="mydb" ,charset="utf8")
curs = conn.cursor()
sql = "select * from user"

curs.execute(sql)
rows = curs.fetchall()
print(rows)

conn.close()