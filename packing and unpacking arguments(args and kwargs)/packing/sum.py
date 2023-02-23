def add_numbers(*args):
  total = 0
  for num in args:
    total += num
  return total
print(add_numbers(5,4,3,2,1,0))
values = [4,5,6,7]
values2 = [20,45,67]
print(add_numbers(*values, *values2))