from student_course import *
from GUI import showMenuOptions
import os

def main():

    students = []
    courses = []

    first_time = True

    while True:

        if not first_time:
            os.system("cls")
        else:
            print("Welcome to the Student Course Enrollment System!")
            first_time = False

        showMenuOptions()
        op = input("Option: ")

        os.system("cls")

        if op == '1':
            AddStudent(students)
        elif op == '2':
            AddCourse(courses)
        elif op == '3':
            EnrollStudents(students, courses)
        elif op == '4':
            ViewStudendCourses(students)
        elif op == '5':
            ViewCourseStudents(courses)





def AddStudent(students):
    print("Adding student!")

    student_name = input("Name: ")
    student_age = int(input("Age: "))

    students.append(Student(student_name, student_age))


def AddCourse(courses):
    print("Adding course!")

    courses.append(Course(input("Name: ")))


def EnrollStudents(students, courses):
    print("Enrolling students into courses")

    while True:

        print("\nCourses:")

        for i, course in enumerate(courses):
            print(f"{i+1} {course.name}")

        print("0 to exit")
        course = int(input("\nSelect course id: "))

        if 0 > course > len(courses):
            print("Non-existant id!")
            continue

        break

    if course == 0:
        return None

    while True:

        print("\nStudents:")

        for i, student in enumerate(students):
            print(f"{i+1} {student.name}")

        print("0 to exit")
        student = int(input("\nSelect student id: "))

        if 0 > student > len(students):
            print("Non-existant id!")
            continue
        elif student == 0:
            return None

        courses[course-1].addStudent(students[student-1])
        students[student-1].addCourse(courses[course-1])
        print(
            f"{students[student-1].name} was added to {courses[course-1].name}")


def ViewStudendCourses(students):
    for i, stu in enumerate(students):
        print(f"{i+1} {stu.name}")

    st = int(input("Select student id: "))

    for i, cor in enumerate(students[st-1].getCourses()):
        print(cor.name)

    input(("Press Enter"))


def ViewCourseStudents(courses):
    for i, cor in enumerate(courses):
        print(f"{i+1} {cor.name}")

    st = int(input("Select course id: "))

    for i, stu in enumerate(courses[st-1].getStudents()):
        print(stu.name)

    input(("Press Enter"))


if __name__ == "__main__":
    main()
