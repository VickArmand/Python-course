# By default only negative numbers are prefixed with a sign. This can be changed of course.
print('{:+d}'.format(42))
# Use a space character to indicate that negative numbers should be prefixed with a minus symbol and a leading space should be used for positive ones.
print('{: d}'.format((- 23)))
print('{: d}'.format(42))
# New style formatting is also able to control the position of the sign symbol relative to the padding.
# This operation is not available with old-style formatting.
print('{:=5d}'.format((- 23)))
print('{:=+5d}'.format(23))