'''
Created on Aug 27, 2023

@author: seb
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import ejercicios.drawer as drawer
import ejercicios.transform as transform

def Ejercicio_1_1():
    plt.figure()
    plt.subplot(231, projection='3d')
    
    robot_frame = transform.LocalFrame()
    drawer.PlotFrame(robot_frame)
    
    w_translation_robot = [0, 0, 0]
    w_rotation_robot = [0, np.pi/2, 0]
    
    w_frame_robot = transform.FrameTransform(robot_frame, w_translation_robot, w_rotation_robot)
    
    ax = plt.subplot(232, projection='3d')
    drawer.PlotFrame(w_frame_robot)

def Ejercicio_1_2():
    plt.figure()
    
    Ry = transform.RotationMatrixY(np.pi/2)
    Rx = transform.RotationMatrixX(-np.pi/2)
    
    azm = 45
    ele = 30
    dst = 12
    
    # Frame Origin
    ax = plt.subplot(231, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev=ele, azim=azm)
    ax.dist = dst
    plt.title('xy Rx(-90)Ry(90)')
    
    robot_frame = transform.LocalFrame()
    drawer.PlotFrame(robot_frame)
    
    # Rotate In Rx(-90)
    ax = plt.subplot(232, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('In Rx(-90)')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = Rx
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Rotate In Rx(-90)Ry(90)
    ax = plt.subplot(233, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('In Rx(-90)Ry(90)')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = np.dot(Rx, Ry)
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Rotate Ex Ry(90)
    ax = plt.subplot(235, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('Ex Ry(90)')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = Ry
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Rotate Ex Rx(-90)Ry(90)
    ax = plt.subplot(236, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('Ex Ry(90)')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = np.dot(Rx, Ry)
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)

def Ejercicio_1_3():
    plt.figure()
    
    Rz = transform.RotationMatrixZ(np.pi)
    Rx = transform.RotationMatrixX(-np.pi/2)
    Ry = transform.RotationMatrixY(np.pi/2)
    
    azm = 45
    ele = 30
    dst = 12
    
    # Frame Origin
    ax = plt.subplot(241, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev=ele, azim=azm)
    ax.dist = dst
    plt.title('z(180)x(-90)y(90)')
    
    robot_frame = transform.LocalFrame()
    drawer.PlotFrame(robot_frame)
    
    # In z
    ax = plt.subplot(242, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('In Zxy')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = Rz
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # In zx
    ax = plt.subplot(243, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('In zXy')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = np.dot(Rz, Rx)
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # In zxy
    ax = plt.subplot(244, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('In zxY')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = np.dot(Rz, np.dot(Rx, Ry))
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Ex y
    ax = plt.subplot(246, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('Ex zxY')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = Ry
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Ex xy
    ax = plt.subplot(247, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('Ex zXy')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = np.dot(Rx, Ry)
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)
    
    # Ex zxy
    ax = plt.subplot(248, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    ax.view_init(elev = ele, azim = azm)
    ax.dist = dst
    plt.title('Ex Zxy')
    
    robot_frame = transform.LocalFrame()
    T = transform.Identity()
    R = np.dot(np.dot(Rz, Rx), Ry)
    transform.SetRotationalMatrix(T, R)
    robot_frame = np.dot(T, robot_frame)
    drawer.PlotFrame(robot_frame)

# Ejercicio_1_1()
# Ejercicio_1_2()
Ejercicio_1_3()

plt.show()