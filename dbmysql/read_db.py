import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='student',
                     charset='utf8')

cur = db.cursor()
sql = "select name,score from class1 order by score desc;"
cur.execute(sql)   #执行语句

#cur 可迭代对象(每一个都是一个元组）
# for i in cur:
#     print(i)
#获取一个结果
print(cur.fetchone())
print("======================================================")
#获取多个结果
print(cur.fetchmany(3))
print("======================================================")
print(cur.fetchall())

cur.close()
db.close()

