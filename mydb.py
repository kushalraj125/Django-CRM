import mysql.connector

import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='1234'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrmdata")


print("Connected!")
