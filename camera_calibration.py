# -*- coding: utf-8 -*-
"""q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cqn1GQ6TY6VKKVIvyL6V4ddxsARVV20x
"""

import numpy as np
np.set_printoptions(precision=10)

"""Given points in world and image coordinates"""

x_w = [0,0,0,0,7,0,7,0]
y_w = [0,3,7,11,1,11,9,1]
z_w = [0,0,0,0,0,7,0,7]
x_c = [757, 758,758,759,1190,329,1204,340]
y_c = [213,415,686,966,172,1041,850,159]

"""Defining an empty Projection Matrix"""

P = np.zeros((3,4))
A = np.zeros((16,12))

"""Forming A matrix"""

for i,j in enumerate(x_w):
    A[2*i,:] = [x_w[i],y_w[i], z_w[i],1, 0, 0, 0, 0, -x_c[i]*x_w[i], -x_c[i]*y_w[i], -x_c[i]*z_w[i], -x_c[i]]
    A[2*i+1,:] = [0, 0, 0, 0,x_w[i],y_w[i], z_w[i],1,  -y_c[i]*x_w[i], -y_c[i]*y_w[i], -y_c[i]*z_w[i], -y_c[i]]

"""Finding the P matrix"""

U, S, V_T = np.linalg.svd(A)
V = V_T.T
S_sorted = (np.argsort(S))[::-1]
V[S_sorted]
min_eigenvect = V[:,-1]
P = min_eigenvect.reshape(3,4)

print('proejction matrix un-normalized \n', P)
print("\n")
"""Next method by directly usign eigen method of numpy and A_T, A"""

A_T = A.T
A_mat = np.matmul(A_T,A)
e,v = np.linalg.eig(A_mat)
sort = np.argsort(e)[::-1]
v[sort]
V_min = v[:,-1]
P_new = V_min.reshape(3,4)

"""QR factorization (Decomposing the projection matrix)

If you have a matrix composed of an upper triangular matrix and an orthonormal matrix, it is possible to decopule them using QR factorization
"""

q,r = np.linalg.qr(P[:,0:3])
r = r[:,:]/r[-1,-1]

"""Here q is the rotation matrix and r is the upper triangular calibrartion matrix

For a check the transpose of q multipied with q gives identity matrix
"""

print('rotation matrix \n', q)
print("\n")
print('calibration matrix \n', r)
print("\n")

"""Now  for translation vector"""

T = np.matmul(np.linalg.inv(r),P[:,-1])

print('Translational vector is \n', T)