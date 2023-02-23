#!/usr/bin/python3
user = __import__("user").User 
from user import User
# A process in which any given identifier with one trailing underscore and two leading underscores is textually replaced with the __ClassName__Identifier is known as Name mangling. In __ClassName__Identifier name, ClassName is the name of current class where identifier is present.
class Teacher(user):
    def __init__(self,username,name,email,staff_no, age):
        super().__init__(username,name,email,age)
        self.staff_no = staff_no
    def __str__(self):
        return f"Hi There My name is {self.name} and i'm a teacher and i'm {self._User__age} years old"
    

        