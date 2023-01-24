def safe_print_division(a, b):
    try:
        c = a/b
        return (c)
    except ZeroDivisionError:
        c = None
    except:
        pass
    finally:
        print("Inside result: {}".format(c))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))