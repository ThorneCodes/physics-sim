#imports
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from sympy import *
# functions

def plot(x, y, mode="plot", save=False, title=""):
    if mode == "plot":
        plt.plot(x, y)
        if save:
            plt.savefig(title+".png")
        else:
            plt.show()
    elif mode == "scat":
        plt.scatter(x, y)
        if save:
            plt.savefig(title+".png")
        else:
            plt.show()

def dpdt(vel, time): #where vel is a vector
    p = vel + np.array([0, -9.78*time])
    return p

def velocity(speed, theta): #converts scalar speed into velocity vector
    theta = theta*(pi/180)
    return speed*np.array([(cos(theta)).evalf(), (sin(theta)).evalf()])

def collision(pos):
    coll = False
    x, y = pos[0], pos[1]
    if x >= 1 or x < 0:
        coll = True
    elif y >= 1 or y < 0:
        coll = True
    return coll

##def innerAngle(v1, v2):
##    cdot = np.dot(v1, v2)
##    mod1, mod2 = (sqrt(np.dot(v1,v1))).evalf(), (sqrt(np.dot(v2,v2))).evalf()
##    angle = (acos(cdot/(mod1*mod2))).evalf()
##    return angle

def bounce(p0):
    rot = lambda a: np.dot(p0,np.array([[(cos(a)).evalf(), (sin(a)).evalf()],[(-1*sin(a)).evalf(), (cos(a)).evalf()]]))
    return rot(pi)
    

def euler(speed, theta, t, h=0.0001): # Where h is step size and t is total time
    dp = lambda t,v: dpdt(v, t) # When evaluated return np.ndarray
        
    T = np.arange(0, t+h, h)
    s = [[0,0]]
    v_0 = velocity(speed, theta)
    for i in range(0, len(T) - 1):
        # CHECK FOR COLLISION AND ROTATE
        temp = s[i] + h*dp(T[i], v_0)
        if not collision(temp):
            s.append(temp)
        else:
            if s[i][0] >= 1 and (s[i][1] <= 0.6 and s[i][1] >= 0.3):
                break
            else:
                normal = np.array([0, 0])
                mul = np.array([1, 1])
                v_i = velocity(speed, theta)
##                if s[i][0] >= 1:
##                    normal = np.array([-1,0])
##                elif s[i][0] <= 0:
##                    normal = np.array([1,0])
##                elif s[i][1] >= 1:
##                    normal = np.array([0, -1])
##                elif s[i][1] <= 0:
##                    normal = np.array([0, 1])
                v_i = bounce(v_i)
                temp = s[i] + h*dp(T[i], v_i)
                s.append(temp)
        
    return np.array(s)

x, y = [], []
e = euler(6, 30, 10, h=0.001)

for var in e:
    x.append(var[0])
    y.append(var[1])

plot(x, y, mode="plot")
