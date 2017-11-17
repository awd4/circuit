
CHARGES_PER_VOLT = 100.0


class Circuit:
    def __init__(self):
        self.parts = []
        self.nodes = []
        self.charges = []


class Battery:
    def __init__(self):
        self.neg = None
        self.pos = None
        self.charges = None
    def move_charges(self, old_charges, new_charges):
        n, p = self.neg, self.pos
        new_charges[p] = old_charges[n] + self.charges


class Resistor:
    def __init__(self):
        self.n1 = None
        self.n2 = None
        self.ohms = None
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
    def move_charges(self, old_charges, new_charges):
        n1, n2 = self.n1, self.n2
        c1 = old_charges[n1]
        c2 = old_charges[n2]
        c_diff = c2 - (c1 + self.charges)
        c_diff *= self.capacitance
        new_charges[n2] -= c_diff
        self.charges += c_diff


def make_battery(neg_node, pos_node, volts):
    b = Battery()
    b.charges = CHARGES_PER_VOLT * volts
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


