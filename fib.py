=====================**************==============================
def fib(n):
    if n <= 1:
        return n
    else:
        return fib( n-1) + fib(n-2 )
n=int(input())
print(fib(n))

=======================*************===========================
# using memoization with the fibonacci sequence
cache = { } # used to cache values to be used later
def fib(n):
    if n in cache:
        return cache[ n ] # return value stored in dictionary
    result = 0 # base case
    if n <= 1:
        result = n
    else:
        result = fib(n-1) + fib( n-2 )
        cache[ n ] = result # save result into dictionary with n as the key
    return result
print( fib(50) ) # calculates almost instantly
=======================********************=================================
# using @lru_cache, Python’s default moization/caching technique
from functools import lru_cache
@lru_cache( ) # python’s built-in memoization/caching system
def fib(n):
    if n <= 1:
        return n
    else:
        return fib( n -1 ) + fib( n- 2 )
print(fib(50)) # calculates almost instantly
==============================*********************==============================
