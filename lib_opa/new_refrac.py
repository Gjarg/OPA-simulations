from abc import ABC, abstractmethod
import numpy as np
from scipy.constants import c


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
    def beta(cls, omega_center, omega_range,n):
        return (omega_range + omega_center) * n / c

class PPLN(Qpm):
    def n_2(lin, T=None):

        l = lin*1e6
        F = (T-24.5)*(T+570.82)

        return 5.756 + 2.86*1e-6 * F + (0.0983+4.7*1e-8*F)/(l**2-(0.202+6.113*1e-8*F)**2) + (189.32+1.516*1e-4*F)/(l**2-12.52**2)-1.32*1e-2*l**2

class Uniaxial(Refractivee, ABC):
    @staticmethod
    @abstractmethod
    def nx_2(x, T=None):
        "refractive index along x axis"
    @staticmethod
    @abstractmethod
    def nz_2(x, T=None):
        "refractive index along x axis"

    @classmethod
    def nz(cls, wavelength, T=None):
        return np.sqrt(cls.nz_2(wavelength, T))
    @classmethod
    def nx(cls, wavelength, T=None):
        return np.sqrt(cls.nx_2(wavelength,T))

    @classmethod
    def n_theta(cls, wavelength, theta=None, T=None):
        nx = cls.nx(wavelength, T)
        nz = cls.nz(wavelength, T)
        return 1/np.sqrt(np.cos(theta)**2/nx**2+np.sin(theta)**2/nz**2)


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

# def n_BBO(lin, ax=None):

#     l = lin*1e6

#     if ax == 'e':

#         return np.sqrt(2.3730 + 0.0128 / (l**2 - 0.0156) - 0.0044 * l**2)

#     elif ax == 'o':

#         return np.sqrt(2.7405 + 0.0184 / (l**2 - 0.0179) - 0.0155 * l**2)

#     else:

#         raise Exception(
#             "The input is incorrect, ax must be equal to 'e' or 'o'")



material_dict = {}
material_info_dict = {}
for i in [Qpm.__subclasses__(), Uniaxial.__subclasses__()]:
    for cls in i:
        print(cls.__name__)
        material_dict[cls.__name__] = cls
        material_info_dict[cls.__name__] = cls


def get_material(name):
    """returns an instance of the material class corresponding to the name"""
    if name not in material_info_dict:
        raise Exception("Unknown material {}".format(name))
    return material_info_dict[name]
