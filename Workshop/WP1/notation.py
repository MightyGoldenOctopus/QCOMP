# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:02:38 2020

@author: Pio
"""

from correction import *
from ref import quantumComputer as qC

#test empty input

arr = np.array([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])
t1_1 = np.array_equal(arr, quantumComputer(3,[]))
arr = np.array([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])
t1_2 = np.array_equal(arr, quantumComputer(2,[]))
arr = np.zeros([16])
arr[0] = 1
t1_3 = np.array_equal(arr, quantumComputer(4,[]))

print(t1_1 and t1_2 and t1_3 )

#test kronecker product

m1 = [0,2]
m2 = [[4,5],[6,7]]
t2_1 = np.array_equal(kroneckerProduct(m1,m2) , [[ 0,  0,  8, 10],[ 0,  0, 12, 14]])

m1 = [[4,5],[6,7]]
m2 = [[4,5],[6,7]]
t2_2   = np.array_equal(kroneckerProduct(m1,m2) , np.kron(m1,m2))

print(t2_1 and t2_2)

#test compute matrix

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

#test not gate

arr =quantumComputer(2,[QuantumGate(TypeOfQuantumGate.NOT,0)])
t4_1 = np.array_equal(arr,[0., 1., 0., 0.])

arr =quantumComputer(2,[QuantumGate(TypeOfQuantumGate.NOT,1)])
t4_2 = np.array_equal(arr,[0., 0., 1., 0.])

arr =quantumComputer(3,[QuantumGate(TypeOfQuantumGate.NOT,0)])
t4_3 = np.array_equal(arr,[0., 1., 0., 0.,0., 0., 0., 0.])

print(t4_1 and t4_2 and t4_3)

#test hadamard gate

arr =quantumComputer(1,[QuantumGate(TypeOfQuantumGate.HADAMARD,0)])
t5_1 = (np.isclose(arr,[1/math.sqrt(2), 1/math.sqrt(2) ]).all()) 

arr =quantumComputer(2,[QuantumGate(TypeOfQuantumGate.HADAMARD,0)])
t5_2 = (np.isclose(arr,[1/math.sqrt(2), 1/math.sqrt(2),0.,0. ]).all()) 

print(t5_1 and t5_2)

#test multi gate

arr =quantumComputer(2,[QuantumGate(TypeOfQuantumGate.HADAMARD,0),QuantumGate(TypeOfQuantumGate.HADAMARD,1)])
t6_1 = (np.isclose(arr,[1/math.sqrt(4), 1/math.sqrt(4),1/math.sqrt(4),1/math.sqrt(4) ]).all())

inp = [QuantumGate(TypeOfQuantumGate.NOT,2),QuantumGate(TypeOfQuantumGate.NOT,1) , QuantumGate(TypeOfQuantumGate.NOT,2)]
arr1 = quantumComputer(3,inp)
t6_2 = np.array_equal(arr1,[0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])

inp = [QuantumGate(TypeOfQuantumGate.NOT,2),QuantumGate(TypeOfQuantumGate.NOT,1) , QuantumGate(TypeOfQuantumGate.NOT,2),QuantumGate(TypeOfQuantumGate.HADAMARD,0)]
arr1 = quantumComputer(3,inp)
result = [0. +0.j, 0.+0.j, 0.70710678+0.j, 0.70710678+0.j,
 0.  +0.j, 0. +0.j ,0.+0.j, 0.+0.j]
t6_3 = (np.isclose(arr1,result).all())

print(t6_1 and t6_2 and t6_3)

#test ComputeCnot

arr = [[1., 0., 0., 0.],
 [0., 0., 0., 1.],
 [0., 0., 1., 0.],
 [0., 1., 0., 0.]]

t7_1 = np.array_equal(computeCNOT(2,0,1) , arr)


arr = [[1., 0., 0., 0.],
 [0., 1., 0., 0.],
 [0., 0., 0., 1.],
 [0., 0., 1., 0.]]

t7_2 = np.array_equal(computeCNOT(2,1,0) , arr)


print(t7_1 and t7_2)
#test CNOT

arr =quantumComputer(2,[QuantumGate(TypeOfQuantumGate.NOT,1),QuantumGate(TypeOfQuantumGate.CNOT,1,0)])
t8_1  = (np.array_equal(arr , [0,0,0,1]))

arr =quantumComputer(2,[QuantumGate(TypeOfQuantumGate.NOT,1),QuantumGate(TypeOfQuantumGate.CNOT,0,1)])
t8_2  = (np.array_equal(arr , [0,0,1,0]))

arr =quantumComputer(3,[QuantumGate(TypeOfQuantumGate.NOT,0),QuantumGate(TypeOfQuantumGate.CNOT,0,1),QuantumGate(TypeOfQuantumGate.CNOT,1,2)])
res = np.zeros([8])
res[7] = 1
t8_3  = (np.array_equal(arr , res))

print(t8_1 and t8_2 and t8_3)

#test compute proba

arr =quantumComputer(1,[QuantumGate(TypeOfQuantumGate.NOT,0),
                        QuantumGate(TypeOfQuantumGate.HADAMARD,0)])
t9_1 = (np.isclose(computeProbability(arr),[0.5,0.5]).all())

arr =quantumComputer(2,[QuantumGate(TypeOfQuantumGate.NOT,0),
                        QuantumGate(TypeOfQuantumGate.HADAMARD,0)])
t9_2 = (np.isclose(computeProbability(arr),[0.5,0.5,0.,0.]).all())

print(t9_1 and t9_2)