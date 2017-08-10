def factorial(n):
    f=1
    while n>=1:
        f=f*n
        n=n-1
    return f


print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
