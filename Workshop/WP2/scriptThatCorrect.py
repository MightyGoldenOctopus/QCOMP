

from correction.bellState import *
from correction.AND import *

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
