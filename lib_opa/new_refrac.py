from abc import ABC, abstractmethod
import numpy as np
from scipy.constants import c
import sys


class Refractivee(ABC):

    ''' Common to all materials'''

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
    def beta(cls, omega_center, omega_range, n):
        return (omega_range + omega_center) * n / c


class PPLN(Qpm):
    def n_2(lin, T=None):

        x = lin*1e6
        F = (T-24.5)*(T+570.82)

        return 5.756 + 2.86*1e-6 * F + (0.0983+4.7*1e-8*F)/(x**2-(0.202+6.113*1e-8*F)**2) + (189.32+1.516*1e-4*F)/(x**2-12.52**2)-1.32*1e-2*x**2


class Uniaxial(Refractivee, ABC):
    @staticmethod
    @abstractmethod
    def nx_2(x, T=None):
        "refractive index along x axis"
    @staticmethod
    @abstractmethod
    def nz_2(x, T=None):
        "refractive index along z axis"

    @classmethod
    def nz(cls, wavelength, T=None):
        return np.sqrt(cls.nz_2(wavelength, T))

    @classmethod
    def nx(cls, wavelength, T=None):
        return np.sqrt(cls.nx_2(wavelength, T))

    @classmethod
    def n_theta(cls, wavelength, theta=None, T=None):
        nx = cls.nx(wavelength, T)
        nz = cls.nz(wavelength, T)
        return 1 / np.sqrt(np.cos(theta) ** 2 / nx ** 2 + np.sin(theta) ** 2 / nz ** 2)

    @classmethod
    def beta(cls, omega_center, omega_range, n):
        return (omega_range + omega_center) * n / c


class Biaxial(Refractivee, ABC):
    @staticmethod
    @abstractmethod
    def nz_2(x, T=None):
        "refractive index along z axis"

    @staticmethod
    @abstractmethod
    def ny_2(x, T=None):
        "refractive index along y axis"

    @staticmethod
    @abstractmethod
    def nx_2(x, T=None):
        "refractive index along x axis"

    @classmethod
    def nz(cls, wavelength, T=None):
        return np.sqrt(cls.nz_2(wavelength, T))

    @classmethod
    def ny(cls, wavelength, T=None):
        return np.sqrt(cls.ny_2(wavelength, T))

    @classmethod
    def nx(cls, wavelength, T=None):
        return np.sqrt(cls.nx_2(wavelength, T))

    @classmethod
    def n_angle(cls, wavelength, theta=None, phi=None, T=None,plan=None):
        if plan == 'XZ':
            if phi != 0:
                print('Phi should be equal to 0 degres')
                sys.exit()
            else:
                return 12
        if plan == 'XY':
            if theta != 90:
                print('Theta should be equal to 90 degres')
                sys.exit()
            else:
                return 1/np.sqrt((np.cos(phi)/cls.ny(wavelength))**2+(np.sin(phi)/cls.nx(wavelength))**2)
        if plan == 'YZ':
            if phi != 90:
                print('Phi should be equal to 90 degres')
                sys.exit()
            else:
                return 12



    @classmethod
    def beta(cls, omega_center, omega_range, n):
        return (omega_range + omega_center) * n / c


class BBO(Uniaxial):
    '''Tamošauskas, G., Beresnevičius, G., Gadonas, D., & Dubietis, A. (2018).
    Transmittance and phase matching of BBO crystal in the 3−5 μm range and its
     application for the characterization of mid-infrared laser pulses. Optical Materials Express,
      8(6), 1410. doi:10.1364/ome.8.001410 '''

    def nx_2(lin, T=None):
        x = lin*1e6
        return 1+(0.90291*x**2/(x**2-0.003926))+(0.83155*x**2/(x**2-0.018786))+(0.76536*x**2/(x**2-60.01))

    def nz_2(lin, T=None):
        x = lin*1e6
        return 1+(1.151075*x**2/(x**2-0.007142))+(0.21803*x**2/(x**2-0.02259))+(0.656*x**2/(x**2-263))


class NL(Uniaxial):

    def nx_2(lin, T=None):
        x = lin*1e6
        return np.sqrt(4.9048 - 0.11768/(0.04750-x**2)-0.027169*x**2)

    def nz_2(lin, T=None):
        x = lin * 1e6
        return np.sqrt(4.5820-0.099169/(0.044432-x**2)-0.021950*x**2)

class LBO(Biaxial):
    '''K. Kato: IEEE J. QE-26, 1173 (1990): Tunable UV Generation to 0.2325 pm in LiB305. doi: 10.1109/3.59655'''

    def nx_2(lin, T=None):
        x = lin*1e6
        return 2.4542 + (0.01125 / (x ** 2 - 0.001135)) - 0.01388 * x ** 2

    def ny_2(lin, T=None):
        x = lin*1e6
        return 2.5390 + (0.01277 / (x ** 2 - 0.01189)) - 0.01848 * x ** 2

    def nz_2(lin, T=None):
        x = lin*1e6
        return 2.5865 + (0.01310/(x**2-0.01223))- 0.01861*x**2


material_dict = {}
material_info_dict = {}
for i in [Qpm.__subclasses__(), Uniaxial.__subclasses__(), Biaxial.__subclasses__()]:
    for cls in i:
        print(cls.__name__)
        material_dict[cls.__name__] = cls
        material_info_dict[cls.__name__] = cls


def get_material(name):
    """returns an instance of the material class corresponding to the name"""
    if name not in material_info_dict:
        raise Exception("Unknown material {}".format(name))
    return material_info_dict[name]
