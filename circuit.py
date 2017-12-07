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
 
    hist = [ct.charges.copy() - ct.charges[0]]

    for t in range(steps):

        c1 = ct.charges.copy()
        c2 = c1.copy()

        N = 8
        for i in range(N):

            for p in ct.parts:
                p.move_charges(c1, c2)

            diff = c2 - c1
            c2 = c1 + diff / N

            c1 = c2
            c2 = c1.copy()

        ct.charges = c2

        hist.append(ct.charges - ct.charges[0])

    return np.array(hist)


