'''
Created on Aug 28, 2023

@author: seb
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import ejercicios.drawer as drawer
import ejercicios.transform as transform

import transforms3d.euler as euler

def Subplot(idref, title):
    azm = 45
    ele = 30
    dst = 12
    
    ax = plt.subplot(idref, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev=ele, azim=azm)
    ax.dist = dst
    plt.title(title)

def Ejercicio_1_3():
    plt.figure()
    
    angle_z = np.pi
    angle_x = -np.pi/2
    angle_y = np.pi/2
    
    # Frame Origin
    Subplot(241, 'z(180)x(-90)y(90)')
    
    robot_frame = transform.LocalFrame()
    drawer.PlotFrame(robot_frame)
    
    # In z
    Subplot(242, 'In Zxy')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = euler.euler2mat(angle_z, 0, 0, 'rzxy')
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # In zx
    Subplot(243, 'In zXy')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    # R = np.dot(Rz, Rx)
    R = euler.euler2mat(angle_z, angle_x, 0, 'rzxy')
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # In zxy
    Subplot(244, 'In zxY')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    # R = np.dot(Rz, np.dot(Rx, Ry))
    R = euler.euler2mat(angle_z, angle_x, angle_y, 'rzxy')
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Ex y
    Subplot(246, 'Ex zxY')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    # R = Ry
    R = euler.euler2mat(0, 0, angle_y, 'rzxy')
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Ex xy
    Subplot(247, 'Ex zXy')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    # R = np.dot(Rx, Ry)
    R = euler.euler2mat(0, angle_x, angle_y, 'syxz')
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Ex zxy
    Subplot(248, 'Ex Zxy')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    # R = np.dot(np.dot(Rz, Rx), Ry)
    R = euler.euler2mat(angle_z, angle_x, angle_y, 'syxz')
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)

Ejercicio_1_3()

plt.show()

