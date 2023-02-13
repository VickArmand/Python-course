#!/usr/bin/python3
def func(name = "devX"):
    # devX acts as a default name just in case the function is called without a parameter  
    print(f"Hello {name}")

func()
func("Joe")