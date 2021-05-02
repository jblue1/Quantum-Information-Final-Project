import analyticSolution
import circuits
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from noisyopt import minimizeSPSA
import sys


def usage(message):
    print(message)
    print("Usage: ")
    print("python main.py numIters depth")
    print("    numIters - Number of iterations to run optimization algorithm")
    print(
        "    depth - Number of entangling layers to use in circuit preparing the trial state"
    )


def main():
    numIters = int(sys.argv[1])
    depth = int(sys.argv[2])
    analyticJs = np.linspace(0, 1, 500)
    evaluateJs = np.linspace(0, 1, 5)
    true_e = []
    evaluated_e = []
    for j in analyticJs:
        b = 1
        H = analyticSolution.buildHamiltonian(j, b)
        vals, vecs = np.linalg.eig(H)
        minIndex = np.argmin(vals)
        true_e.append(vals[minIndex])

    for j in evaluateJs:
        print("J/B Ratio : {}".format(j))
        b = 1
        thetas = np.random.uniform(0, 2 * pi, size=((depth + 1) * 8,))
        result = minimizeSPSA(
            circuits.costFnx, thetas, (j, depth), paired=False, niter=numIters
        )
        print("Optimizer message: {}".format(result.message))
        evaluated_e.append(circuits.costFnx(result.x, j, depth))
    plt.plot(analyticJs, true_e, label="True ground state energy")
    plt.scatter(evaluateJs, evaluated_e, label="Ground state energy from VQE", c="r")
    plt.xlabel(r"$J/B$")
    plt.ylabel(r"Energy (a.u)")
    plt.title("Ground state energy of four site Heisenberg Model")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()