def factorial(n):# set your base case!
    if n <= 1:
        return 1
    else:
        return factorial(n-1 ) * n
n=int(input())
print(factorial(n))
