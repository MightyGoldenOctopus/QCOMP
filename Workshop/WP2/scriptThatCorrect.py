

from correction.bellState import *
from correction.AND import *
from correction.QFT3 import qft as qft3
from correction.deutsch import deutsch, dj_oracle
from correction.QFTN import qft as qftn
circuit =bellState()

#test bellState
def testBellState():
    circuit = bellState()
    sim = Aer.get_backend('statevector_simulator')
    job = execute(circuit, sim)
    arr = job.result().get_statevector(circuit)
    b0 = (np.isclose(arr,[1/math.sqrt(2),0,0, 1/math.sqrt(2)]).all()) 
    b1 = (np.isclose(arr,[0, 1/math.sqrt(2), 1/math.sqrt(2),0]).all() )
    return (b0 or b1)
     

t1 = False
try:
    t1 =testBellState()
except:
    pass

#test AND
def testAND():
    circuit = AND()
    yourCircuit = circuit.to_gate()
    circuitForTest = QuantumCircuit(3)
    circuitForTest.x(1)
    circuitForTest.append(yourCircuit,[0,1,2])
    sim = Aer.get_backend('statevector_simulator')
    job = execute(circuitForTest, sim)
    arr = job.result().get_statevector(circuitForTest) 
    print(arr)
    tab = [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]
    tab2 = [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]
    tab3 = [0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]
    tab4 = [0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]
    return(np.isclose(arr,tab).all()  or np.isclose(arr,tab2).all() 
    or np.isclose(arr,tab3).all() or np.isclose(arr,tab4).all())
         

t2 = False
try:
    t2 =testAND()
except:
    pass

#test QFT3
def testQFT3():
    circuit = qft3()
    qftCircuit = circuit.to_gate()
    circuitForTest = QuantumCircuit(3)
    circuitForTest.x(0)
    circuitForTest.x(1)
    circuitForTest.x(2)
    circuitForTest.append(qftCircuit,[0,1,2])
    sim = Aer.get_backend('statevector_simulator')
    job = execute(circuitForTest, sim)
    arr = job.result().get_statevector(circuitForTest) 
    tab = [ 3.53553391e-01-1.29893408e-16j,  2.50000000e-01-2.50000000e-01j,
 -1.51542310e-16-3.53553391e-01j, -2.50000000e-01-2.50000000e-01j,
 -3.53553391e-01+1.29893408e-16j, -2.50000000e-01+2.50000000e-01j,
  1.51542310e-16+3.53553391e-01j,  2.50000000e-01+2.50000000e-01j]
    return (np.isclose(arr,tab).all())
        
         

t3 = False
try:
    t3 = testQFT3()
except:
    pass

#test deutch
def testDeutch():  
    circuit = deutsch(dj_oracle("constant"))
    circuit.measure_all()
    backend = BasicAer.get_backend('qasm_simulator')
    shots = 1024
    results = execute(circuit, backend=backend, shots=shots).result()
    answer = results.get_counts()
    a = (answer['00'] + answer['10']== 1024)
    circuit = deutsch(dj_oracle("balanced"))
    circuit.measure_all()
    results = execute(circuit, backend=backend, shots=shots).result()
    answer = results.get_counts()
    b = (answer['01'] + answer['11'] == 1024)
    return a and b
     

t4 = False
try:
    t4 = testDeutch()
except:
    pass

#test QFTN
def testQFTN():
    circuit = qftn(5)
    qftCircuit = circuit.to_gate()
    circuitForTest = QuantumCircuit(5)
    circuitForTest.x(2)
    circuitForTest.append(qftCircuit,[0,1,2,3,4])
    sim = Aer.get_backend('statevector_simulator')
    job = execute(circuitForTest, sim)
    arr = job.result().get_statevector(circuitForTest) 
    tab = [ 1.76776695e-01-2.16489014e-17j,  1.25000000e-01+1.25000000e-01j,
  3.24733521e-17+1.76776695e-01j, -1.25000000e-01+1.25000000e-01j,
 -1.76776695e-01+2.16489014e-17j, -1.25000000e-01-1.25000000e-01j,
 -3.24733521e-17-1.76776695e-01j, 1.25000000e-01-1.25000000e-01j,
  1.76776695e-01-2.16489014e-17j,  1.25000000e-01+1.25000000e-01j,
  3.24733521e-17+1.76776695e-01j, -1.25000000e-01+1.25000000e-01j,
 -1.76776695e-01+2.16489014e-17j, -1.25000000e-01-1.25000000e-01j,
 -3.24733521e-17-1.76776695e-01j,  1.25000000e-01-1.25000000e-01j,
  1.76776695e-01-2.16489014e-17j,  1.25000000e-01+1.25000000e-01j,
  3.24733521e-17+1.76776695e-01j, -1.25000000e-01+1.25000000e-01j,
 -1.76776695e-01+2.16489014e-17j, -1.25000000e-01-1.25000000e-01j,
 -3.24733521e-17-1.76776695e-01j,  1.25000000e-01-1.25000000e-01j,
  1.76776695e-01-2.16489014e-17j, 1.25000000e-01+1.25000000e-01j,
  3.24733521e-17+1.76776695e-01j, -1.25000000e-01+1.25000000e-01j,
 -1.76776695e-01+2.16489014e-17j, -1.25000000e-01-1.25000000e-01j,
 -3.24733521e-17-1.76776695e-01j,  1.25000000e-01-1.25000000e-01j] 
    return (np.isclose(arr,tab).all())
               
     

t5 = False
try:
    t5 =testQFTN()
except:
    pass