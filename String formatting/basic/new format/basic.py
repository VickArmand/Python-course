# Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate.
# Since the elements are not represented by something as descriptive as a name this simple style should only be used to format a relatively small number of elements.
def pyintro():
    print('{} {}'.format('one', 'two'))
    print('{} {}'.format(1, 2))
pyintro()
# With new style formatting it is possible (and in Python 2.6 even mandatory) to give placeholders an explicit positional index.
# This allows for re-arranging the order of display without changing the arguments.
# This operation is not available with old-style formatting.
print('{1} {0}'.format('one', 'two'))