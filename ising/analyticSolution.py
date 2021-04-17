import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# Define necessary Pauli Matrices
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.array([[1, 0], [0, 1]])


def buildHamiltonian(j, b):
    """Create matrix representation of the 2 site Ising Hamiltonian
    H = jX1X2 + (b/2)(Z1 + Z2)

    Args:
        j (float): Strength of spin-spin coupling
        b (float): Strength of magnetic field

    Returns:
        ndarray (4,4): Hamiltonian matrix
    """
    H = j * np.kron(X, X) + (b / 2) * (np.kron(Z, I) + np.kron(I, Z))
    return H


def calcCoeffs(state, H):
    """Given a state in the computational (Z) basis, calculate
    its representation in the basis of the eigenvectors of the
    Hamiltonian.


    Args:
        state (ndarray (4,)): State in the computational basis
        H (ndarray (4,4)): Hamiltonian matrix

    Returns:
        ndarray (4,): Representation of state in new basis
    """
    _, vecs = np.linalg.eig(H)
    sols = np.linalg.solve(vecs, state)
    return sols


def solution(coeffs, H, t):
    """Given the representation of some initial state in the basis of the
    eigenvalues of the Hamiltonian, evolve the state for time t using
    Schrodinger's equation.

    Args:
        coeffs (ndarray (4,)): Initial state in energy basis
        H (ndarray (4,4)): Hamiltonian matrix
        t (ndarray (N,)): Array of times

    Returns:
        ndarray (4, N): States at time t
    """
    vals, vecs = np.linalg.eig(H)
    ans = np.zeros((4, len(t)), dtype=np.complex128)
    for i in range(4):
        ans += coeffs[i] * vecs[:, i][:, np.newaxis] * np.exp(-1j * vals[i] * t)
    return ans


def expectation(state, O):
    """Calculate the inner product <state|O|state>

    Args:
        state (ndarray (4,N)): A set of states with which to calculate expectation values
        O (ndarray (4,4)): Observable with which to calculate an expectation value
    """
    print(state.shape)
    return np.sum(np.conjugate(state) * (O @ state), axis=0)


def main():
    H = buildHamiltonian(1, 3)
    initialState = np.sqrt(1 / 2) * np.array([1, -1j, 0, 0])
    coeffs = calcCoeffs(initialState, H)
    times = np.linspace(0, 3 * pi / 4, 100)
    states = solution(coeffs, H, times)
    avgz1 = expectation(states, np.kron(Z, I))
    avgz2 = expectation(states, np.kron(I, Z))
    plt.plot(avgz1)
    plt.plot(avgz2)
    plt.show()


if __name__ == "__main__":
    main()
