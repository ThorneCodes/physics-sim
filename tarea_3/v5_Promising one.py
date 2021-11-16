#impots
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# Functions

def plot(x, y, mode="plot"): #plotting function, takes 2 arrays (1 for x, 1 for y) and an optional arg 'mode'
    plt.clf()
    last = x[len(x)-1], y[len(y)-1]
    print(last)
    x, y = x[0:len(x)-1], y[0:len(x)-1]
    if mode == "plot":
        plt.plot(x, y)
        plt.scatter(last[0], last[1], color='red')
        plt.show()
    elif mode == "scatter":
        plt.scatter(x, y)
        plt.scatter(last[0], last[1], color='red', marker='x')
        plt.show()
    else:
        print("Invalid plot mode")

def bounceX(x_i): #Basic bounce for X axis (flips X velocity sign)
    if round(x_i, 10) > 1 or round(x_i, 10) < 0:
        return float(-1) # collision detected
    else:
        return float(1) # NO collision
    
def bounceY(y_i): #Basic bounce for Y axis (flips Y velocity sign)
    if round(y_i, 10) > 1 or round(y_i, 10) < 0:
        return float(-1) # collision detected
    else:
        return float(1) # NO collision

def floor_aux(a, y_0, y_1, t_i, h):

    # THIS NEEDS TO CHANGE TO BE ABLE TO BOUNCE OFF OF THE FLOOR ACCURATELY
    m, g = 1, 9.78
    v = (y_1 - y_0)/h
    print("Value of speed at floor collision: ",v)
    fy_aux = lambda t: -1*v*(sin(a)).evalf() -g*t
    y_i = y_1 + h*fy_aux(t_i)
    return [y_i, -1*v]

def euler(s, a, h=0.0001): # Euler method application

    # Initialization
    a *= (pi/180).evalf()
    n = 10/h
    sx, sy = s, s
    dirX, dirY = 1, 1
    fx = lambda t: sx*(cos(a)).evalf()
    fy = lambda t: sy*(sin(a)).evalf() - 9.78*t
    T = np.linspace(0, 10+h, int(n))

    # Initial Condition
    px, py = [0], [0]

    # Iteration
    for i in range(1, len(T)-1):
        x_i = px[i-1] + h*fx(T[i])
        y_i = py[i-1] + h*fy(T[i])

        if y_i < 0: # Checks for floor bounce, which gives some issues due to the size of the step being so small
            temp = floor_aux(a, py[i-2], py[i-1], T[i], h)
            y_i, sy = temp[0], temp[1]
        else:
            if (x_i >= 1) and (y_i > 0.4 and y_i < 0.6): # Checks if the particle left the box & breaks iteration
                px.append(x_i)
                py.append(y_i)
                break
            else:   # No special or problematic collisions
                sx, sy = sx*bounceX(x_i), sy*bounceY(y_i)
                x_i = px[i-1] + h*fx(T[i])
                y_i = py[i-1] + h*fy(T[i])

        px.append(x_i)
        py.append(y_i)
    
    return np.array([px, py])


path = euler(6, 30)
plot(path[0], path[1])
