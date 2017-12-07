
CHARGES_PER_VOLT = 100.0


class Battery:
    def __init__(self):
        self.neg = None
        self.pos = None
        self.volts = None
        self.internal_resistance = 0.1
        self.current = 5.0
    def nodes(self):
        return [self.neg, self.pos]
    def move_charges(self, old_charges, new_charges):
        n, p, old, new = self.neg, self.pos, old_charges, new_charges
        goal = self.volts * CHARGES_PER_VOLT
        curr = old[p] - old[n]

        diff = goal - curr
        I = diff / self.internal_resistance
        jump = max(0, min(I, old[n]))
        add = max(0, I - jump)
        new[n] -= jump
        new[p] += jump
        new[p] += add


class Resistor:
    def __init__(self):
        self.n1 = None
        self.n2 = None
        self.ohms = None
    def nodes(self):
        return [self.n1, self.n2]
    def move_charges(self, old_charges, new_charges):
        n1, n2 = self.n1, self.n2
        c1 = old_charges[n1]
        c2 = old_charges[n2]
        c_diff = (c1 - c2) / self.ohms
        if c_diff == 0.0:
            return
        new_charges[n1] -= c_diff
        new_charges[n2] += c_diff


class Capacitor:
    def __init__(self):
        self.n1 = None
        self.n2 = None
        self.capacitance = None
        self.charges = 0.0
    def nodes(self):
        return [self.n1, self.n2]
    def move_charges(self, old_charges, new_charges):
        n1, n2 = self.n1, self.n2
        c1 = old_charges[n1]
        c2 = old_charges[n2]
        c_diff = c2 - (c1 + self.charges)
        c_diff *= self.capacitance
        new_charges[n2] -= c_diff
        self.charges += c_diff


class Diode:
    def __init__(self):
        self.anode = None
        self.cathode = None
        self.bias = None
        self.effective_resistance = 0.1
    def nodes(self):
        return [self.anode, self.cathode]
    def move_charges(self, old_charges, new_charges):
        a, c = self.anode, self.cathode
        c1 = old_charges[a]
        c2 = old_charges[c]
        c_diff = c1 - c2 - CHARGES_PER_VOLT * self.bias
        if c_diff > 0.0:
            I = c_diff / self.effective_resistance
            new_charges[a] -= I
            new_charges[c] += I


def make_battery(neg_node, pos_node, volts):
    b = Battery()
    b.volts = volts
    b.neg = neg_node
    b.pos = pos_node
    return b


def make_resistor(a_node, b_node, ohms):
    r = Resistor()
    r.ohms = ohms
    r.n1 = a_node
    r.n2 = b_node
    return r


def make_capacitor(a_node, b_node, capacitance):
    c = Capacitor()
    c.n1 = a_node
    c.n2 = b_node
    c.capacitance = capacitance
    return c


def make_diode(anode, cathode, bias=0.7):
    d = Diode()
    d.anode = anode
    d.cathode = cathode
    d.bias = bias
    return d


