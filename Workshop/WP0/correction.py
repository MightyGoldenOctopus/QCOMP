from qiskit import *
import numpy as np


def nearestValue(arr, x):
    # YOUR CODE GOES HERE
    return arr[np.abs(arr - x).argmin()]
    ###

def mostFrequent(arr):
    # YOUR CODE GOES HERE
    return np.bincount(arr).argmax()
    ###

def kroneckerProduct(m1, m2):
    # YOUR CODE GOES HERE
    return np.kron(m1, m2)
    ###

def kroneckerProductBonus(m1, m2):
    # YOUR CODE GOES HERE
    
    # final_list = []
    # sub_list = []
 
    # count = len(m2)
 
    # for elem1 in m1:
    #     counter = 0
    #     check = 0
    #     while check < count:
    #         for num1 in elem1:
    #             for num2 in m2[counter]:
    #                 sub_list.append(num1 * num2)
    #         counter += 1
    #         final_list.append(sub_list)
    #         sub_list = []
    #         check +=1
    # return final_list

    return [[num1 * num2 for num1 in elem1 for num2 in m2[row]] for elem1 in m1 for row in range(len(m2))]
    ###


def NOT(input):

    q = QuantumRegister(1) # a qubit in which to encode and manipulate the input
    c = ClassicalRegister(1) # a bit to store the output
    qc = QuantumCircuit(q, c) # this is where the quantum program goes
    
    # We encode '0' as the qubit state |0⟩, and '1' as |1⟩
    # Since the qubit is initially |0⟩, we don't need to do anything for an input of '0'
    # For an input of '1', we do an x to rotate the |0⟩ to |1⟩
    if input=='1':
        qc.x( q[0] )
        
    # Now we've encoded the input, we can do a NOT on it using x
    qc.x( q[0] )
    
    # Finally, we extract the |0⟩/|1⟩ output of the qubit and encode it in the bit c[0]
    qc.measure( q[0], c[0] )
    
    # We'll run the program on a simulator
    backend = Aer.get_backend('qasm_simulator')
    # Since the output will be deterministic, we can use just a single shot to get it
    job = execute(qc,backend,shots=1)
    output = next(iter(job.result().get_counts()))
    
    return output


def XOR(input1,input2):
    
    q = QuantumRegister(2) # two qubits in which to encode and manipulate the input
    c = ClassicalRegister(1) # a bit to store the output
    qc = QuantumCircuit(q, c) # this is where the quantum program goes
    
    # YOUR QUANTUM PROGRAM GOES HERE    
    if input1 == '1':
        qc.x(q[0])
    if input2 == '1':
        qc.x(q[1])
    qc.cnot(q[0], q[1])
    ###

    qc.measure(q[1],c[0]) # YOU CAN CHANGE THIS IF YOU WANT TO
    
    # We'll run the program on a simulator
    backend = Aer.get_backend('qasm_simulator')
    # Since the output will be deterministic, we can use just a single shot to get it
    job = execute(qc,backend,shots=1,memory=True)
    output = job.result().get_memory()[0]
    
    return output