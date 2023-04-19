import mysql.connector
from datetime import datetime

# Importing classes for creating objects from database records
from connection import mydb
from student import Student
from teacher import Teacher
from classes import Class


class Dbmaneger:
    def __init__(self):
        # Initialize database connection and cursor
        self.connection = mydb
        self.cursor = self.connection.cursor()

    def get_teachers(self):
        # Query database to get all teachers
        sql = "select * from teacher"
        self.cursor.execute(sql)
        try:
            # Create Teacher objects from database records and return them
            obj = self.cursor.fetchall()
            return Teacher.create_teacher(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def get_classes(self):
        # Query database to get all classes
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            # Create Class objects from database records and return them
            obj = self.cursor.fetchall()
            return Class.create_class(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def getstudent_byid(self, id):
        # Query database to get student with given id
        sql = "select * from student where id= %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            # Create Student object from database record and return it
            obj = self.cursor.fetchone()
            return Student.create_student(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def getstudents_byclass(self, classid):
        # Query database to get all students in the given class
        sql = "select *from student where classid=%s"
        value = (classid,)
        self.cursor.execute(sql, value)
        try:
            # Create Student objects from database records and return them
            obj = self.cursor.fetchall()
            return Student.create_student(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def getteacher_byid(self, id):
        # Query database to get teacher with given id
        sql = "select * from teacher where id=%s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            # Create Teacher object from database record and return it
            obj = self.cursor.fetchone()
            return Teacher.create_teacher(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def add_student(self, student: Student):
        # Insert new student record into database
        sql = "insert into student(studentnumber,name,surname,birthdate,gender,classid) values(%s,%s,%s,%s,%s,%s)"
        values = (student.studentnumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, values)
        try:
            # Commit changes to database
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error: ", err)

    def edit_student(self, student: Student):
        # Update student record in database
        sql = "update student set studentnumber = %s,name = %s,surname = %s,birthdate = %s,gender = %s,classid = %s where id = %s"
        values = (student.studentnumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql, values)
        try:
            # Commit changes to database
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error: ", err)

    def add_teacher(self, teacher: Teacher):
        """
        Adds a new row to the teacher table with the specified Teacher object.

        Parameters:
        -----------
        teacher : Teacher
            The Teacher object to be added to the table.
        """
        sql = "insert into teacher(branch,name,surname,birthdate,gender) values(%s,%s,%s,%s,%s)"
        values = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender)
        self.cursor.execute(sql, values)
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error: ", err)

    def edit_teacher(self, teacher: Teacher):
        """
        Updates the row in the teacher table with the specified Teacher object.

        Parameters:
        -----------
        teacher : Teacher
            The Teacher object to be updated in the table.
        """
        sql = "update teacher set branch = %s,name = %s,surname = %s,birthdate = %s,gender = %s where id = %s"
        values = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender, teacher.id)
        self.cursor.execute(sql, values)
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error: ", err)

    def __del__(self):
        """
        Closes the connection to the MySQL database.
        """
        self.connection.close()
        print("Db deleted")
