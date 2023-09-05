# A for or while loop can include an else clause.
# In a for loop, the else clause is executed after the loop reaches its final iteration.
# In a while loop, it’s executed after the loop’s condition becomes false.
# In either kind of loop, the else clause is not executed if the loop was terminated by a break.
# (Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')