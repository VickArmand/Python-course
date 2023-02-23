class Person:
    def __init__(self,name,age,height,job):
        self.name = name
        self.age = age
        self.height = height
        self.job= job
    def speak(self):
        print(f"I am {self.name} and i'm {self.age} years old height of {self.height} working as an {self.job}")