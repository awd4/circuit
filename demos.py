import numpy as np
import matplotlib.pyplot as plt

import parts
import circuit


def br():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 5),
            parts.make_resistor(1, 0, 5),
            ]
    return ct


def vd():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 5),
            parts.make_resistor(1, 2, 5),
            parts.make_resistor(2, 0, 3),
            ]
    return ct


def brc():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 5),
            parts.make_resistor(1, 2, 5),
            parts.make_capacitor(0, 2, 0.25),
            ]
    return ct


if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 1:
        sys.argv.append('None')

    if sys.argv[1].lower() == 'br':
        ct = br()
    elif sys.argv[1].lower() == 'vd':
        ct = vd()
    elif sys.argv[1].lower() == 'brc':
        ct = brc()

    circuit.initialize(ct)

    hist = circuit.simulate(ct)

    plt.plot(hist)
    plt.show()


