# These methods are of course the getter for retrieving the data and the setter for changing the data. 
# According to this principle, the attributes of a class are made private to hide and protect them.
class P:
    def __init__(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
p1 = P(42)
p2 = P(4711)
p1.get_x()
p1.set_x(47)
p1.set_x(p1.get_x()+p2.get_x())
print(p1.get_x())
class P:
    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
# A method which is used for getting a value is decorated with "@property", i.e. we put this line directly in front of the header. 
# The method which has to function as the setter is decorated with "@x.setter". If the function had been called "f", we would have to decorate it with "@f.setter".
class P:
    def __init__(self, x):
        self.__set_x(x)
    def __get_x(self):
        return self.__x
    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(__get_x, __set_x)