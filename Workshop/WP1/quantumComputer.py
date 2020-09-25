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
    pass