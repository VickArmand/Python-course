# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
 
fun(name="Scaler Academy", ID="001", language="Python")
