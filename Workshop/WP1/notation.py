# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:02:38 2020

@author: Pio
"""

from correction import *
from ref import quantumComputer as qC

arr = np.array([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])
t1_1 = np.array_equal(arr, quantumComputer(3,[]))
arr = np.array([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])
t1_2 = np.array_equal(arr, quantumComputer(2,[]))
arr = np.zeros([16])
arr[0] = 1
t1_3 = np.array_equal(arr, quantumComputer(4,[]))

print(t1_1 and t1_2 and t1_3 )


m1 = [0,2]
m2 = [[4,5],[6,7]]
t2_1 = np.array_equal(kroneckerProduct(m1,m2) , [[ 0,  0,  8, 10],[ 0,  0, 12, 14]])

m1 = [[4,5],[6,7]]
m2 = [[4,5],[6,7]]
t2_2   = np.array_equal(kroneckerProduct(m1,m2) , np.kron(m1,m2))

print(t2_1 and t2_2)

m = [[0,1],[1,0]]
arr = [[0., 1., 0., 0.],
 [1., 0., 0., 0.],
 [0., 0., 0., 1.],
 [0., 0., 1., 0.]]
t3_1 = np.array_equal(computeMatrix(m,2,0), arr)

m = [[0,1],[1,0]]
arr = [[0., 0., 1., 0.],
 [0., 0., 0., 1.],
 [1., 0., 0., 0.],
 [0., 1., 0., 0.]]
t3_2 = np.array_equal(computeMatrix(m,2,1), arr)

print(t3_1 and t3_2)

arr =quantumComputer(2,[QuantumGate(TypeOfQuantumGate.NOT,0)])
t4_1 = np.array_equal(arr,[0., 1., 0., 0.])

inp = [QuantumGate(TypeOfQuantumGate.NOT,2),QuantumGate(TypeOfQuantumGate.NOT,1) , QuantumGate(TypeOfQuantumGate.NOT,2)]
arr1 = quantumComputer(3,inp)
t4_2 = np.array_equal(arr1,[0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])

inp = [QuantumGate(TypeOfQuantumGate.NOT,2),QuantumGate(TypeOfQuantumGate.NOT,1) , QuantumGate(TypeOfQuantumGate.NOT,2),QuantumGate(TypeOfQuantumGate.HADAMARD,0)]
arr1 = quantumComputer(3,inp)
result = [0. +0.j, 0.+0.j, 0.70710678+0.j, 0.70710678+0.j,
 0.  +0.j, 0. +0.j ,0.+0.j, 0.+0.j]
t4_3 = (np.isclose(arr1,result).all())

print(t4_1 and t4_2)
print(t4_3)