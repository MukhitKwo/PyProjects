class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = set()

    def addCourse(self, course):
        self.courses.add(course)

    def getCourses(self):
        return self.courses


class Course:

    def __init__(self, name):
        self.name = name
        self.students = set()

    def addStudent(self, student):
        self.students.add(student)

    def getStudents(self):
        return self.students
