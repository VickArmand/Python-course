# By default values are formatted to take up only as many characters as needed to represent the content. It is however also possible to define that a value should be padded to a specific length.
# Unfortunately the default alignment differs between old and new style formatting. The old style defaults to right aligned while for new style it's left.
# Align right:
print('%10s' % ('test',))
# Align left
print('%-10s' % ('test',))