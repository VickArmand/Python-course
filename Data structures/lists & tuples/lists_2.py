persons = ['tim','joe','rick','jason','metro','carter','simon']
persons_2= ['rita','faith','josh']
# concatenation
new_persons = persons + persons_2
print(new_persons)
# append
persons.append('victor')
print(persons)
# insert - adds an element at a specific index
# it takes in 2 parameters where the first one is the index and the second is the value to be added
persons_2.insert(1,'Victoria')
print(persons_2)
# remove- Deletes first occurrence of value.
persons.remove('rick')
print(persons)
# pop - Remove and return item at index (default last).
persons_2.pop(2) # removes value at second postion
n =persons_2.pop() # removes the last value
print(persons_2, n)