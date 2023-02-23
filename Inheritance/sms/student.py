#!/usr/bin/python3
user = __import__("user").User
from user import User
class Student(user):
    def __init__(self,username,name,email,reg_no,age):
        super().__init__(username,name,email,age)
        self.reg_no = reg_no
    def __str__(self):
        return f"Hi There My name is {self.name} and i'm a student of {self._User__age}"
    

        