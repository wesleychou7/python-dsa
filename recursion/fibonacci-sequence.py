"""
Your function will accept a number n and return the nth number of the fibonacci 
sequence. Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,55... starts 
off with a base case checking to see if n = 1 or n == 2, then it returns 0, 1
respectively.

Else it returns fib(n-1) + fib(n+2).
"""

def fib_rec(n):
    """
    Using recursion.
    """
    # base cases
    if n < 1:
        return "Error"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    else:
        return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(10)) # should equal 34



# Instantiate Cache information
n = 10
cache = [None] * (n + 1)

def fib_dyn(n):
    """
    Using dynamic programming by using a cache to store results (memoization).
    """
    # edge cases
    if n < 1: 
        return "Error"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    if cache[n] != None:
        return cache[n]
    
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]

print(fib_dyn(10))



def fib_iter(n):
    """
    Using iteration
    """
    sequence = []

    for i in range(n):
        
        if i == 0:
            output = 0
        elif i == 1:
            output = 1
        else:
            output += sequence[-1] + sequence[-2]

        sequence.append(output)
        output = 0

    return sequence[-1]

print(fib_iter(10))





