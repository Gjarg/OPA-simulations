import numpy as np
import sys
#from sellmeier import Sell


class Crystal:
    def __init__(self, name, angle):
        self.name = str(name)
        self.angle = angle


def n_PPLN(lin, T=None):

    l = lin*1e6

    #f = (T -24.5)*(T+570.82)
    F = (T-24.5)*(T+570.82)

    #a1 = 5.35583
    #a2 = 0.100473
    #a3 = 0.20692
    #a4 = 100
    #a5 = 11.34927
    #a6 = 0.015334
    #b1 = 4.629*1e-7
    #b2 = 3.862*1e-8
    #b3 = -0.89*1e-8
    #b4 = 2.657*1e-5

    return np.sqrt(5.756 + 2.86*1e-6 * F + (0.0983+4.7*1e-8*F)/(l**2-(0.202+6.113*1e-8*F)**2) + (189.32+1.516*1e-4*F)/(l**2-12.52**2)-1.32*1e-2*l**2)
