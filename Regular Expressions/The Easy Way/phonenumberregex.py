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
"""
Say you want to separate the area code from the rest of the phone number.
Adding parentheses will create groups in the regex:
"""
groupedRegex = re.compile(r"(\d{3})-(\d{3}-\d{4})")
groupMatchObject = groupedRegex.search(message)
# The first set of parentheses in a regex string will be group 1.
# The second set will be group 2.
# By passing the integer 1 or 2 to the group() match object method,
# you can grab different parts of the matched text.
# Passing 0 or nothing to the group() method will return the entire matched text.
# To retrieve all groups at once use groups()
print('Phone number found: ' + groupMatchObject.group(1))
print('Phone number found: ' + groupMatchObject.group(2))
print('Phone number found: ' + groupMatchObject.group(0))
print(groupMatchObject.groups())
# Parentheses have a special meaning in regular expressions,
# but what do you do if you need to match a parenthesis in your text?
# For instance, maybe the phone numbers you are trying to match have the area code set in parentheses.
# In this case, you need to escape the ( and ) characters with a back­slash.
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)