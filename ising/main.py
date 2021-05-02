import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import qiskit as qi
import buildCircuit
import analyticSolution
from analyticSolution import X,Z,I

def trueValues():
    H = analyticSolution.buildHamiltonian(1, 3)
    initialState = np.sqrt(1 / 2) * np.array([1, -1j, 0, 0])
    coeffs = analyticSolution.calcCoeffs(initialState, H)
    times = np.linspace(0, 3 * pi / 4, 100)
    states = analyticSolution.solution(coeffs, H, times)
    avgz1 = analyticSolution.expectation(states, np.kron(Z, I))
    avgz2 = analyticSolution.expectation(states, np.kron(I, Z))
    return (times, avgz1, avgz2)

def makePredictions(finalPhase, numSteps):
    circ = buildCircuit.buildCircuit(finalPhase, numSteps)
    backend = qi.Aer.get_backend('qasm_simulator')
    result = qi.execute(circ, backend=backend, shots=10000).result()
    counts = result.get_counts()
    avgs = buildCircuit.getResults(counts)
    return avgs

def main():
    trueVals = trueValues()
    fig, axes = plt.subplots(2,2, figsize=(9,6), dpi=200)
    axes = axes.reshape(4)
    ax = 0
    for numSteps in [1, 3, 5, 10]:
        z1Avgs = []
        z2Avgs = []
        angles = []
        for i in range(10):
            finalPhase = (3*pi/20)*i
            avgs = makePredictions(finalPhase, numSteps)
            z1Avgs.append(avgs[0])
            z2Avgs.append(avgs[1])
            angles.append(finalPhase)
        axes[ax].scatter(angles, z1Avgs, label=r"Site 1 (Simulated)")
        axes[ax].scatter(angles, z2Avgs, label=r"Site 2 (Simulated)")
        axes[ax].plot(trueVals[0]*2, trueVals[1], label=r"Site 1 (Analytic Solution)")
        axes[ax].plot(trueVals[0]*2, trueVals[2], label=r"Site 2 (Analytic Solution)")
        axes[ax].set_ylabel(r"$\langle \sigma_z \rangle$")
        axes[ax].set_xlabel(r"$2J\Delta t$")
        axes[ax].set_ylim(-1.1,1.1)
        axes[ax].set_xlim(-0.1, 3*pi/2)
        axes[ax].set_title("{} Trotter steps".format(numSteps))
        if ax == 0:
            axes[ax].legend()

        ax += 1
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()