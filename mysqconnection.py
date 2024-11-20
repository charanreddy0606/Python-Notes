import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",port='3306')


print("connected",conn)
cursor=conn.cursor()
print(conn.is_connected())
