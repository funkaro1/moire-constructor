import math
import numpy as np

def makeSimpleMoire(Moire):
    dx = Moire.d
    c = Moire.c
    
    lines = []
    xsize = Moire.xsize
    ysize = Moire.ysize
    x_min = -xsize/2
    x_max = xsize/2
    y_min = -ysize/2
    y_max = ysize/2
    angle = Moire.angle
    angle = math.radians(angle)
    dy = dx*math.tan(angle)
    c2 = dx/((dx/c) - 1)
    m = dy/c2
    if m < 0:
        p1 = np.array([x_min ,y_min])
        p2 = np.array([x_min + c2 ,y_min])
        p3 = np.array([x_min + c2 +  y_max*2/m ,y_max])
        p4 = np.array([x_min + y_max*2/m,y_max])
    else:
        p1 = np.array([x_min -  y_max*2/m,y_min])
        p2 = np.array([x_min + c2 - y_max*2/m,y_min])
        p3 = np.array([x_min + c2 ,y_max])
        p4 = np.array([x_min ,y_max])
        
    while True:
        if p2[0] >= x_max and p4 [0] >= x_max:
            lines.append([np.copy(p1),np.copy(p2),np.copy(p3),np.copy(p4)])
            break 
        
        lines.append([np.copy(p1),np.copy(p2),np.copy(p3),np.copy(p4)])
        p1 += np.array([2*c2,0])
        p2 += np.array([2*c2,0])
        p3 += np.array([2*c2,0])
        p4 += np.array([2*c2,0])
    
    Moire.points = lines
    