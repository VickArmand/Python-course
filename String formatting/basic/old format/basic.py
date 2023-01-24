# Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate.
# Since the elements are not represented by something as descriptive as a name this simple style should only be used to format a relatively small number of elements.
def pyintro():
    print('%s %s' % ('one', 'two'))
    print('%d %d' % (1, 2))
pyintro()