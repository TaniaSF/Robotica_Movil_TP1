'''
Created on Aug 23, 2023

@author: seb
'''

import numpy as np
import transforms3d.affines as aff
import transforms3d.euler as euler

res = aff.compose(np.zeros(3), np.eye(3), np.ones(3), np.zeros(3))
print(res)

r = euler.euler2mat(0, 0, 0)
print(r)
