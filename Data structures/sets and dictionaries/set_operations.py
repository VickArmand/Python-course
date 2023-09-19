#!/usr/bin/python3
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
print(set_1 & set_2)
print(set_1.intersection(set_2))
print(set_1 ^ set_2)
print(set_1.symmetric_difference(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))
print(set_1.difference_update(set_2))