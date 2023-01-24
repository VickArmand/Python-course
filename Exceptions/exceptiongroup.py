def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
f()

# By using except* instead of except, we can selectively handle only the exceptions in the group that match a certain type. In the following example, which shows a nested exception group, each except* clause extracts from the group exceptions of a certain type while letting all other exceptions propagate to other clauses and eventually to be reraised.
def f2():
    raise ExceptionGroup("group1",[OSError(1),SystemError(2),ExceptionGroup("group2",[OSError(3), RecursionError(4)])])
try:
    f2()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

# Note that the exceptions nested in an exception group must be instances, not types. This is because in practice the exceptions would typically be ones that have already been raised and caught by the program, along the following pattern:
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)