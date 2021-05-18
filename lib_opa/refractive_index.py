import numpy as np
from lib_opa.pulse import Pulse
from lib_opa.opa import Opa
from lib_opa.crystal import Crystal


class Refractive:
    def __init__(self, Pulse, Opa, Crystal):
        self.l_mic = Pulse.lp_mic
        self.pump_polar = Opa.pump_polar
        self.signal_polar = Opa.signal_polar
        self.idler_polar = Opa.idler_polar
        self.theta = Crystal.theta
        self.name = Crystal.name
        self.phi = phi
        self.plan = plan

    def n(self):
        return np.sqrt(self.n_2)

    def ne_theta(self, no, ne, theta):
        return 1 / np.sqrt(np.sin(theta) ** 2 / ne ** 2 + np.cos(theta) ** 2 / no ** 2)
