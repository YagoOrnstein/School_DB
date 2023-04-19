from dbmaneger import Dbmaneger
from student import Student
from teacher import Teacher


class App:
    def __init__(self):
        self.db = Dbmaneger()

    def display_classes(self):
        classes = self.db.get_classes()
        for i in classes:
            print(f"{i.id}: {i.name}")

    def display_students(self):
        self.display_classes()
        classid = input("Which Class: ")

        students = self.db.getstudents_byclass(int(classid))
        print("Student List")
        for std in students:
            print(f"{std.id}-{std.name} {std.surname}")
        return classid

    def add_student(self):
        self.display_classes()
        number = input("Student Number: ")
        name = input("Name: ")
        surname = input("Surname: ")
        birthdate = input("Birthdate(YYYY-MM-DD): ")
        gender = input("Gender(M/W): ")
        classid = int(input("Which Class: "))
        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.add_student(student)

    def display_teachers(self):
        teachers = self.db.get_teachers()
        print("Teacher List")
        for i in teachers:
            print(f"{i.id}-{i.name} {i.surname}: {i.branch}")

    def add_teacher(self):
        name = input("Name: ")
        surname = input("Surname: ")
        birthdate = input("Birthdate(YYYY-MM-DD): ")
        gender = input("Gender(M/W): ")
        branch = input("Which Branch: ")
        teacher = Teacher(None, branch, name, surname, birthdate, gender)
        self.db.add_teacher(teacher)

    def updating_student(self):
        self.display_students()
        studentid = int(input("Choose id: "))
        student = self.db.getstudent_byid(studentid)
        print(student[0].id, student[0].name, student[0].surname, student[0].birthdate, student[0].gender, student[0].classid)
        student[0].name = input("Update Name: ") or student[0].name
        student[0].surname = input("Update Surname: ") or student[0].surname
        student[0].birthdate = input("Update Birthdate(YYYY-MM-DD): ") or student[0].birthdate
        student[0].gender = input("Update Gender: ") or student[0].gender
        student[0].classid = input("Update Class: ") or student[0].classid
        self.db.edit_student(student[0])

    def updating_teacher(self):
        self.display_teachers()
        teacherid = int(input("Choose id: "))
        teacher = self.db.getteacher_byid(teacherid)
        print(teacher[0].id, teacher[0].name, teacher[0].surname, teacher[0].birthdate, teacher[0].gender, teacher[0].branch)
        teacher[0].name = input("Update Name: ") or teacher[0].name
        teacher[0].surname = input("Update Surname: ") or teacher[0].surname
        teacher[0].birthdate = input("Update Birthdate(YYYY-MM-DD): ") or teacher[0].birthdate
        teacher[0].gender = input("Update Gender: ") or teacher[0].gender
        teacher[0].branch = input("Update Class: ") or teacher[0].branch
        self.db.edit_teacher(teacher[0])
        self.display_teachers()

    def init_app(self):
        msg = "*****\n*****\n1-Student List\n2-Add Student\n3-Update Student\n4-Add Teacher\n5-Update Teacher\n6-Exit(Q)"
        while True:
            print(msg)
            choice = input("Choice: ")
            if choice == "1":
                self.display_students()
            elif choice == "2":
                self.add_student()
            elif choice == "3":
                self.updating_student()
            elif choice == "4":
                self.add_teacher()
            elif choice == "5":
                self.updating_teacher()
            elif choice == "6":
                quit = input("Are you sure?")
                if quit == "q":
                    break
                else:
                    continue
            else:
                print("Wrong choice")


App().init_app()
