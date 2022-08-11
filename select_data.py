import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1',
                                    port='3306',
                                    user='root',
                                    password='a30812',
                                    database='test')

cursor = connection.cursor()

# 取得部門表格所有資料
#cursor.execute("SELECT * FROM `USERS`;")

#records = cursor.fetchall()
#for r in records:
#    print(r)


#Q1
#cursor.execute("SELECT `NAME`FROM `USERS`WHERE `user_id` IN(SELECT `user_id`FROM `USERS`WHERE `deposit` > any(SELECT `deposit`FROM `USERS`WHERE `user_id` IN(SELECT `agent_id`FROM `USERS`WHERE `agent_id` != 0))AND `agent_id` != 0);")
#records = cursor.fetchall()
#for r in records:
#    print(r)

#Q2
#cursor.execute("SELECT `NAME` FROM `USERS` WHERE `region_id` = 1 AND `deposit` = (SELECT MAX(`deposit`) FROM `USERS` WHERE `region_id` = 1);")
#records = cursor.fetchall()
#for r in records:
#    print(r)
#cursor.execute("SELECT `NAME` FROM `USERS` WHERE `region_id` = 2 AND `deposit` = (SELECT MAX(`deposit`) FROM `USERS` WHERE `region_id` = 2);")
#records = cursor.fetchall()
#for r in records:
#    print(r)
#Q3
cursor.execute("SELECT * FROM `USERS` WHERE `deposit` >= (SELECT `deposit` FROM `USERS` ORDER BY `deposit` DESC LIMIT 2,1) ORDER BY `deposit` DESC;")
records = cursor.fetchall()
for r in records:
    print(r)


cursor.close()
connection.close()