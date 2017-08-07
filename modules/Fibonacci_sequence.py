"""Implement a function recursivly to get the desired
Fibonacci sequence value."""

def get_fib(position):
    if position==0:
        return 0
    elif position==1:
        return 1
    else:
        return get_fib(position-2)+get_fib(position-1)
    

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
