import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="FKM,TMJz(rIQm:g", database="schooldb")


# try:
#     mydb.commit()
#     print(f"{mycursor.rowcount}")
# except mysql.connector.Error as err:
#     print("Error: ", err)
# finally:
#     mydb.close()