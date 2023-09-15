# map() is a function which takes two arguments:
# r = map(func, seq)
# The first argument func is the name of a function
# the second a sequence (e.g. a list) seq. 
# map() applies the function func to all the elements of the sequence seq.
squares = list(map(lambda x: x**2, range(10)))
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celsius, F)