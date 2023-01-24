# Both formatting styles support named placeholders.
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))
# .format() also accepts keyword arguments.
# This operation is not available with old-style formatting.
print('{first} {last}'.format(first='Hodor', last='Hodor!'))