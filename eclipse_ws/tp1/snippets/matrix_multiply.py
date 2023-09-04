'''
Created on Aug 23, 2023

@author: seb
'''

import numpy as np

if __name__ == '__main__':
    # Define two matrices
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    
    # Perform matrix multiplication
    result = np.dot(matrix_a, matrix_b)
    print(result)