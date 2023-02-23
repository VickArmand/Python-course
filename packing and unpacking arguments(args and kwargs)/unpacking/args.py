#Supposing 1, 2, 3, 4, 5 are going to be function parameters
# We want to add these numbers
values = (1, 2, 3, 4, 5)
 
def add_numbers(*args):
  total = 0
  for num in args:
    total += num
  return total
 
print(add_numbers(*values))
# if we called the function like this :
# print(add_numbers(values))
# It will result in an error because we passed the whole tuple into the function call. It will result in the value of args being a tuple inside a tuple.
# When we iterate over args, we will get a tuple, and we cannot perform += operation with an integer (total) and a tuple (num).
# Therefore to counteract this, Both * and ** operators are used for unpacking argument values from a tuple and a dictionary, respectively.