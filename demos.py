import numpy as np
import matplotlib.pyplot as plt

import parts
import circuit


def br():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 10),
            parts.make_resistor(1, 0, 10),
            ]
    return ct


def bbr():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 5),
            parts.make_battery(1, 2, 5),
            parts.make_resistor(2, 0, 10),
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


def rgrid():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 8, 5),
            parts.make_resistor(0, 1, 1),
            parts.make_resistor(0, 3, 2),
            parts.make_resistor(1, 2, 1),
            parts.make_resistor(1, 4, 1),
            parts.make_resistor(2, 5, 1),
            parts.make_resistor(3, 4, 2),
            parts.make_resistor(3, 6, 2),
            parts.make_resistor(4, 5, 1),
            parts.make_resistor(4, 7, 2),
            parts.make_resistor(5, 8, 1),
            parts.make_resistor(6, 7, 2),
            parts.make_resistor(7, 8, 2),
            ]
    return ct


def npn():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 5),
            parts.make_resistor(1, 2, 5),
            parts.make_resistor(1, 3, 10),
            parts.make_resistor(3, 0, 8.9),
            parts.make_npn(2, 3, 0),
            ]
    return ct


def pnp():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 5),
            parts.make_pnp(1, 2, 3),
            parts.make_resistor(1, 2, 1),
            parts.make_resistor(2, 0, 20),
            parts.make_resistor(3, 0, 5),
            ]
    return ct


def and_gate():
    ct = circuit.Circuit()
    ct.parts = [
            parts.make_battery(0, 1, 5),
            parts.make_battery(0, 2, 5),    # A
            parts.make_battery(0, 3, 5),    # B
            parts.make_npn(1, 2, 4),
            parts.make_npn(4, 3, 5),
            parts.make_resistor(5, 0, 20),  # Node 5 = A & B
            ]
    return ct


if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 1:
        sys.argv.append('None')

    if sys.argv[1].lower() == 'br':
        ct = br()
    elif sys.argv[1].lower() == 'bbr':
        ct = bbr()
    elif sys.argv[1].lower() == 'vdiv':
        ct = vdiv()
    elif sys.argv[1].lower() == 'brc':
        ct = brc()
    elif sys.argv[1].lower() == 'brd':
        ct = brd()
    elif sys.argv[1].lower() == 'rgrid':
        ct = rgrid()
    elif sys.argv[1].lower() == 'npn':
        ct = npn()
    elif sys.argv[1].lower() == 'pnp':
        ct = pnp()
    elif sys.argv[1].lower() == 'and-gate':
        ct = and_gate()

    circuit.initialize(ct)

    hist = circuit.simulate(ct, steps=400)

    plt.plot(hist[:,1:])
    plt.show()


