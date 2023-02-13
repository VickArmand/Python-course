#!/usr/bin/python3
import modules
# the above code is similar to from modules import add,sub
arith =__import__('modules').add
# this code means we are importing add function from modules
print(modules.add(3,4))
print(modules.sub(10,7))
print(arith(2,6))