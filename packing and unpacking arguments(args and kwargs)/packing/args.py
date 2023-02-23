# A Python program to demonstrate packing
# All arguments passed to fun2 are packed into tuple *args.
def fun2(*args):
    # Accessing the elements just like we access then from a tuple
    print(args[0])
 
    # Convert args tuple to a list so we can modify it
    args = list(args)
 
    # Modifying args
    args[0] = 'Scaler'
    args[1] = 'Academy'
    print(args)
 
# Driver code
fun2('Python', 'programming', 'preparation')
