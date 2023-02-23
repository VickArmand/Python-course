#!/usr/bin/python3
import json
name = {'id': 1, 'name': 'Patrick Swayze', 'job': 'Artist'}
print(type(name))
print(name)
name = json.dumps(name) #produces a string
print(name)
print(type(name))