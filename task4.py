class Teacher:              #polymorphism
    def work(self):
        print("Teacher teaches students")


class Doctor:
    def work(self):
        print("Doctor treats patients")


teacher = Teacher()
doctor = Doctor()

teacher.work()
doctor.work()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myname(self):
        print("My name is", self.name)


class Student(Person):
    def study(self):
        print("I am studying")


student = Student("areesha", 21)

student.myname()
student.study()