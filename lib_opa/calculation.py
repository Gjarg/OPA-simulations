from lib_opa import *
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