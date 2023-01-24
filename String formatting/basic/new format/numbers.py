# Of course it is also possible to format numbers.
# Integers:
print('{:d}'.format(42))
# Floats:
print('{:f}'.format(3.141592653589793))
# Padding numbers
# Similar to strings numbers can also be constrained to a specific width.
print('{:4d}'.format(42))
# Again similar to truncating strings the precision for floating point numbers limits the number of positions after the decimal point.
# For floating points the padding value represents the length of the complete output. In the example below we want our output to have at least 6 characters with 2 after the decimal point.
print('{:06.2f}'.format(3.141592653589793))
# For integer values providing a precision doesn't make much sense and is actually forbidden in the new style (it will result in a ValueError).
print('{:04d}'.format(42))