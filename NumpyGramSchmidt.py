import numpy as np
import scipy.linalg as sc

# vect_input is the test input vectors with each list/array in the 2d array repressenting a column vector in a matrix
vect_input = [[1,1,1,1], [0,1,1,1], [0,0,1,1]]
def projn(x, v):
    return np.divide(np.dot(x, v), np.dot(v,v))
def orthonormalise(A):
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return [A[0]/sc.norm(A[0])]
    ort_list = []
    ort_list.append(np.array(A[0]))
    for i in range(1,len(A)):
        temp_v = A[i]
        for j in range(0, i):
            temp_v = np.subtract(temp_v, np.multiply(projn(L[i], ort_list[j]),  ort_list[j]))
        ort_list.append(np.array(temp_v))
    ort_list = np.array(ort_list)
    for i in range(len(ort_list)):
        x = sc.norm(ort_list[i])
        for j in range(len(ort_list[i])):
            ort_list[i][j] = (1/x)*ort_list[i][j]
    return ort_list

def qr_fact(A):
    q = orthonormalise(A)
    print("\nq: ", q)
    q_t = np.transpose(q)
    print("\nqt", q_t)
    print("\n",np.matmul(q,q_t))
    r = np.matmul(A, q_t)
    print("\nr:", r)
    print("A: ", np.matmul(r,q))

print(orthonormalise(vect_input))

qr_fact(vect_input))