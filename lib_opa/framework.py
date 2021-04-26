import numpy as np
import math


class Framework:
    #nt = 0
    def __init__(self, dt, T, dr, R):
        self.dt = dt
        self.T = T
        self.dr = dr
        self.R = R

    @property
    def nt(self):
        return 2**math.ceil(np.log2(self.T/self.dt))

    @property
    def t(self):
        return np.sort(-np.arange((-self.nt/2)*self.dt, (self.nt/2)*self.dt, self.dt))

    @property
    def w(self):
        return np.arange(-self.nt/2, self.nt/2)*2*np.pi / self.dt/self.nt

    @property
    def dw(self):
        return abs(self.w[0]-self.w[1])

    @property
    def nr(self):
        return self.R/self.dr - 1

    @property
    def r(self):
        return np.arange(0, self.nr*self.dr+self.dr, self.dr)