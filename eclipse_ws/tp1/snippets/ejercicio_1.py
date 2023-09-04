'''
Created on Aug 27, 2023

@author: seb
'''
import unittest
import numpy as np
import transforms3d.affines as affines
import transforms3d.euler as euler

# # res = aff.compose(np.zeros(3), np.eye(3), np.ones(3), np.zeros(3))
# # print(res)
# #
# # r = euler.euler2mat(, 0, 0)
#
# def RotationIdentityMatrix():
    # return np.identity(3)
    #
# def RotationMatrixX(angle):
    # return np.array([[ 1,                0,              0],
                     # [ 0,                np.cos(angle), -np.sin(angle)],
                     # [ 0,                np.sin(angle),  np.cos(angle)],])
                     #
# def RotationMatrixY(angle):
    # return np.array([[ np.cos(angle),    0,              np.sin(angle)],
                     # [ 0,                1,              0],
                     # [-np.sin(angle),     0,              np.cos(angle)],])
                     #
# def RotationMatrixZ(angle):
    # return np.array([[ np.cos(angle),   -np.sin(angle),  0],
                     # [ np.sin(angle),    np.cos(angle),  0],
                     # [ 0,                0,              1],])
                     #
# def MatrixCompose(mA, mB):
    # return np.dot(mA, mB)
    #
# # def RotarionMatrixXYZ(x, y, z):
    # # Rx = RotationMatrixX(x)
    # # Ry = RotationMatrixX(y)
    # # Rz = RotationMatrixX(z)
    # # return ComposeMatrix(Rz, ComposeMatrix(Ry, Rx))
    #
# def TranslationZeroMatrix():
    # return np.zeros((3, 1))
    #
# def TranslationMatrix(x=0., y=0., z=0.):
    # return np.array([[x],
                     # [y],
                     # [z],])
                     #
# # def AffineRotationMatrix(x=0., y=0., z=0.):
    # # Rx = AffineRotarionMatrixX(x)
    # # Ry = RotarionMatrixY(Transformation matrices are matrices for application on the left, applied to coodinates on the right, stored as column vecty)
    # # Rz = RotarionMatrixZ(z)
    # # return ComposeMatrix(Rz, ComposeMatrix(Ry, Rx))
    #
# # def TransformationMatrix(T, R):
    # # return R + T
    #
# # def AffineEmptyMatrix():
    # # A = np.zeros((4, 4))
    # # A[3, 3] = 1
    # # return A
    #
# def TransformationIdentityMatrix():
    # return np.identity(4)
    #
# def TransformationMatrix(mt, mR):
    # mT = TransformationIdentityMatrix()
    # mT[0:3,  3:4] = mt
    # mT[0:3,  0:3] = mR
    # return mT
    #
# def TransformationRotationMatrix(mR):
    # mt = TranslationZeroMatrix()
    # return TransformationMatrix(mt, mR)
    #
# def TransformationTranslationMatrix(mt):
    # mR = RotationIdentityMatrix()
    # return TransformationMatrix(mt, mR)
    #
# def TransformationTransform(mA, transformation):
    # return MatrixCompose(transformation, mA)
    #
# def TransformationRotateX(mA, angle):
    # rotation = RotationMatrixX(angle)
    # transformation = TransformationRotationMatrix(rotation)
    # return TransformationTransform(mA, transformation)
    #
# def TransformationRotateY(mA, angle):
    # rotation = RotationMatrixY(angle)
    # transformation = TransformationRotationMatrix(rotation)
    # return TransformationTransform(mA, transformation)
    #
# def TransformationRotateZ(mA, angle):
    # rotation = RotationMatrixZ(angle)
    # transformation = TransformationRotationMatrix(rotation)
    # return TransformationTransform(mA, transformation)

