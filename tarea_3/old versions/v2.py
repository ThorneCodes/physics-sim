# imports
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import t, a
from sympy.utilities.lambdify import lambdify, implemented_function

f = implemented_function('f', lambda t, a: v(a,t)+ np.array([0, -9.78*t]))
lam_f = lambdify([t, a], f(t, a))

def v(a,t):
    return np.array([6*t*np.cos(a), 6*t*np.cos(a)])

def plot(x, y, mode="plot"):

    if mode == "plot":
        plt.plot(x, y)
        plt.show()

    elif mode == "scat":
        plt.scatter(x, y)
        plt.show()

    else:
        print("Invalid plotting mode")

def checkColl(pos):
    check = False
    if pos[0] <= 0 or pos[0] >= 1:
        check = True
    elif pos[1] <= 0 or pos[1] >= 1:
        check = True
    return check

def bounce(a, t):
    

def euler(t, a, known):
    if t != 0:
        e0 = np.array(lam_f(t-0.001, a))
        e1 = np.array(lam_f(t, a))
        h = (e1[0]-e0[0])/(e1[1]-e0[1])
        return e0 + e0*h*t
    else:
        return np.array([0,0])
    
def getPath(angle, dt):

    time = 0
    path = [[],[]]
    coll = [[],[]]
    while time < 10:
        p = euler(time, angle, path)
        path[0].append(p[0])
        path[1].append(p[1])
        coll[0].append(checkColl(p))
        coll[1].append(time)
        time += dt
    return path

path = getPath(45, 0.001)
x, y = path[0], path[1]
plot(x, y)
