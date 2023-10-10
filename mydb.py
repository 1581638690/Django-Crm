import mysql.connector
dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="142511",
    auth_plugin="mysql_native_password"
)

cursorObject=dataBase.cursor()
cursorObject.execute("create database rzc")
print("ALL Done!")
