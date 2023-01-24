# By default values are formatted to take up only as many characters as needed to represent the content. It is however also possible to define that a value should be padded to a specific length.
# Unfortunately the default alignment differs between old and new style formatting. The old style defaults to right aligned while for new style it's left.
# Align right:
print('{:>10}'.format('test'))
# Align left
print('{:10}'.format('test'))
# Again, new style formatting surpasses the old variant by providing more control over how values are padded and aligned.
# You are able to choose the padding character:
# This operation is not available with old-style formatting.
print('{:_<10}'.format('test'))
# And also center align values:
# This operation is not available with old-style formatting.
print('{:^10}'.format('test')) 
# When using center alignment where the length of the string leads to an uneven split of the padding characters the extra character will be placed on the right side:
# This operation is not available with old-style formatting.
print('{:^6}'.format('zip'))
