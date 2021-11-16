from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def plot(x, y):
    plt.plot(x,y)
    plt.show()

def innerAngle(v1, v2):
    cdot = np.dot(v1, v2)
    m1 = (sqrt(np.dot(v1,v1))).evalf()
    m2 = (sqrt(np.dot(v2,v2))).evalf()
    return acos(cdot/(m1*m2))

def bounce(v1, normal):
    alpha = innerAngle(v1, normal)
    alpha = (alpha*(180/pi)).evalf()

    if (normal == np.array([1, 0])).all():
        return alpha/2
    elif (normal == np.array([-1, 0])).all():
        return 180 - alpha/2
    elif (normal == np.array([0, 1])).all():
        return 90 - alpha/2
    elif (normal == np.array([0, -1])).all():
        return 270 + alpha/2

mul = np.array([-1, 1])
n = np.array([5, 6])
print(mul*n)
