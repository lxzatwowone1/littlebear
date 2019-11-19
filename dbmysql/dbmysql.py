import pymysql

db = pymysql.connect(host='localhost',port=3306,user='root',passwd="123456",database="student",charset="utf8")

#生成游标对象(用于操作数据库数据,获取sql执行结果的对象）
cur = db.cursor()

#执行sql语句
cur.execute("delete from class1 where sex = 'f';")
db.commit()
excep
cur.close()
db.close()