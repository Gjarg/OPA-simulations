import numpy as np

def n_KTA (lin, ax = None):
    
    l = lin*1e6

    if ax == 'nx':

        nx = np.sqrt(2.1495 + 1.0203*l**1.9951/(l**1.9951-0.042378) + 0.5531*l**1.9567/(l**1.9567-72.3045))
        return nx

    elif ax == 'ny':  

        ny = np.sqrt(2.1308 + 1.0564*l**2.0017/(l**2.0017-0.042523) + 0.6927*l**1.7261 / (l**1.7261-54.8505))
        return ny 

    elif ax == 'nz':

        nz = np.sqrt(2.1931 +1.2382*l**1.8920/(l**1.8920-0.059171) + 0.5088*l**2/(l**2-53.2898))
        return nz

    else:

        raise Exception("The input is incorrect, ax must be equal to 'nx' or 'ny' or 'nz' ")



def n_LGS (lin, ax = None):

    #Isaenko et al-2003-Crystal Research and Technology, https://www.researchgate.net/publication/285971031_Isaenko_et_al-2003-Crystal_Research_and_Technology
    l = lin*1e6

    if ax == 'nx':

        A = 4.326834
        B = 0.1030907
        C = 0.0309876
        D = 0.0037015

    elif ax == 'ny':

        A = 4.478907
        B = 0.120426
        C = 0.034616
        D = 0.0035119

    elif ax == 'nz':

        A = 4.493881
        B = 0.1177452
        C = 0.0337004
        D = 0.0037767

    else:
        raise Exception("The input is incorrect, ax must be equal to 'nx' or 'ny' or 'nz' ")


    return np.sqrt(A + B/(l**2-C)-D*l**2)



def n_NL (lin, ax = None):

    l = lin*1e6

    if ax == 'e':

        return np.sqrt(4.5820-0.099169/(0.044432-l**2)-0.021950*l**2)

    elif ax == 'o':

        return np.sqrt(4.9048 - 0.11768/(0.04750-l**2)-0.027169*l**2)

    else:

        raise Exception("The input is incorrect, ax must be equal to 'e' or 'o'")






def n_GaSe(lin, ax = None):

    l = lin*1e6

    if ax == 'e': 

        return np.sqrt(8.2477 + 0.2881 / (l**2 - 0.1669) + 4927.5 / (l**2 - 1990.1))

    elif ax == 'o':

        return np.sqrt(10.6409 + 0.3788 / (l**2 - 0.1232) + 7090.7 / (l**2 - 2216.3))

    else:

        raise Exception("The input is incorrect, ax must be equal to 'e' or 'o'")



def n_BBO(lin, ax = None):

    l = lin*1e6

    if ax == 'e': 

        return np.sqrt(2.3730 + 0.0128 / (l**2 - 0.0156) - 0.0044 * l**2 )
 
    elif ax == 'o':

        return np.sqrt(2.7405 + 0.0184 / (l**2 - 0.0179) - 0.0155 * l**2 )
 
    else:

        raise Exception("The input is incorrect, ax must be equal to 'e' or 'o'")

def n_LBO (lin, ax = None):
    
    l = lin*1e6

    if ax == 'nx':

        nx = np.sqrt(2.45768 + 0.0098877 /(l**2 - 0.026095) - 0.013847 * l**2)
        return nx

    elif ax == 'ny':  

        ny = np.sqrt(2.52500 + 0.017123 /(l**2 + 0.0060517) -0.0087838* l**2)
        return ny 

    elif ax == 'nz':

        nz = np.sqrt(2.58488 + 0.012737 / (l**2-0.021414)-0.016293*l**2)
        return nz

    else:

        raise Exception("The input is incorrect, ax must be equal to 'nx' or 'ny' or 'nz' ")



def n_AGS(lin, ax = None):
    "Lim 0.54-12.9. New data on the nonlinear Optical constant, Phase Matching, and Optical Damage of AgGaS2. KATO 1996 "

    l = lin*1e6

    if ax == 'e': 

        return np.sqrt(5.54120 + 0.22041/(l**2-0.09824)-2.5240*1e-3*l**2+3.6214*1e-7*l**4-8.3605*1e-9*l**6)
 
    elif ax == 'o':

        return np.sqrt(5.79419 + 0.23114/(l**2-0.06882)-2.4534*1e-3*l**2+3.1814*1e-7*l**4-9.7051*1e-9*l**6)
 
    else:

        raise Exception("The input is incorrect, ax must be equal to 'e' or 'o'")


def n_AGSe(lin, ax = None):
    "Lim 0.81-16. New data on the nonlinear Optical constant, Phase Matching, and Optical Damage of AgGaS2. KATO 1996 "

    l = lin*1e6

    if ax == 'e': 

        return np.sqrt(6.67920 + 0.45980/(l**2 - 0.21220)-0.00126*l**2)
 
    elif ax == 'o':

        return np.sqrt(6.85070 + 0.42970/(l**2-0.15840)-0.00125*l**2)
 
    else:

        raise Exception("The input is incorrect, ax must be equal to 'e' or 'o'")



def n_PPLN (lin, T = None):

    l = lin*1e6

    #f = (T -24.5)*(T+570.82)
    F = (T-24.5)*(T+570.82);

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

    
    return  np.sqrt(5.756 + 2.86*1e-6 * F + (0.0983+4.7*1e-8*F)/(l**2-(0.202+6.113*1e-8*F)**2) + (189.32+1.516*1e-4*F)/(l**2-12.52**2)-1.32*1e-2*l**2)

        


def ne_theta(no, ne, theta):
    
    return 1/np.sqrt(np.sin(theta)**2/ne**2 + np.cos(theta)**2/no**2)