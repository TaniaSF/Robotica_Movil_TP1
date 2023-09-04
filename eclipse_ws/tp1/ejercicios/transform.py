'''
Created on Aug 27, 2023

@author: seb
'''

import numpy as np

def RotationMatrixX(angle):
    return np.array([[ 1.,                0.,              0.],
                     [ 0.,                np.cos(angle), -np.sin(angle)],
                     [ 0.,                np.sin(angle),  np.cos(angle)],])
                     
def RotationMatrixY(angle):
    return np.array([[ np.cos(angle),    0.,              np.sin(angle)],
                     [ 0.,                1.,              0.],
                     [-np.sin(angle),     0.,              np.cos(angle)],])
                     
def RotationMatrixZ(angle):
    return np.array([[ np.cos(angle),   -np.sin(angle),  0.],
                     [ np.sin(angle),    np.cos(angle),  0.],
                     [ 0.,                0.,              1.],])
    
def LocalFrame(scale=1.):
    return np.array([
        [0., scale, 0., 0.],
        [0., 0., scale, 0.],
        [0., 0., 0., scale],
        [1., 1., 1., 1.],
        ])

def Identity():
    return np.array([
        [1., 0., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.],
        [0., 0., 0., 1.],
        ])

def SetRotationalMatrix(T, R):
    T[0:3, 0:3] = R

def FrameTransform(frame, traslation, rotation):
    tx = traslation[0]
    ty = traslation[1]
    tz = traslation[2]
    
    M = np.array([
        [1., 0., 0., tx],
        [0., 1., 0., ty],
        [0., 0., 1., tz],
        [0., 0., 0., 1.],
        ])
    
    rx = rotation[0]
    ry = rotation[1]
    rz = rotation[2]
    
    Rx = RotationMatrixX(rx)
    Ry = RotationMatrixY(ry)
    Rz = RotationMatrixZ(rz)
    
    M[0:3, 0:3] = np.dot(Rx, np.dot(Ry, Rz))
    
    return np.dot(M, frame)
    
# def RotationMatrixXYZ(x, y, z):
    # Rx = RotationMatrixX(rx)
    # Ry = RotationMatrixY(ry)
    # Rz = RotationMatrixZ(rz)
    # return np.dot(Rx, np.dot(Ry, Rz))