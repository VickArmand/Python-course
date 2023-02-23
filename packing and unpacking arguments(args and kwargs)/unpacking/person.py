import json
class Person:
    def __init__(self,name,age,height,job):
        self.name = name
        self.age = age  
        self.height = height
        self.job= job
    def speak(self):
        print(f"I am {self.name} and i'm {self.age} years old height of {self.height} working as an {self.job}")
    
    def to_json(self):
        person_dict = {'name': self.name, 'age': self.age, 'height':self.height, 'job': self.job}
        return json.dumps(person_dict)
        # it is similar to
        # return json.dumps(self.__dict__)