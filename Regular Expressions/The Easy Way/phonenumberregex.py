#!/usr/bin/python3
"""
This module is used to match whether a string is a phone number
the pattern: three numbers, a hyphen, three numbers, a hyphen, and four numbers.
Here’s an example: 415-555-4242.
"""
import re
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
phoneNumregex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumregex2 = re.compile(r"\d{3}-\d{3}-\d{4}")
# we compile inorder to store a Regex object in the variable
# The r before the first quote is to escape all backslashes
# instead of typing extra backslashes. Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.
matchObject1 = phoneNumregex1.search(message)
matchObject2 = phoneNumregex2.search(message)
print('Phone number found: ' + matchObject1.group())
print('Phone number found: ' + matchObject2.group())