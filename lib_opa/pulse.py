import numpy as np
import math
from scipy.constants import c, epsilon_0
from lib_opa.framework import Framework


class Pulse:

    def __init__(self, lambda_c, duration, beta2, delay, energy, radius, Framework):

        self.lambda_c = lambda_c
        self.duration = duration
        self.w = Framework.w
        self.beta2 = beta2
        self.delay = delay
        self.energy = energy
        self.radius = radius
        self.t = Framework.t
        self.dt = Framework.dt
        # print(self.t,self.w)
        #self.wc = 2*np.pi*c / self.lambda_c
        #self.wp = c*2*np.pi / (self.lambda_c+ self.w)
        #self.lp = c*2*np.pi / self.wp

    @property
    def wc(self):
        return 2*np.pi*c/self.lambda_c

    @property
    def lp(self):
        tab = 2 * np.pi * c / (self.wc + self.w)
        r = list()
        for i in tab:
            if i < 0:
                r.append(0)
            else:
                r.append(i)
        del(tab)
        return np.array(r)
#        return tab

    # return np.nan_to_num(self.wc + f.w, copy= False , nan = 1)

    @property
    def lp_mic(self):
        return self.lp*1e6

    @property
    def pulse_t(self):
        et = np.exp(-((self.t-self.delay)*np.sqrt(2*np.log(2))/self.duration)**2)
        ew = np.fft.fftshift(np.fft.fft(et))
        ew = ew * (np.exp(-1j*(self.w**2*self.beta2/2))).T
        et = np.fft.ifft(np.fft.ifftshift(ew))
        return et

    @property
    def I(self):
        return abs(self.pulse_t**2)

    @property
    def ratio_energie(self):
        return (np.sum(self.I) * self.dt * 2.186594637045260 * c * epsilon_0 * np.pi * self.radius**2 / 2)

    @property
    def peak_elec_field(self):
        return np.max(abs(self.pulse_t)) * np.sqrt(self.energy/self.ratio_energie)

    @property
    def peak_intensity(self):
        return (2.186594637045260 * c * epsilon_0 * self.peak_elec_field**2 / (2))

    def find_nearest(self, a, vals):
        idx, val = min(enumerate(a), key=lambda x: abs(x[1]-vals))
        return idx

    def pulse_duration(self):
        val = np.max(self.I)
        idex = np.where(abs(self.pulse_t**2) == val)
        idx = idex[0][0]
        t1 = self.find_nearest(self.I[:int(idx)], val/2)
        t2 = self.find_nearest(self.I[int(idx)+1:], val/2)
        time_FWHM = np.round((t2+idx-t1)*self.dt*1e15, 1)*1e-15
        print(f'Pulse duration is:{np.round(time_FWHM*1e15,1)}fs')
        return time_FWHM

    def add_beta2(self, beta2):
        self.beta2 = self.beta2 + beta2

    def add_delay(self, delay):
        self.delay = self.delay + delay

    def refrac(self, l):
        return np.sqrt(8.2477 + 0.2881 / (l**2 - 0.1669) + 4927.5 / (l**2 - 1990.1))
