import mysql.connector
# coding=utf8
# 获取数据库连接
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="root",  # 数据库密码
    database='pythonDB',

)
myCursor = mydb.cursor()
# myCursor.execute('create database pythonDB')
# myCursor.execute('show databases')
for i in myCursor:
    print(i)

# 创建表
# myCursor.execute('create table test(name varchar(255), age int)')
myCursor.execute('show tables')

for i in myCursor:
    print(i)
print(type(myCursor))

# 插入数据
# sql = "insert into test value('张三',2)"
# myCursor.execute(sql)
# mydb.commit()
# myCursor.execute('select * from test')
# for i in myCursor:
#     print(i)

# 插入多条数据
sql1 = "INSERT INTO test VALUES (%s, %s)"
val = [
    ("张三", '22'),
    ('李四', '23'),
    ('王五', '32'),
    ('周六', '12')
]

myCursor.executemany(sql1, val)
mydb.commit()
print(myCursor.rowcount)