import mysql.connector

connection = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = 'a30812')

cursor = connection.cursor()

#創建資料庫
#cursor.execute("CREATE DATABASE `tt`;")

#取得資料庫名稱
#cursor.execute("SHOW DATABASES;")
#records = cursor.fetchall()
#for r in records:
#        print(r)

#choose db
cursor.execute('USE `sql_tutorial`;')

#創建表格
cursor.execute('CREATE TABLE `tt`(tt INT);')


cursor.close()
connection.close()