import math 
import numpy as np 
from numpy import pi
from qiskit import QuantumCircuit, execute, Aer
from qiskit.quantum_info.operators import Operator

def qft():
    pass

circuit = qft()

#Lets print the circuit
print(circuit.draw())


#Lets verify the state vector
qftCircuit = circuit.to_gate()
circuitForTest = QuantumCircuit(3)
circuitForTest.x(0)
circuitForTest.x(1)
circuitForTest.append(qftCircuit,[0,1,2])
sim = Aer.get_backend('statevector_simulator')
job = execute(circuitForTest, sim)
arr = job.result().get_statevector(circuitForTest) 
tab = [ 3.53553391e-01-8.65956056e-17j, -1.08244507e-16-3.53553391e-01j,
 -3.53553391e-01+8.65956056e-17j,  1.08244507e-16+3.53553391e-01j,
 -2.50000000e-01+2.50000000e-01j,  2.50000000e-01+2.50000000e-01j,
  2.50000000e-01-2.50000000e-01j, -2.50000000e-01-2.50000000e-01j]
assert(np.isclose(arr,tab).all())    


#Lets execute our circuit
circuit.measure_all()
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1000)
result = job.result()
counts = result.get_counts(circuit) 
print(counts)

