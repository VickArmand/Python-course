# Inverse to padding it is also possible to truncate overly long values to a specific number of characters.
# The number behind a . in the format specifies the precision of the output. For strings that means that the output is truncated to the specified length. In our example this would be 5 characters.
print('%.5s' % ('xylophone',))