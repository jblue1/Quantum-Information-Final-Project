import numpy as np
from numpy import pi
import qiskit as qi


def prepareState():
    circ = qi.QuantumCircuit(2)
    circ.h(0)
    circ.rz(pi / 2, 0)
    circ.rz(pi / 2, 1)
    gate = circ.to_gate()
    return gate


def trotterStep(dt):
    circ = qi.QuantumCircuit(3)
    circ.rz(3 * dt, [0, 1])
    circ.h([0, 1])
    circ.cx(0, 2)
    circ.cx(1, 2)
    circ.rz(2 * dt, 2)
    circ.cx(1, 2)
    circ.cx(0, 2)
    circ.h([0, 1])
    gate = circ.to_gate()
    return gate


def buildCircuit(finalPhase, numSteps):
    dt = finalPhase / (2 * numSteps)
    circ = qi.QuantumCircuit(3, 2)
    prep_gate = prepareState()
    trotterGate = trotterStep(dt)
    circ.append(prep_gate, [0, 1])
    for _ in range(numSteps):
        circ.append(trotterGate, [0, 1, 2])

    circ.measure([0, 1], [0, 1])

    return circ


def getResults(counts):
    shots = 0
    firstQubit0s = 0
    firstQubit1s = 0
    secondQubit0s = 0
    secondQubit1s = 0
    for key in counts:
        shots += counts[key]
        if key[0] == "0":
            firstQubit0s += counts[key]
        if key[0] == "1":
            firstQubit1s += counts[key]
        if key[1] == "0":
            secondQubit0s += counts[key]
        if key[1] == "1":
            secondQubit1s += counts[key]

    z1Avg = (firstQubit0s - firstQubit1s) / shots
    z2Avg = (secondQubit0s - secondQubit1s) / shots
    return (z1Avg, z2Avg)