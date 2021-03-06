import math 
import numpy as np 
from qiskit import QuantumCircuit, execute, Aer

def example():
    circuit = QuantumCircuit(1)
    circuit.h(0)
    return circuit

circuit = example()
sim = Aer.get_backend('statevector_simulator')
job = execute(circuit, sim)

arr = job.result().get_statevector(circuit)

print(circuit.draw())
assert(np.isclose(arr,[1/math.sqrt(2), 1/math.sqrt(2) ]).all())    
circuit.measure_all()
simulator = Aer.get_backend('qasm_simulator')
# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)
# Grab results from the job
result = job.result()
# Returns counts 
counts = result.get_counts(circuit) 
print(counts)

