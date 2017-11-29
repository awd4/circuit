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


def vdiv():
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


def brd():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 5),
            parts.make_resistor(1, 2, 5),
            parts.make_diode(2, 0, 0.7),
            ]
    return ct


if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 1:
        sys.argv.append('None')

    if sys.argv[1].lower() == 'br':
        ct = br()
    elif sys.argv[1].lower() == 'vdiv':
        ct = vdiv()
    elif sys.argv[1].lower() == 'brc':
        ct = brc()
    elif sys.argv[1].lower() == 'brd':
        ct = brd()

    circuit.initialize(ct)

    hist = circuit.simulate(ct)

    plt.plot(hist)
    plt.show()


