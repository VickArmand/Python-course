def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
     
# Using **kwargs to pass arguments to this function : 
kwargs = {"arg1" : "InterviewBit", "arg2" : "Blog", "arg3" : "Packing and Unpacking"}
myFun(**kwargs)