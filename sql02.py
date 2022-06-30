import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password=''
)

cursor = conn.cursor()
cursor.execute('SHOW DATABASES')

for dados in cursor:
    print(dados)