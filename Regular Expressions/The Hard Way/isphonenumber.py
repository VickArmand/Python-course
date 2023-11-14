#!/usr/bin/python3
def isPhoneNumber(text):
    """
    This function is used to match whether a string is a phone number
    the pattern: three numbers, a hyphen, three numbers, a hyphen, and four numbers.
    Here’s an example: 415-555-4242.
    """
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
"""
The above function uses a lot of code to do something limited.
The isPhoneNumber() function is 17 lines but can find only one pattern of phone numbers.
What about a phone number formatted like 415.555.4242 or (415) 555-4242?
What if the phone number had an extension, like 415-555-4242 x99?
The isPhoneNumber() function would fail to validate them.
You could add yet more code for these additional patterns, but there is an easier way which is regex.
"""