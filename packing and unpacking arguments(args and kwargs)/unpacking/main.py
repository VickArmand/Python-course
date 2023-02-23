#!usr/bin/env python3
from person import Person

def create_person(**person_details):
    person = Person(person_details['name'], person_details['age'],person_details['height'], person_details['job'])
    person.speak()
    print(person.to_json())
details = {'name': 'Jordan Carter', 'height': 189, 'job': 'Artist','age': 27}
create_person(**details)
create_person(name = 'Tobi', age = 30, height = 169, job = 'Engineer')
