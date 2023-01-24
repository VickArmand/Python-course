# New style formatting allows even greater flexibility in accessing nested data structures.
# It supports accessing containers that support __getitem__ like for example dictionaries and lists:
# This operation is not available with old-style formatting.
person = {'first': 'Jean-Luc', 'last': 'Picard'}
print('{p[first]} {p[last]}'.format(p=person))
data = [4, 8, 15, 16, 23, 42]
print('{d[4]} {d[5]}'.format(d=data))
# As well as accessing attributes on objects via getattr():
# This operation is not available with old-style formatting.
class Plant(object):
    type = 'tree'
print('{p.type}'.format(p=Plant()))
# Both type of access can be freely mixed and arbitrarily nested:
# This operation is not available with old-style formatting.
class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]
print('{p.type}: {p.kinds[0][name]}'.format(p=Plant()))