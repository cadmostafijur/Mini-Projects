def factorial(n):# set your base case!
    if n <= 1:
        return 1
    else:
        return factorial(n-1 ) * n #simple fac if n=4 then (4-1)*4=12 it returns 12
n=int(input())
print(factorial(n))
