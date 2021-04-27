from lib_opa import *
from lib_opa.new_refrac import get_material, material_info_dict
import numpy as np


def all_pulses(OPA):
    lp = OPA.SYSTEM['PumpBeam'].lambda_c
    ls = OPA.SYSTEM['SignalBeam'].lambda_c
    F1 = OPA.SYSTEM['OpaFramework']
    Idler = (Pulse(lambda_c=1 / (1 / lp - 1 / ls),
                   duration=None,
                   beta2=None,
                   delay=None,
                   energy=None,
                   radius=None,
                   Framework=F1))
    Pump_2 = (Pulse(lambda_c=lp/2,
                    duration=None,
                    beta2=None,
                    delay=None,
                    energy=None,
                    radius=None,
                    Framework=F1))
    Signal_2 = (Pulse(lambda_c=ls/2,
                      duration=None,
                      beta2=None,
                      delay=None,
                      energy=None,
                      radius=None,
                      Framework=F1))
    Idler_2 = (Pulse(lambda_c=(1 / (1 / lp - 1 / ls))/2,
                     duration=None,
                     beta2=None,
                     delay=None,
                     energy=None,
                     radius=None,
                     Framework=F1))
    return Idler, Pump_2, Signal_2, Idler_2


def allComponents(OPA):
    Idler, Pump_2, Signal_2, Idler_2 = all_pulses(OPA)
    OPA.add_component(Idler, "IdlerBeam")
    OPA.add_component(Pump_2, "PumpBeam_2")
    OPA.add_component(Signal_2, "SignalBeam_2")
    OPA.add_component(Idler_2, "IdlerBeam_2")


def generate_indices(OPA):
    crystal = get_material(OPA.SYSTEM['OpaCrystal'].name)
    #print(crycry.__bases__[0], 'to check avant')
    # dev
    if crystal.__bases__[0] == material_info_dict['BBO'].__bases__[0]:
        print('c est uniaxe')
        get_indices_uniaxe(OPA, crystal)
    elif crystal.__bases__[0] == material_info_dict['PPLN'].__bases__[0]:
        print(' c qpm')
        get_indices_qpm(OPA, crystal)

# dev


def get_indices_uniaxe(OPA, crystal):
    print('Voici les indices de refraction pour uni')
    #crystal = get_material(OPA.SYSTEM['OpaCrystal'].name)
    # n_p = crystal.nx(OPA.SYSTEM['PumpBeam'].lp)
    # print(n_p[0:15])
    # n_s = crystal.n_theta(
    #     OPA.SYSTEM['SignalBeam'].lp, OPA.SYSTEM['OpaCrystal'].angle)
    # print(n_s[0:15])
    n_i, n_s, n_p = get_indice_name_uni(crystal,OPA )
    print(n_s)#[0:15])
    print(n_p)#[0:15])
    print(n_i)#[0:15])
    # betap = crystal.beta(
    #    n=n_p, omega_center=OPA.SYSTEM['PumpBeam'].wc, omega_range=OPA.SYSTEM['OpaFramework'].w)
    # print(betap[0:15])


def get_indice_name_uni(crystal, OPA):
    n = [0,0,0]
    if OPA.Opa_PM[0] == 'e':
        # idler refractive index
        n[0] = crystal.n_theta(OPA.SYSTEM['IdlerBeam'].lp,
                               OPA.SYSTEM['OpaCrystal'].angle)
    else:
        n[0] = crystal.nx(OPA.SYSTEM['IdlerBeam'].lp)

    if OPA.Opa_PM[1] == 'e':
        # idler refractive index
        n[1] = crystal.n_theta(OPA.SYSTEM['SignalBeam'].lp,
                               OPA.SYSTEM['OpaCrystal'].angle)
    else:
        n[1] = crystal.nx(OPA.SYSTEM['SignalBeam'].lp)

    if OPA.Opa_PM[2] == 'e':
        # idler refractive index
        n[2] = crystal.n_theta(OPA.SYSTEM['PumpBeam'].lp,
                               OPA.SYSTEM['OpaCrystal'].angle)
    else:
        n[2] = crystal.nx(OPA.SYSTEM['PumpBeam'].lp)
    return n


def get_indices_qpm(OPA, crystal):
    print('Voici les indices de refraction pour qpm')
    #crystal = get_material(OPA.SYSTEM['OpaCrystal'].name)
    n_p = crystal.n(OPA.SYSTEM['PumpBeam'].lp, T=140)
    betap = crystal.beta(
        n=n_p, omega_center=OPA.SYSTEM['PumpBeam'].wc, omega_range=OPA.SYSTEM['OpaFramework'].w)
    print(betap[0:15])


def get_group_velocity(OPA):
    crystal = get_material(OPA.SYSTEM['OpaCrystal'].name)
