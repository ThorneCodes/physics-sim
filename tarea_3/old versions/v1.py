import numpy as np
import matplotlib.pyplot as plt

def plot(x, y, mode="plot"):

    if mode == "plot":
        plt.plot(x,y)
        plt.show()
        
    elif mode == "scat":
        plt.scatter(x,y)
        plt.show()

def collision(pos): # Takes a position (x,y) and determines if there's a collision

    # 1st element is status for X axis collision
    # 2nd element is status for Y axis collision
    # 3rd element is status for particle leaving the box
    
    x, y = pos[0], pos[1]
    coll = [False, False, False]

    if x <= 0 or x >= 1:
        if x >= 1 and (y > 0.4 and y < 0.6):
            coll = [True, True, True]
        else:
            coll[0] = True
    if y <= 0 or y >= 1:
        coll[1] = True
    return coll

def bounce(velocity, check, pos, time):

    normal = [1, 1]

    if check[2] != True:
        if check[0] == True:
            if pos[0] <= 0:
                normal[0] = 1
            elif pos[1] >= 1:
                normal[0] = -1
            else:
                normal[0] = 1
        elif check[1] == True:
            if pos[1] <= 0:
                normal[1] = 1
            elif pos[1] >= 1:
                normal[1] = -1
            else:
                normal[1] = 1
        return np.array([velocity[0]*normal[0], velocity[1]*normal[1]])
    else:
        return time

def velocity(speed, angle, t):
    xV = float(speed*np.cos(angle)*t)
    yV = float(speed*np.sin(angle)*t - 0.5*(t**2)*9.78)
    return np.array([xV, yV]) #This has gravity built-in

def position(initPos, initAngle, t, velArray):
    pos = initPos + velArray
    return pos

def innerAngle(a, b):
    dot = np.dot(a, b)
    normA, normB = np.sqrt(np.dot(a,a)), np.sqrt(np.dot(b,b))
    return np.arccos(dot/(normA*normB))

##def getPath(initPos, initSpeed, initAngle, totalTime, dt):
##
##    path = [[],[]]
##    
##    time = 0
##    Vel = velocity(initSpeed, initAngle, time)
##
##    while time <= totalTime:
##
##        pos = position(initPos, initAngle, time, Vel)
##        check = collision(pos)
##        Vel = bounce(Vel, check, pos, time)
##        path[0].append(pos[0])
##        path[1].append(pos[1])
##
##        time += dt
##
##    return path
##
##p = getPath(np.array([0,0]), 0.6, 45, 10, 0.1)
##plot(np.array(p[0]), np.array(p[1]), mode="scat")
##
