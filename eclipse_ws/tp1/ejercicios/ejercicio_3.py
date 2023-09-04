'''
Created on Aug 28, 2023

@author: seb
'''

import os
import sys

def Setup():
    current_path = os.getcwd() + "/../"
    sys.path.append(current_path)
    
Setup()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import ejercicios.drawer as drawer
import ejercicios.transform as transform

import transforms3d.affines as affines
import transforms3d.euler as euler

def NewSubplot():
    ax = plt.subplot(1, 1, 1)
    ax.set_xlim(0, 6)
    ax.set_xlabel('X')
    
    ax.set_ylim(0, 10)
    ax.set_ylabel('Y')
    
    ax.grid(True)
    ax.axis('equal')
    # plt.grid(linestyle='-', linewidth=0.5)

def Transformation2D(x, y, yaw):
    Rz = transform.RotationMatrixZ(yaw)
    return affines.compose([x, y, 0], Rz, np.ones(3))

def Point2D(x, y):
    return np.array([[x], [y], [0], [1]])

def DrawRobot(T, color):
    frame_base = transform.LocalFrame(1.)
    G_frame = np.dot(T, frame_base)
    drawer.PlotFrame2D(G_frame)

def DrawPoint(P, color):
    drawer.PlotPoint2D(P)

def Ejercicio_3():
    print('--------------------------------------------------')
    print('Ejercicio 3')
    
    W_T_A = Transformation2D(2, 3, np.pi/4)
    A_T_B = Transformation2D(1, 1, -np.pi/4)
    W_P1 = Point2D(1, 5)
    A_P2 = Point2D(1, 2)
    
    print('Ejercicio 3 a')
    plt.figure()
    NewSubplot()
    DrawRobot(W_T_A, 'r')
    DrawRobot(np.dot(W_T_A, A_T_B), 'b')
    DrawPoint(W_P1, 'r')
    DrawPoint(np.dot(W_T_A, A_P2), 'b')

    print('Ejercicio 3 b')
    print('A_p1')
    A_T_W = np.linalg.inv(W_T_A)
    print(np.dot(A_T_W, W_P1))
    
    print('Ejercicio 3 c')
    print('B_P2')
    B_T_A = np.linalg.inv(A_T_B)
    print(np.dot(B_T_A, A_P2))
    
    print('Ejercicio 3 d')
    print('W_T_B')
    W_T_B = np.dot(W_T_A, A_T_B)
    T, R, _, _ = affines.decompose44(W_T_B)
    angle = euler.mat2euler(R, axes='szyx')
    print(W_T_B)
    print(f'T: {T}')
    print(f'R: {R}')
    print(f'x: {T[0]}, y: {T[1]}, yaw: {angle[2]}')

def Main():
    Ejercicio_3()
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    Main()
