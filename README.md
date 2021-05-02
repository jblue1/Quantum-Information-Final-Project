# Quantum-Information-Final-Project
Final project for a quantum information class at Davidson College

## Ising
The ising folder contains code to do a digitial quantum circuit simulation of a 1-D transverse field Ising model with two spins. 
The ```main.py``` script will produce a plot showing the analytic solution of the expectation value of
the spin along the z axis for each site as well as the results from the simulation. As the number of
Trotter steps is increased, the simulation approaches the true values. An example of the results 
produced by ```main.py``` using IBM's Qasm simulator is below

<img src="https://github.com/jblue1/Quantum-Information-Final-Project/blob/main/imgs/IsingSimulationSimulation.png?raw=true" width=600>

And here are the results using IBM's Santiago quantum computer

<img src="https://github.com/jblue1/Quantum-Information-Final-Project/blob/main/imgs/IsingSimulationSantiago.png?raw=true" width=600>


## Heisenberg
The heisenberg folder contains code to use the Variational Quantum Eigensolver (VQE) algorithm to find the ground state energies
of a 2-D heisenburg model with four spins. Optimiziation is performed using the simultaneous perturbation stochastic approximation algorithm (SPSA)
implemented in the [noisyopt](https://noisyopt.readthedocs.io/en/latest/index.html) package. The circuit used to prepare the trail state consists
of alternating layers of single qubit Ry and Rz gates, and CNOT gates between each pair of qubits. The ```main.py``` script will produce a plot
showing the true ground state energy and ground state energy obtained using VQE for different ratios of the spin-spin coupling strength (J) and
the magnetic field strength (B). The script takes two arguments, the depth of the circuit preparing the trial state, and the number of iterations
to run SPSA. Example usage for a depth of 2 and 100 iterations of SPSA: ```python main.py 2 100```. The results using a depth of 3 and 1000 iterations
is shown below. 

<img src="https://github.com/jblue1/Quantum-Information-Final-Project/blob/main/imgs/VQEResults.png?raw=true" width=600>

