# The raise statement allows the programmer to force a specified exception to occur.
# If an unhandled exception occurs inside an except section, it will have the exception being handled attached to it and included in the error message:
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
# one can disable automatic exception chaining using the from None
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
