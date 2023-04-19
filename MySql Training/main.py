import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="FKM,TMJz(rIQm:g", database="schooldb")

mydb = mydb

mycursor = mydb.cursor()

sql = "UPDATE student set classid=1"

mycursor.execute(sql)

mydb.commit()
