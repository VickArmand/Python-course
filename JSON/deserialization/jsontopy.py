#!/usr/bin/python3
import json
name = {'id': 1, 'name': 'Patrick Swayze', 'job': 'Artist'}
name = json.dumps(name)
print(name)
print(type(name))
name = json.loads(name)#converts from json to py dictionary
print(name)

