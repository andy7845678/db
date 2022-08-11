import mysql.connector

connection = mysql.connector.connect(
        host = '127.0.0.1',
        port = '3306',
        user = 'root',
        password = 'a30812')

cursor = connection.cursor()

#創建資料庫
#cursor.execute("CREATE DATABASE `test`;")

#取得資料庫名稱
#cursor.execute("SHOW DATABASES;")
#records = cursor.fetchall()
#for r in records:
#        print(r)

#choose db
#cursor.execute('USE `test`;')

#創建表格
#cursor.execute("CREATE TABLE `REGION`(`region_id` INT PRIMARY KEY,`Region_name` VARCHAR(10));")

#cursor.execute("CREATE TABLE `USERS`(`user_id` INT PRIMARY KEY,`region_id` INT,FOREIGN KEY(`region_id`) REFERENCES `REGION`(`region_id`) ON DELETE SET NULL,`agent_id` INT ,`NAME` VARCHAR(20),`deposit` INT);")
#cursor.execute("ALTER TABLE `USERS` ADD FOREIGN KEY(`agent_id`) REFERENCES `USERS`(`user_id`) ON DELETE SET NULL;")


cursor.close()
connection.close()