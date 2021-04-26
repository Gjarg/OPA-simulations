from lib_opa import *
from lib_opa.new_refrac import get_material, material_info_dict
import numpy as np
def all_pulses(OPA):
    lp = OPA.SYSTEM['PumpBeam'].lambda_c
    ls = OPA.SYSTEM['SignalBeam'].lambda_c
    F1 =OPA.SYSTEM['OpaFramework']
    Idler = (Pulse(lambda_c=1 / (1 / lp - 1 / ls),
                    duration=None,
                    beta2=None,
                    delay=None,
                    energy=None,
                    radius=None,
                    Framework=F1))
    Pump_2 = (Pulse(lambda_c= lp/2,
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
    crycry = get_material(OPA.SYSTEM['OpaCrystal'].name)
    print(crycry.__bases__[0], 'to check avant')
    print(crycry.__name__)
    #print(material_info_dict['BBO'].__bases__[0])
    if crycry.__bases__[0] == material_info_dict['BBO'].__bases__[0]:
        print('c est uniaxe')
    elif crycry.__bases__[0] == material_info_dict['PPLN'].__bases__[0]:
        print(' c qpm')

def get_indices(OPA):
    print('Voici les indices de refraction')
    crystal = get_material(OPA.SYSTEM['OpaCrystal'].name)
    n_p = crystal.n(OPA.SYSTEM['PumpBeam'].lp, T=140)
    betap = crystal.beta(n=n_p, omega_center=OPA.SYSTEM['PumpBeam'].wc, omega_range=OPA.SYSTEM['OpaFramework'].w);
    print(betap)

def get_group_velocity(OPA):
    crystal = get_material(OPA.SYSTEM['OpaCrystal'].name)
    #n_e = crystal.
