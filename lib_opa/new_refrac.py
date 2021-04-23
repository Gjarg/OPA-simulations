from abc import ABC, abstractmethod
import numpy as np
from scipy.constants import c


class Refractivee(ABC):
    ''' Refractive prop, common to all materials'''

    @classmethod
    @abstractmethod
    def n(cls, wavelength_mic, **kwargs):
        "index of refraction, !!wavelength in microns!!"
    @classmethod
    @abstractmethod
    def beta(cls, omega_center, omega_range, n):
        "return beta, omega_range corresponds to the range in Framework"


class Qpm(Refractivee, ABC):
    @staticmethod
    @abstractmethod
    def n_2(x, T=None):
        "refraction index, wavelength in microns"

    @classmethod
    def n(cls, wavelength, T=None):
        return np.sqrt(cls.n_2(wavelength, T))
    @classmethod
    def beta(cls, omega_center, omega_range,n):
        return (omega_range+omega_center)*n/c


class PPLN(Qpm):
    def n_2(lin, T=None):

        l = lin*1e6
        F = (T-24.5)*(T+570.82)

        return 5.756 + 2.86*1e-6 * F + (0.0983+4.7*1e-8*F)/(l**2-(0.202+6.113*1e-8*F)**2) + (189.32+1.516*1e-4*F)/(l**2-12.52**2)-1.32*1e-2*l**2


material_dict = {}
material_info_dict = {}
for cls in Qpm.__subclasses__():
    print(cls.__name__)
    material_dict[cls.__name__] = cls
    material_info_dict[cls.__name__] = cls
    #material_info_dict[cls.name] = cls


def get_material(name):
    """returns an instance of the material class corresponding to the name"""
    if name not in material_info_dict:
        raise Exception("Unknown material {}".format(name))
    return material_info_dict[name]
