'''
Created on Aug 27, 2023

@author: seb
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# import transforms3d.euler as euler

def RotationMatrixX(angle):
    return np.array([[ 1,                0,              0],
                     [ 0,                np.cos(angle), -np.sin(angle)],
                     [ 0,                np.sin(angle),  np.cos(angle)],])
                     
def RotationMatrixY(angle):
    return np.array([[ np.cos(angle),    0,              np.sin(angle)],
                     [ 0,                1,              0],
                     [-np.sin(angle),     0,              np.cos(angle)],])
                     
def RotationMatrixZ(angle):
    return np.array([[ np.cos(angle),   -np.sin(angle),  0],
                     [ np.sin(angle),    np.cos(angle),  0],
                     [ 0,                0,              1],])
    
def RotationMatrixXYZ(x, y, z):
    Rx = RotationMatrixX(rx)
    Ry = RotationMatrixY(ry)
    Rz = RotationMatrixZ(rz)
    return np.dot(Rx, np.dot(Ry, Rz))

ax = plt.figure().add_subplot(projection='3d')

def PlotFrame(traslation, rotation):
    tx = traslation[0]
    ty = traslation[1]
    tz = traslation[2]
    
    P = np.array([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        ])
    
    print(P)
    
    # R[0:3, 0:3] = RotationMatrixZ(rz) * RotationMatrixY(ry) * RotationMatrixX(rx)
    
    
    
    # M = np.identity(4)
    M = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1],
        ])
    rx = rotation[0]
    ry = rotation[1]
    rz = rotation[2]
    
    Rx = RotationMatrixX(rx)
    Ry = RotationMatrixY(ry)
    Rz = RotationMatrixZ(rz)
    
    M[0:3, 0:3] = np.dot(Rx, np.dot(Ry, Rz))
    
    print(M)
    
    Q = np.dot(M, P)
    
    print(Q)
    
    # rx = rotation[0]
    # ry = rotation[1]
    # rz = rotation[2]
    #
    # R = np.identity(4)
    # R[0:3, 0:3] = RotationMatrixZ(rz) * RotationMatrixY(ry) * RotationMatrixX(rx)
    # print(R)
    
    # Q = R * P
    
    cx = Q[0, 0]
    cy = Q[1, 0]
    cz = Q[2, 0]
    
    xx = Q[0, 1]
    xy = Q[1, 1]
    xz = Q[2, 1]
    
    yx = Q[0, 2]
    yy = Q[1, 2]
    yz = Q[2, 2]
    
    zx = Q[0, 3]
    zy = Q[1, 3]
    zz = Q[2, 3]
    
    plt.plot([cx, xx], [cy, xy], [cz, xz], 'r')
    plt.plot([cx, yx], [cy, yy], [cz, yz], 'g')
    plt.plot([cx, zx], [cy, zy], [cz, zz], 'b')

PlotFrame([0, 0, 0], [0, 0, 0])
# PlotFrame([1, 1, 1], [0, 0, 0])
# PlotFrame([0, 1, 1], [0, 0, 0])
# PlotFrame([0, 1, 0], [0, 0, 0])

PlotFrame([1, 1, 1], [np.pi/2, np.pi/2, np.pi/2])

# ax = plt.figure().add_subplot(projection='3d')
# PlotFrame([0, 0, 0], [0, 0, 0])
# PlotFrame([1, 1, 1], [np.pi, np.pi, 0])
#
# ax = plt.figure().add_subplot(projection='3d')
# PlotFrame([0, 0, 0], [0, 0, 0])
# PlotFrame([1, 1, 1], [np.pi, np.pi, -np.pi/2])

# plt.axis('equal')
plt.show()