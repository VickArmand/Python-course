# The first parameter in the definition of a method has to be a reference to the instance, which called the method. This parameter is usually called "self".
# We want to define the attributes of an instance right after its creation. __init__ is a method which is immediately and automatically called after an instance has been created. 
# the method __del__. It is called when the instance is about to be destroyed and if there is no other reference to this instance. If a base class has a __del__() method, the derived class's __del__() method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance.
class A:
    def __init__(self):
        print("__init__ has been executed!")
x = A()
class Robot():
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print ("Robot has been destroyed")
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    # The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
    del y
# The usage of the __del__ method is very problematic. If we change the previous code to personalize the deletion of a robot, we create an error because We are accessing an attribute which doesn't exist anymore.
class Robot():
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print (self.name + " says bye-bye!")
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y