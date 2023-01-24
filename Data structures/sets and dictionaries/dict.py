# Dictionary is made up of key pair values
person = { 
          'name' : 'Hector',
          'age' : 15, 
          'country': 'Kenya'
          }
for key, value in person.items():
    print(f"{key} :{value}")
for key in person.keys():
    print(key)
print("\n")
for values in person.values():
    print(values)
# Accessing dictionary values
print(person['name'])