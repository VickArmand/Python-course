my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = {'d': 4, 'e': 5, 'f': 6}
new_dict = {**my_dict, **my_dict2} #merge both elements
print(new_dict)