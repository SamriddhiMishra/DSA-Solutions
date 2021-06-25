# fibonacci 
# fn = (n-1) + (n-2)
# f0 = 0
# f1 = 1
# I - n , O - fn

def fib(f0, f1, n):
    if n == 1:
        return f0
    elif n == 2:
        return f1
    else:
        for i in range(n-2):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
    
print(fib(0, 1,4))
        