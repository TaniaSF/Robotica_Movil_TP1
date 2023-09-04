'''
Created on Aug 27, 2023

@author: seb
'''

import numpy as np

# R = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# T = np.array([[10], [11], [12]])
    #
# Z = np.array([
        # [21, 22, 23],
        # ])
        #
# A = np.empty((4, 4))
# A[0:3,  0:3] = R
# A[0:3,  3:4] = T
# A[3:4,  0:3] = Z
# A[3, 3] = 33
#
# print(A)


A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = np.array([[1, 3],
              [5, 7]])

print(np.dot(np.dot(A, B), C))
print(np.dot(A, np.dot(B, C)))


