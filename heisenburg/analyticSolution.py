import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# Define necessary Pauli Matrices
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.array([[1, 0], [0, 1]])

def buildHamiltonian(j, b):
    first = [X, Y, Z, I, I, I, I, I, I, X, Y, Z]
    second = [X, Y, Z, X, Y, Z, I, I, I, I, I, I]
    third = [I, I, I, I, I, I, X, Y, Z, X, Y, Z]
    fourth = [I, I, I, X, Y, Z, X, Y, Z, I, I, I]

    zs = [[Z, I, I, I], [I, Z, I, I], [I, I, Z, I], [I, I, I, Z]]
    H = np.zeros((16, 16), dtype=np.complex128)
    for i in range(len(first)):
        H += j*(np.kron(np.kron(first[i], second[i]), np.kron(third[i], fourth[i])))
    for i in range(4):
        H += b*(np.kron(np.kron(zs[i][0], zs[i][1]), np.kron(zs[i][2], zs[i][3])))
    return H

def calcExpectation(state, O):
    return np.vdot(state, O@state)

def calcMagnetization(state):
    z1 = np.kron(np.kron(Z, I), np.kron(I, I))
    z2 = np.kron(np.kron(I, Z), np.kron(I, I))
    z3 = np.kron(np.kron(I, I), np.kron(Z, I))
    z4 = np.kron(np.kron(I, I), np.kron(I, Z))
    expZ = 0
    for O in [z1, z2, z3, z4]:
        #print(calcExpectation(state, O))
        expZ += calcExpectation(state, O)
    return expZ


def main():
    js = np.linspace(0, 1, 100)
    energies = []
    mags = []
    for j in js:
        H = buildHamiltonian(j, 1)
        vals, vecs = np.linalg.eigh(H)
        minIndex = np.argmin(vals)
        energies.append(vals[minIndex])

        netMag = calcMagnetization(vecs[:, minIndex])
        mags.append(netMag)
    
    plt.plot(js, np.array(energies) - np.array(mags))
    plt.show()
 


if __name__ == "__main__":
    main()