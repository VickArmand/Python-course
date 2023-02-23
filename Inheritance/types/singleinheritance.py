#!/usr/bin/python3
"""
This example shows the essence of single inheritance 
"""
class ParentClass:
    first = 'a'
    second = 'b'
    third = 'c'

    def __init__(self,name)-> None:
        self.name = name
class SubClass(ParentClass):
    def express(self)->None:
        print(f"{self.name} has {self.first}, {self.second} {self.third} stuff")

person1 = SubClass("Philip")
print(person1.express())