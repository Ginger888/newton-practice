import numpy as np

# find derivative of f
def drvt(f,x):
    eps = 1e-5
    return (f(x+eps)-f(x))/eps

# second derivative of f
def drvt2(f,x):
    eps = 1e-5
    f2 = (drvt(f,x+eps) - drvt(f,x))/eps
    return f2


def optimize(x,f):
    if not callable(f):
        raise TypeError(f"Argument is not a function, it is of type {type(f)}")
    eps = 1e-15
    temp = 1 + eps
    while abs(temp) > eps:
        temp = drvt(f,x)/drvt2(f,x)
        x = x - temp
    return x

