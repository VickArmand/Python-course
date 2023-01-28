class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
'''
To use inheritance, we specify the base class names in a tuple following the class name in the class definition (for example, class Teacher(SchoolMember)). Next, we observe that the __init__ method of the base class is explicitly called using the self variable so that we can initialize the base class part of an instance in the subclass. This is very important to remember- Since we are defining a __init__ method in Teacher and Student subclasses, Python does not automatically call the constructor of the base class SchoolMember, you have to explicitly call it yourself.
In contrast, if we have not defined an __init__ method in a subclass, Python will call the constructor of the base class automatically.
While we could treat instances of Teacher or Student as we would an instance of SchoolMember and access the tell method of SchoolMember by simply typing Teacher.tell or Student.tell, we instead define another tell method in each subclass (using the tell method of SchoolMember for part of it) to tailor it for that subclass. Because we have done this, when we write Teacher.tell Python uses the tell method for that subclass vs the superclass. However, if we did not have a tell method in the subclass, Python would use the tell method in the superclass. Python always starts looking for methods in the actual subclass type first, and if it doesnt find anything, it starts looking at the methods in the subclasss base classes, one by one in the order they are specified in the tuple (here we only have 1 base class, but you can have multiple base classes) in the class definition.
A note on terminology - if more than one class is listed in the inheritance tuple, then it is called multiple inheritance.
The end parameter is used in the print function in the superclass's tell() method to print a line and allow the next print to continue on the same line. This is a trick to make print not print a \n (newline) symbol at the end of the printing.'''