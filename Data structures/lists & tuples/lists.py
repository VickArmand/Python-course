persons = ['tim','joe','rick','jason','metro','carter','simon']
# list iteration
for i in persons:
    print(i)
print("\n")
# The above loop is similar to this
for i in persons[:]:
    print(i) 
print("\n")  
print(persons[0])
print(persons[-1])
# slicing
print(persons[2:])
print(persons[2:4])