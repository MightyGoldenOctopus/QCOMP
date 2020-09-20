# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:22:06 2020

@author: Pio
"""

import numpy as np 
from enum import Enum

from qiskit import QuantumCircuit, execute, Aer


#Enumration for each type of gate our quantum computer handle
class TypeOfQuantumGate(Enum):
    NOT = 1
    HADAMARD = 2 
    CNOT = 3

#The class quantum gate
#TypeOfGate is the type of the gate (a value of TypeOfQuantumGate)
#fQbit is the position in the circuit of the first input Qbit of the gate
#sQbit is the position in the circuit of the second input Qbit of the gate ( if the gate has two input)
class QuantumGate:
    def __init__(self, typeOfGate: TypeOfQuantumGate, fQbit: int, sQbit: int =0 ):
        self.typeOfGate = typeOfGate
        self.fQbit = fQbit
        self.sQbit = sQbit


#The main function, you need to program it without using qiskit
#nbQbits is the number of Qbits of the circuit
#QuantumGates is the list of quantum gates of the circuits
#This function output the state vector of the circuit after executing all the gate
def quantumComputer(nbQbits: int, quantumGates: list):
    qc = QuantumCircuit(nbQbits)
    sim = Aer.get_backend('statevector_simulator')
    for i in quantumGates:
        fQbit = i.fQbit
        sQbit = i.sQbit
        if(fQbit >= nbQbits or sQbit >= nbQbits ):
            raise Exception("One of the input qbit does not belong to the circuit, its value is to high")
        if(i.typeOfGate == TypeOfQuantumGate.HADAMARD):
            qc.h(fQbit)
        elif(i.typeOfGate == TypeOfQuantumGate.NOT):
            qc.x(fQbit)
        elif(i.typeOfGate == TypeOfQuantumGate.CNOT):
            qc.cx(fQbit, sQbit)
        else:
            raise Exception("Unknown Gate")
    job = execute(qc, sim)
    return job.result().get_statevector(qc)

# Test
#Empty test
assert(str(quantumComputer(3,[])) == "[1.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]")

#One Hadamard gate test
assert(str((quantumComputer(1,[QuantumGate(TypeOfQuantumGate.HADAMARD,0)])))== "[0.70710678+0.j 0.70710678+0.j]")

#One Hadamard gate test
(str((quantumComputer(2,[QuantumGate(TypeOfQuantumGate.NOT,0)]))))


#Multi gate test
l = [QuantumGate(TypeOfQuantumGate.NOT,0),QuantumGate(TypeOfQuantumGate.HADAMARD,0),QuantumGate(TypeOfQuantumGate.CNOT,0,1)]
string = str(quantumComputer(2,l))
assert(string == """[ 0.70710678-8.65956056e-17j  0.        +0.00000000e+00j
  0.        +0.00000000e+00j -0.70710678+8.65956056e-17j]""")

#Test of invalid qbit input
try:
    quantumComputer(1,[QuantumGate(TypeOfQuantumGate.HADAMARD,1)])    
except:
    pass
else:
    raise Exception("An error should have been raised")    
    
#Test of unknown gate
try:
    quantumComputer(1,[QuantumGate(1000,0)])    
except:
    pass
else:
    raise Exception("An error should have been raised")


arr =quantumComputer(1,[QuantumGate(TypeOfQuantumGate.HADAMARD,0)])
assert(np.isclose(arr,[1/math.sqrt(2), 1/math.sqrt(2) ]).all())    

arr =quantumComputer(1,[QuantumGate(TypeOfQuantumGate.NOT,0),QuantumGate(TypeOfQuantumGate.HADAMARD,0)])
assert(np.isclose(arr,[1/math.sqrt(2), -1/math.sqrt(2) ]).all())   

