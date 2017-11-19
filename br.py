import numpy as np
import matplotlib.pyplot as plt

import parts
import circuit


ct = circuit.Circuit()
ct.parts = [
        parts.make_battery(0, 1, 5),
        parts.make_resistor(1, 2, 5),
        parts.make_capacitor(0, 2, 0.25),
        ]


circuit.initialize(ct)


hist = circuit.simulate(ct)


plt.plot(hist)
plt.show()


