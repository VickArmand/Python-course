#!/usr/bin/python3
import re
"""
The | character is called a pipe. You can use it anywhere you want to match one
of many expressions. For example, the regular expression r'Batman|Tina Fey'
will match either 'Batman' or 'Tina Fey'.
"""
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group())
# If you need to match an actual pipe character,
# escape it with a back­slash, like \|.