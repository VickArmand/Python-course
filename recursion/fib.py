#!/usr/bin/python3
def fib(n, memo = {}):
    # use of a dictionary to save the values minimizes the lookup time hence this is called memoization
    if(n <= 1):
        return 1
    if (n == 2):
        return 2
    if (n in memo):
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

if __name__ == "__main__":
    print(fib(400))
