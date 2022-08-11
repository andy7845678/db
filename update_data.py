import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1',
                                    port='3306',
                                    user='root',
                                    password='a30812',
                                    database='test')

cursor = connection.cursor()

# 新增REGION資料
#cursor.execute("INSERT INTO `REGION` VALUES(1, 'USA')")
#cursor.execute("INSERT INTO `REGION` VALUES(2, 'UK')")
#cursor.execute("INSERT INTO `REGION` VALUES(3, 'AUS')")
#cursor.execute("INSERT INTO `REGION` VALUES(4, 'TH')")

#新增USERS資料
#cursor.execute("INSERT INTO `USERS` VALUES(1,1,NULL,'Dustin',100000)")
#cursor.execute("INSERT INTO `USERS` VALUES(2,1,1,'Ben',100000)")
#cursor.execute("INSERT INTO `USERS` VALUES(3,1,1,'Allen',90000)")
#cursor.execute("INSERT INTO `USERS` VALUES(4,2,NULL,'Kate',250000)")
#cursor.execute("INSERT INTO `USERS` VALUES(5,2,NULL,'Leo',200000)")
#cursor.execute("INSERT INTO `USERS` VALUES(6,1,NULL,'Jessica',90000)")

#寫入USERS的foreign key
#cursor.execute("UPDATE `USERS` SET `agent_id` = 5 WHERE `user_id` = 4")
#cursor.execute("UPDATE `USERS` SET `agent_id` = 5 WHERE `user_id` = 6")

cursor.close()
connection.commit()
connection.close()