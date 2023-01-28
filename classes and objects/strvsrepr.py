# str() and repr() both are used to get a string representation of object.

s = 'Hello, Geeks.'
print (str(s))
print (str(2.0/11.0))
print (repr(s))
print (repr(2.0/11.0))
# From above output, we can see if we print string using repr() function then it prints with a pair of quotes and if we calculate a value we get more precise value than str() function.
# Following are differences:
    # str() is used for creating output for end user while repr() is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable. For example, if we suspect a float has a small rounding error, repr will show us while str may not.
    # repr() compute the “official” string representation of an object (a representation that has all information about the object) and str() is used to compute the “informal” string representation of an object (a representation that is useful for printing the object).
    # The print statement and str() built-in function uses __str__ to display the string representation of the object while the repr() built-in function uses __repr__ to display the object.
    
import datetime
today = datetime.datetime.now()
  
# Prints readable format for date-time object
print (str(today))
  
# prints the official format of date-time object
print (repr(today)) 

# A user defined class should also have a __repr__ if we need detailed information for debugging. And if we think it would be useful to have a string version for users, we create a __str__ function.

# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes
  
# A user defined class to represent Complex numbers
class Complex:
  
    # Constructor
    def __init__(self, real, imag):
       self.real = real
       self.imag = imag
  
    # For call to repr(). Prints object's information
    def __repr__(self):
       return 'Rational(%s, %s)' % (self.real, self.imag)    
  
    # For call to str(). Prints readable form
    def __str__(self):
       return '%s + i%s' % (self.real, self.imag)    
  
  
# Driver program to test above
t = Complex(10, 20)
  
# Same as "print t"
print (str(t))  
print (repr(t))
# If you apply str or repr to an object, Python is looking for a corresponding method __str__ or __repr__ in the class definition of the object. If the method does exist, it will be called otherwise Python uses the default output for the object.
# A frequently asked question is when to use __repr__ and when __str__. __str__ is always the right choice, if the output should be for the end user or in other words, if it should be nicely printed. __repr__ on the other hand is used for the internal representation of an object.