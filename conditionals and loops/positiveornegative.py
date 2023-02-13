#!/usr/bin/python3
num = input("Enter a number: ")
if (int(num) < 0):
    print(f"{num} is Negative")
elif (int(num) > 0):
    print(f"{num} is Positive")
else:
    print(f"{num} is Zero")
