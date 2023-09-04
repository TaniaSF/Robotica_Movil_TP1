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
    
    ax = plt.subplot(1, 4, index, projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.view_init(elev=ele, azim=azm)
    ax.dist = dst

def Ejercicio_2_a():
    print('--------------------------------------------------')
    print('Ejercicio 2 a')
    plt.figure()
    
    alpha = 4./7. * np.pi
    beta = np.pi / 2
    gamma = -1./2. * np.pi
    orden = 'xyz'
    
    print(f'alpha: {alpha}')
    print(f'beta: {beta}')
    print(f'gamma: {gamma}')
    print(f'orden: {orden}')
    
    R = euler.euler2mat(alpha, beta, gamma, f'r{orden}')
    print('Matriz de rotación resultante')
    print(R)
    
    NewSubplot(1)
    plt.title('Base')
    frame_base = transform.LocalFrame()
    drawer.PlotFrame(frame_base)
    
    NewSubplot(2)
    plt.title('Rx(a)')
    R = euler.euler2mat(alpha, 0, 0, f'r{orden}')
    T = transform.Identity()
    transform.SetRotationalMatrix(T, R)
    frame = np.dot(T, frame_base)
    drawer.PlotFrame(frame)
    
    NewSubplot(3)
    plt.title('Rx(a)Ry(b)')
    R = euler.euler2mat(alpha, beta, 0, f'r{orden}')
    T = transform.Identity()
    transform.SetRotationalMatrix(T, R)
    frame = np.dot(T, frame_base)
    drawer.PlotFrame(frame)
    
    NewSubplot(4)
    plt.title('Rx(a)Ry(b)Rz(g)')
    R = euler.euler2mat(alpha, beta, gamma, f'r{orden}')
    T = transform.Identity()
    transform.SetRotationalMatrix(T, R)
    frame = np.dot(T, frame_base)
    drawer.PlotFrame(frame)

def Ejercicio_2_b():
    print('--------------------------------------------------')
    print('Ejercicio 2 b')
    plt.figure()
    
    alpha = 4./7. * np.pi
    beta = np.pi / 2
    gamma = -1./2. * np.pi
    
    alpha = alpha + gamma
    gamma = 0
    
    orden = 'xyz'
    
    print(f'alpha: {alpha}')
    print(f'beta: {beta}')
    print(f'gamma: {gamma}')
    print(f'orden: {orden}')
    
    NewSubplot(1)
    plt.title('Base')
    frame_base = transform.LocalFrame()
    drawer.PlotFrame(frame_base)
    
    NewSubplot(2)
    plt.title('Rx(a+g)')
    R = euler.euler2mat(alpha, 0, 0, f'r{orden}')
    T = transform.Identity()
    transform.SetRotationalMatrix(T, R)
    frame = np.dot(T, frame_base)
    drawer.PlotFrame(frame)
    
    NewSubplot(3)
    plt.title('Rx(a+g)Ry(b)')
    R = euler.euler2mat(alpha, beta, 0, f'r{orden}')
    T = transform.Identity()
    transform.SetRotationalMatrix(T, R)
    frame = np.dot(T, frame_base)
    drawer.PlotFrame(frame)
    
    NewSubplot(4)
    plt.title('Rx(a+g)Ry(b)Rz(0)')
    R = euler.euler2mat(alpha, beta, gamma, f'r{orden}')
    T = transform.Identity()
    transform.SetRotationalMatrix(T, R)
    frame = np.dot(T, frame_base)
    drawer.PlotFrame(frame)

def Main():
    Ejercicio_2_a()
    Ejercicio_2_b()
    
    plt.show()

if __name__ == '__main__':
    Main()
