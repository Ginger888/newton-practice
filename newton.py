import numpy as np

# find derivative of f
def drvt(f,x):
    eps = 1e-5
    return (f(x+eps)-f(x))/eps

def drvt2(f,x):
    eps = 1e-5
    f2 = (drvt(f,x+eps) - drvt(f,x))/eps
    return f2


def optimize(f,x,eps):
    temp = 1 + eps
    while abs(temp) > eps:
        temp = drvt(f,x)/drvt2(f,x)
        x = x - temp
        print(abs(temp))
        print(x)
    return x


# x = 2.5
# f = np.cos
# eps = 1e-15

# optimize(f,x,eps)

optimize(c