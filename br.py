import numpy as np
import matplotlib.pyplot as plt

import parts


ct = parts.Circuit()
ct.nodes = np.arange(3)
ct.charges = np.zeros(3)
ct.parts = [
        parts.make_battery(0, 1, 5),
        parts.make_resistor(1, 2, 5),
        parts.make_capacitor(0, 2, 0.25),
        ]

hist = [ct.charges]

for t in range(50):
    new_charges = ct.charges.copy()

    for p in ct.parts:
        p.move_charges(ct.charges, new_charges)
    new_charges[0] = 0.0    # set the ground (hmmm...)

    ct.charges = new_charges

    hist.append(ct.charges)

hist = np.array(hist)
#print(hist[:,0])
#print(hist[:,1])
print(hist.shape)


plt.plot(hist)
plt.show()


