#!/usr/bin/python3
from teacher import Teacher
student = __import__("student").Student
teacher1 = Teacher("Cynthia", "Cynthia Tuva", "cynthia@gmail.com", 443,35)
print(dir(teacher1))
print(teacher1)
student1 = student("Cynthia", "Cynthia Tuva", "cynthia@gmail.com", 443,20)
print(student1)
