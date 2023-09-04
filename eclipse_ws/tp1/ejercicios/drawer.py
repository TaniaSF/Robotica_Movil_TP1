'''
Created on Aug 27, 2023

@author: seb
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import ejercicios.transform as transform

# def FrameBase():
    # return np.array([
        # [0, 1, 0, 0],
        # [0, 0, 1, 0],
        # [0, 0, 0, 1],
        # [1, 1, 1, 1],
        # ])

def PlotFrame2D(frame):
    cx = frame[0, 0]
    cy = frame[1, 0]
    
    xx = frame[0, 1]
    xy = frame[1, 1]
    
    yx = frame[0, 2]
    yy = frame[1, 2]
    
    plt.plot([cx, xx], [cy, xy], 'r')
    plt.plot([cx, yx], [cy, yy], 'g')

def PlotPoint2D(P):
    x = P[0]
    y = P[1]
    plt.plot([x], [y], 'o')

def PlotFrame(frame):
    cx = frame[0, 0]
    cy = frame[1, 0]
    cz = frame[2, 0]
    
    xx = frame[0, 1]
    xy = frame[1, 1]
    xz = frame[2, 1]
    
    yx = frame[0, 2]
    yy = frame[1, 2]
    yz = frame[2, 2]
    
    zx = frame[0, 3]
    zy = frame[1, 3]
    zz = frame[2, 3]
    
    plt.plot([cx, xx], [cy, xy], [cz, xz], 'r')
    plt.plot([cx, yx], [cy, yy], [cz, yz], 'g')
    plt.plot([cx, zx], [cy, zy], [cz, zz], 'b')
