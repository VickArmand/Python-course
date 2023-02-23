#!/usr/bin/env python3
class User:
    def __init__(self,username,name,email,age):
        self.username = username
        self.name = name
        self.email = email
        self.__age = age
    def __str__(self):
        return f"Hi There My name is {self.name} and i'm {self.__age} years old"
    