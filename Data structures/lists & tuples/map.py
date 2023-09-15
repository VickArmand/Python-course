# map() is a function which takes two arguments:
# r = map(func, seq)
# The first argument func is the name of a function
# the second a sequence (e.g. a list) seq. 
# map() applies the function func to all the elements of the sequence seq.
squares = list(map(lambda x: x**2, range(10)))
