#!/usr/bin/python3
import re
"""
f you have a group that you want to repeat a specific number of times, fol-
low the group in your regex with a number in curly brackets. For example,
the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa',
since the latter has only two repeats of the (Ha) group.

Instead of one number, you can specify a range by writing a minimum,
a comma, and a maximum in between the curly brackets.
For example, the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
You can also leave out the first or second number in the curly brackets
to leave the minimum or maximum unbounded.
For example, (Ha){3,} will match three or more instances of the (Ha) group,
while (Ha){,5} will match zero to five instances.
"""
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)
# Here, (Ha){3} matches 'HaHaHa' but not 'Ha'. Since it doesn’t match 'Ha', search() returns None.
# Python’s regular expressions are greedy by default, which means that in
# ambiguous situations they will match the longest string possible
# The non-greedy version of the curly brackets, which matches the shortest string possible,
# has the closing curly bracket followed by a question mark.
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())