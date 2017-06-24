from scipy.optimize import fsolve
import math
import numpy as np


#def equations(p):
#    """eq'n format 0 = ax + by + c"""
#    [x, y] = p
#    return (x+y-1, x-y-3, x+y-1, x+y-1)
def foo(x):
    return x**2

def equations(p):
    """eq'n format 0 = ax + by + c"""
    [x, y] = p
    list = [x - 5 , y - 5]
    return list



#x =  fsolve(equations, (1, 1))
init_val = np.zeros((2), dtype=int)
init_val += 1
x =  fsolve(equations, init_val)
#q, w = (1, 2)
print(x)
#print(equations((x, y)))
