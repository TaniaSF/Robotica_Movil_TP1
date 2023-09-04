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

import transforms3d.euler as euler

def NewSubplot(index):
    azm = 45
    ele = 30
    dst = 12
    
    ax = plt.subplot(1, 2, index, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.view_init(elev=ele, azim=azm)
    ax.dist = dst

def Ejercicio_1_1():
    print('--------------------------------------------------')
    print('Ejercicio 1 1')
    plt.figure()
    
    NewSubplot(1)
    plt.title('Base')
    
    l_F_base = transform.LocalFrame()
    print('Base en el Frame Local')
    print(l_F_base)
    drawer.PlotFrame(l_F_base)
    
    NewSubplot(2)
    plt.title('Ry(90)')
    
    g_R_l = euler.euler2mat(0, np.pi/2, 0, 'rxyz')
    print('Matriz de Rotación, intrinseca Ry(90):')
    print(g_R_l)
    g_T_l = transform.Identity()
    transform.SetRotationalMatrix(g_T_l, g_R_l)
    print('Matriz de Transformación:')
    print(g_T_l)
    
    g_F_base = np.dot(g_T_l, l_F_base)
    print('Base en el Frame Global')
    print(g_F_base)
    
    drawer.PlotFrame(g_F_base)
    
def Ejercicio_1_2():
    print('--------------------------------------------------')
    print('Ejercicio 1 2')
    plt.figure()
    
    NewSubplot(1)
    plt.title('Base')
    
    l_F_base = transform.LocalFrame()
    print('Base en el Frame Local')
    print(l_F_base)
    drawer.PlotFrame(l_F_base)
    
    NewSubplot(2)
    plt.title('Rx(-90)Ry(90)')
    
    g_R_l = euler.euler2mat(-np.pi/2, np.pi/2, 0, 'rxyz')
    print('Matriz de Rotación, intrinseca Rx(-90)Ry(90):')
    print(g_R_l)
    g_T_l = transform.Identity()
    transform.SetRotationalMatrix(g_T_l, g_R_l)
    print('Matriz de Transformación:')
    print(g_T_l)
    
    g_F_base = np.dot(g_T_l, l_F_base)
    print('Base en el Frame Global')
    print(g_F_base)
    
    drawer.PlotFrame(g_F_base)

def Ejercicio_1_3():
    print('--------------------------------------------------')
    print('Ejercicio 1 3')
    plt.figure()
    
    NewSubplot(1)
    plt.title('Base')
    
    l_F_base = transform.LocalFrame()
    print('Base en el Frame Local')
    print(l_F_base)
    drawer.PlotFrame(l_F_base)
    
    NewSubplot(2)
    plt.title('Rz(180)Rx(-90)Ry(90)')
    
    g_R_l = euler.euler2mat(np.pi, -np.pi/2, np.pi/2, 'rzxy')
    print('Matriz de Rotación, intrinseca Rz(180)Rx(-90)Ry(90):')
    print(g_R_l)
    g_T_l = transform.Identity()
    transform.SetRotationalMatrix(g_T_l, g_R_l)
    print('Matriz de Transformación:')
    print(g_T_l)
    
    g_F_base = np.dot(g_T_l, l_F_base)
    print('Base en el Frame Global')
    print(g_F_base)
    
    drawer.PlotFrame(g_F_base)

def Main():
    Ejercicio_1_1()
    Ejercicio_1_2()
    Ejercicio_1_3()
    
    plt.show()

if __name__ == '__main__':
    Main()
