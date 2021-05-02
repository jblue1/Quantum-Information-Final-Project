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
