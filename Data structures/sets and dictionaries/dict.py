# Dictionary is made up of key pair values
person = { 
          'name' : 'Hector',
          'age' : 15, 
          'country': 'Kenya'
          }
person['occupation'] = 'Software Engineer'
for key, value in person.items():
    print(f"{key} :{value}")
for key in person.keys():
    print(key)
print("\n")
person['occupation'] = 'Entrepreneur'
# The pop() method removes the item associated with the specified key from the dictionary and returns its value.
# You can pass a second argument as a default value to pop().
# If the specified key doesn't exist, this value is returned, and the dictionary remains unchanged.
person.pop('occupation')
person.pop('k4', None)
for values in person.values():
    print(values)
# Accessing dictionary values
print(person['name'])