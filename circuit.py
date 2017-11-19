import numpy as np


class Circuit:
    def __init__(self):
        self.parts = []
        self.charges = None


def initialize(circuit):
    ct = circuit
    nodes = set( [n for p in ct.parts for n in p.nodes()] )
    ct.charges = np.zeros(len(nodes))


def simulate(circuit, steps=50):
    ct = circuit
 
    hist = [ct.charges.copy()]

    for t in range(steps):
        new_charges = ct.charges.copy()

        for p in ct.parts:
            p.move_charges(ct.charges, new_charges)
        new_charges[0] = 0.0    # set the ground (hmmm...)

        ct.charges = new_charges

        hist.append(ct.charges)

    return np.array(hist)


