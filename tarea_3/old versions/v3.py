#imports
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math

def eulerX(h):
    f = lambda t,a: 6*np.cos(a)
    t = np.arange(0,1+h,h)
    s0 = 0

    s = np.zeros(len(t))
    s[0] = s0

    for i in range(0, len(t)-1):
        temp = s[i] + h*f(t[i], s[i])
        if not checkX(temp):
            s[i + 1] = temp
        else:
            temp = bounceX(t[i], s[i], temp, h)
            s[i + 1] = temp
    return s

def eulerY(h):
    f = lambda t,a: 6*np.sin(a) - 9.78*t
    t = np.arange(0, 1+h, h)
    s0 = 0

    s = np.zeros(len(t))
    s[0] = s0

    for i in range(0, len(t)-1):
        temp = s[i] + h*f(t[i], s[i])
        if not checkY(temp):
            s[i + 1] = temp
        else:
            temp = bounceY(t[i], s[i], temp, h)
            s[i + 1] = temp
    return s

def bounceX(t, a, pos, h):
    f = lambda t,a: -1*6*np.cos(a)
    s_t = pos + h*f(t, a)
    return s_t

def bounceY(t, a, pos, h):
    f = lambda t,a: -1*6*np.sin(a) -9.78*t
    s_t = pos + h*f(t, a)
    return s_t

def checkX(pos):
    check = False
    if pos <= 0 or pos >= 1:
        check = True
    else:
        check = False
    return check

def checkY(pos):
    check = False
    if pos <= 0 or pos >= 1:
        check = True
    else:
        check = False
    return check

def checkExit(posX, posY):
    Exit = False
    if posX >= 1 and (posY >= 0.4 and posY <= 0.6):
        Exit = True
    else:
        Exit = False
    return Exit

x, y = eulerX(0.0001), eulerY(0.0001)
plt.scatter(x, y)
plt.show()
