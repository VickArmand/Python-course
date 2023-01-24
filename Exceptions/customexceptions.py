class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("Enter your dog's name")
    if any(char.isdigit() for char in dogName):
        raise DogNameError
except DogNameError:
    print("Names shouldn't have numbers")