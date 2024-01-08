import numpy as np
import math 

def obtain_dx(x,r,n):
    dx = r*2*np.sqrt(1 - (x/r)**2)*np.sin(math.pi/n)
    return dx

def obtain_c(dx,c):
    c2 = dx/(dx/c - 1)
    return c2

def n_from_l(r,l):
    perimeter = 2*r*math.pi
    n = perimeter/l
    return n