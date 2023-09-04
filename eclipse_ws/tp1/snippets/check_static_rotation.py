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
    
    ax = plt.subplot(4, 4, idref, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev=ele, azim=azm)
    ax.dist = dst
    plt.title(title)

def PlotBase():
    # Frame Origin
    Subplot(1, 'base')
    robot_frame = transform.LocalFrame()
    drawer.PlotFrame(robot_frame)

def PlotRow(idref_init, axes, angles):
    for i in range(3):
        idref = idref_init + i
        Subplot(idref, f'{i} {axes}')
        robot_frame = transform.LocalFrame()
        T = transform.Identity()
        if 0 == i:
            R = euler.euler2mat(angles[0], 0, 0, axes)
        elif 1 == i:
            R = euler.euler2mat(angles[0], angles[1], 0, axes)
        else:
            R = euler.euler2mat(angles[0], angles[1], angles[2], axes)
        transform.SetRotationalMatrix(T, R)
        robot_frame = np.dot(T, robot_frame)
        drawer.PlotFrame(robot_frame)
    
    # # In zx
    # idref = idref_init + 1
    # Subplot(idref, f'2 {axes}')
    # robot_frame = transform.LocalFrame()
    # T = transform.Identity()
    # R = euler.euler2mat(angle, angle, 0, axes)
    # transform.SetRotationalMatrix(T, R)
    # robot_frame = np.dot(T, robot_frame)
    # drawer.PlotFrame(robot_frame)
    #
    # # In zxy
    # idref = idref_init + 2
    # Subplot(idref, f'3 {axes}')
    # robot_frame = transform.LocalFrame()
    # T = transform.Identity()
    # R = euler.euler2mat(angle, angle, angle, axes)
    # transform.SetRotationalMatrix(T, R)
    # robot_frame = np.dot(T, robot_frame)
    # drawer.PlotFrame(robot_frame)

def PlotRowIn(idref_init, Rs, alias):
    for i in range(3):
        idref = idref_init + i
        Subplot(idref, f'{i} {alias}')
        robot_frame = transform.LocalFrame()
        T = transform.Identity()
        
        if 0 == i:
            R = Rs[0]
        elif 1 == i:
            R = np.dot(Rs[0], Rs[1])
        else:
            R = np.dot(np.dot(Rs[0], Rs[1]), Rs[2])
        
        transform.SetRotationalMatrix(T, R)
        robot_frame = np.dot(T, robot_frame)
        drawer.PlotFrame(robot_frame)
    
def PlotRowEx(idref_init, Rs, alias):
    for i in range(3):
        idref = idref_init + i
        Subplot(idref, f'{i} {alias}')
        robot_frame = transform.LocalFrame()
        T = transform.Identity()
        
        if 0 == i:
            R = Rs[0]
        elif 1 == i:
            R = np.dot(Rs[1], Rs[0])
        else:
            R = np.dot(np.dot(Rs[2], Rs[1]), Rs[0])
        
        transform.SetRotationalMatrix(T, R)
        robot_frame = np.dot(T, robot_frame)
        drawer.PlotFrame(robot_frame)
    
def PlotRowExyz(idref_init):
    angle = np.pi/2
    
    Rz = transform.RotationMatrixZ(angle)
    Rx = transform.RotationMatrixX(angle)
    Ry = transform.RotationMatrixY(angle)
    
    idref = idref_init + 0
    Subplot(idref, f'1 Ezyx')
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = Rz
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # In zx
    idref = idref_init + 1
    Subplot(idref, f'2 Ezyx')
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = np.dot(Ry, Rz)
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # In zxy
    idref = idref_init + 2
    Subplot(idref, f'3 Ezyx')
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = np.dot(np.dot(Rz, Ry), Rx)
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)

def Ejercicio_1_3():
    plt.figure()
    
    PlotBase()
    
    angles = [np.pi/4, -np.pi/4, np.pi/4]
    # angles = [0, -np.pi/2, np.pi]
    PlotRow(2, 'rxyz', angles)
    
    angles = [np.pi/4, -np.pi/4, np.pi/4]
    # angles = [np.pi, -np.pi/2, 0]
    PlotRow(6, 'szyx', angles)
    
    angles = [np.pi/4, -np.pi/4, np.pi/4]
    # angles = [0, -np.pi/2, np.pi]
    Rx = transform.RotationMatrixX(angles[0])
    Ry = transform.RotationMatrixY(angles[1])
    Rz = transform.RotationMatrixZ(angles[2])
    Rs = [Rx, Ry, Rz]
    PlotRowIn(10, Rs, 'Ixyz')
    
    angles = [np.pi/4, -np.pi/4, np.pi/4]
    # angles = [0, -np.pi/2, np.pi]
    Rx = transform.RotationMatrixX(angles[0])
    Ry = transform.RotationMatrixY(angles[1])
    Rz = transform.RotationMatrixZ(angles[2])
    Rs = [Rz, Ry, Rx]
    PlotRowEx(14, Rs, 'Ezyx')
    
    # PlotRowExyz(14)

Ejercicio_1_3()

plt.show()