class Test_Ejercicio_1(unittest.TestCase):

    def test_Ejercicio_1_1(self):
        print('test_Ejercicio_1_1')
        
        T = [0, 0, 0]
        R = euler.euler2mat(0, 0, 0, 'sxyz')
        Z = [1, 1, 1] # zooms
        robot_pose = affines.compose(T, R, Z)
        
        print(robot_pose)
        
        T = [0, 0, 0]
        R = euler.euler2mat(0, np.pi/2, 0, 'sxyz')
        Z = [1, 1, 1]
        rot_y_90 = affines.compose(T, R, Z)
        
        new_robot_pose = np.dot(rot_y_90, robot_pose)
        
        print(new_robot_pose)

    def test_Ejercicio_1_2(self):
        print('test_Ejercicio_1_2')
        
        T = [0, 0, 0]
        R = euler.euler2mat(0, 0, 0, 'sxyz')
        Z = [1, 1, 1] # zooms
        robot_pose = affines.compose(T, R, Z)
        
        print(robot_pose)
        
        T = [0, 0, 0]
        R = euler.euler2mat(-np.pi/2, np.pi/2, 0, 'sxyz')
        Z = [1, 1, 1]
        rot_x_n90_y_90 = affines.compose(T, R, Z)

        new_robot_pose = np.dot(rot_x_n90_y_90, robot_pose)
        print(new_robot_pose)

        T = [0, 0, 0]
        R = euler.euler2mat(-np.pi/2, 0, 0, 'sxyz')
        Z = [1, 1, 1]
        rot_x_n90 = affines.compose(T, R, Z)
        
        T = [0, 0, 0]
        R = euler.euler2mat(0, np.pi/2, 0, 'sxyz')
        Z = [1, 1, 1]
        rot_y_90 = affines.compose(T, R, Z)
        
        new_robot_pose = np.dot(rot_y_90, robot_pose)
        print(new_robot_pose)

    # def test_Ejercicio_Ry_p90(self):
        # Ao = TransformationIdentityMatrix()
        # Af = TransformationRotateY(Ao, np.pi/2)
        #
        # Bo = aff.compose(np.zeros(3), np.eye(3), np.ones(3), np.zeros(3))
        # matRot = euler.euler2mat(0, np.pi/2, 0)
        # matAff = aff.compose(np.zeros(3), matRot, np.ones(3), np.zeros(3))
        #
        # Bf = MatrixCompose(matAff, Bo)
        # self.assertEqual(True, np.all(Bf == Af), f'Bf: {Bf}, Af: {Af}')
        
    # def test_Ejercicio_Rx_n90_Ry_p90(self):
        # Ao = TransformationIdentityMatrix()
        # A = TransformationRotateX(Ao, -np.pi/2)
        # A = TransformationRotateY(A, np.pi/2)
        #
        # Bo = aff.compose(np.zeros(3), np.eye(3), np.ones(3), np.zeros(3))
        # matRot = euler.euler2mat(-np.pi/2, np.pi/2, 0)
        # matAff = aff.compose(np.zeros(3), matRot, np.ones(3), np.zeros(3))
        # B = MatrixCompose(matAff, Bo)
        #
        # self.assertEqual(True, np.all(B == A), f'Bf: {B}, Af: {A}')
        
    # def test_Ejercicio_Rz_p180_Rx_n90_Ry_p90(self):
        # Ao = TransformationIdentityMatrix()
        # A = TransformationRotateZ(Ao, np.pi)
        # A = TransformationRotateX(A, -np.pi/2)
        # # A = TransformationRotateY(A, np.pi/2)
        #
        # Bo = aff.compose(np.zeros(3), np.eye(3), np.ones(3), np.zeros(3))
        # # matRot = euler.euler2mat(np.pi, -np.pi/2, np.pi/2, 'rzxy')
        # matRot = euler.euler2mat(np.pi, -np.pi/2, 0, 'rxy')
        # matAff = aff.compose(np.zeros(3), matRot, np.ones(3), np.zeros(3))
        # B = MatrixCompose(matAff, Bo)
        #
        # self.assertEqual(True, np.all(B == A), f'Bf: {B}, Af: {A}')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()