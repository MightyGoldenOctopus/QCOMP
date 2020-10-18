from bloch import animate_bloch
import numpy as np
from qutip import *

states = []

thetas = np.linspace(0, np.pi/2, 21)

for theta in thetas:
    states.append((np.cos(theta/2)*basis(2,0) + np.sin(theta/2)*basis(2,1)).unit())

animate_bloch("qubit_hadamard", states, duration=0.1, save_all=False)