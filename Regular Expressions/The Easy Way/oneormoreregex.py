#!/usr/bin/python3
import re
"""
The + (or plus) means “match one or more"
"""
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1 == None)
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
# The regex Bat(wo)+man will not match the string 'The Adventures of Batman'
# because at least one wo is required by the plus sign.
# If you need to match an actual plus sign character, prefix the plus sign with a backslash to escape it: \+.