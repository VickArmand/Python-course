# The lambda operator or lambda function is a way to create small anonymous functions,
# i.e. functions without a name.
# These functions are throw-away functions, i.e. they are just needed where they have been created.
# Lambda functions are mainly used in combination with the functions filter(), map() and reduce().
# The general syntax of a lambda function is quite simple:
# lambda argument_list: expression
squares = []
for x in range(10):
    squares.append(x**2)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
print(squares)
def sum(x,y):
    return x + y
sum(3,4)
sum = lambda x, y : x + y
print(sum(3,4))
