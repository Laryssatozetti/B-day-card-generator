#Write a program that displays available commands upon launch. The commands are: create, manage, end.

students = []
teachers = []
homeroom_teachers = []


# Create Users

def create_user():
    while True:
        print("\nCreate: student | teacher | homeroom teacher | end")
        option = input("Option: ").lower()

        if option == "student":
            first = input("First name: ")
            last = input("Last name: ")
            class_name = input("Class (ex: 3C): ")
            students.append(Student(first, last, class_name))
            print("Student created.")

        elif option == "teacher":
            first = input("First name: ")
            last = input("Last name: ")
            subject = input("Subject: ")

            classes = []
            while True:
                class_name = input("Class (empty to finish): ")
                if class_name == "":
                    break
                classes.append(class_name)

            teachers.append(Teacher(first, last, subject, classes))
            print("Teacher created.")

        elif option == "homeroom teacher":
            first = input("First name: ")
            last = input("Last name: ")
            class_name = input("Class they lead: ")
            homeroom_teachers.append(HomeroomTeacher(first, last, class_name))
            print("Homeroom teacher created.")

        elif option == "end":
            break

        else:
            print("Invalid option.")


# Manage Users

def manage_users():
    while True:
        print("\nManage: class | student | teacher | homeroom teacher | end")
        option = input("Option: ").lower()

        if option == "class":
            class_name = input("Class name: ")

            print("\nStudents:")
            for student in students:
                if student.class_name == class_name:
                    print(student.first_name, student.last_name)

            print("Homeroom teacher:")
            found = False
            for ht in homeroom_teachers:
                if ht.class_name == class_name:
                    print(ht.first_name, ht.last_name)
                    found = True
            if not found:
                print("None")

        elif option == "student":
            first = input("First name: ")
            last = input("Last name: ")
            student = find_student(first, last)

            if student is None:
                print("Student not found.")
            else:
                print("Class:", student.class_name)
                print("Teachers:")
                for teacher in teachers:
                    if student.class_name in teacher.classes:
                        print(teacher.first_name, teacher.last_name)

        elif option == "teacher":
            first = input("First name: ")
            last = input("Last name: ")
            teacher = find_teacher(first, last)

            if teacher is None:
                print("Teacher not found.")
            else:
                print("Classes:")
                for class_name in teacher.classes:
                    print(class_name)

        elif option == "homeroom teacher":
            first = input("First name: ")
            last = input("Last name: ")
            ht = find_homeroom_teacher(first, last)

            if ht is None:
                print("Homeroom teacher not found.")
            else:
                print("Students:")
                for student in students:
                    if student.class_name == ht.class_name:
                        print(student.first_name, student.last_name)

        elif option == "end":
            break

        else:
            print("Invalid option.")



#'student': Prompt for the student's first and last name (as one or two variables, depending on your design) and the class name (e.g., "3C").

class Student:
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

#'teacher': Prompt for the teacher's first and last name (as one or two variables, depending on your design), the subject they teach, and the names of the classes they teach, until an empty line is entered.

class Teacher:
    def __init__(self, first_name, last_name, subject, classes):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.classes = classes

#'homeroom teacher': Prompt for the homeroom teacher's first and last name (as one or two variables, depending on your design), and the name of the class they lead.

class HomeroomTeacher:
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name



# Helper Functions


def find_student(first_name, last_name):
    for student in students:
        if student.first_name == first_name and student.last_name == last_name:
            return student
    return None


def find_teacher(first_name, last_name):
    for teacher in teachers:
        if teacher.first_name == first_name and teacher.last_name == last_name:
            return teacher
    return None


def find_homeroom_teacher(first_name, last_name):
    for ht in homeroom_teachers:
        if ht.first_name == first_name and ht.last_name == last_name:
            return ht
    return None


def main():
    while True:
        print("\nCommands: create | manage | end")
        command = input("Command: ").lower()

        if command == "create":
            create_user()
        elif command == "manage":
            manage_users()
        elif command == "end":
            print("Program ended.")
            break
        else:
            print("Invalid command.")

main()