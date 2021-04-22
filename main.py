from lib_opa import *
from lib_opa.calculation import allComponents, get_indices
import matplotlib.pyplot as plt
# https://whimsical.com/XSrhVZ1abs7SHSRh2UMVdg

def main():
    print('New ------------------------------------------\n')
    # Convention idler - signal --> pump
    OPA1 = Opa('eee')
    OPA1.set_polar
    F1 = (Framework(dt=4e-15,
                    T=2e-12,
                    dr=25e-6,
                    R=1125e-6))
    Pump = (Pulse(lambda_c=1.03e-6,
                  duration=150e-15,
                  beta2=0_000e-30,
                  delay=0,
                  energy=125e-6,
                  radius=600e-6,
                  Framework=F1))
    Signal = (Pulse(lambda_c=1.750e-6,
                    duration=100e-15,
                    beta2=0e-30,
                    delay=0,
                    energy=1e-9,
                    radius=600e-6,
                    Framework=F1))

    Signal.pulse_duration()
    Pump.pulse_duration()
    Ppln=Crystal('PPLN', 0)

    print('\n------------\n')
    print(OPA1)
    print(OPA1.SYSTEM)
    OPA1.add_component(F1,"OpaFramework")
    OPA1.add_component(Pump, "PumpBeam")
    OPA1.add_component(Signal, "SignalBeam")
    OPA1.add_component(Ppln, "OpaCrystal")
    #print(OPA1.SYSTEM)
    allComponents(OPA1)
    print(OPA1.SYSTEM.keys())
    print("--" * 20 + "Test to check" + "--" * 20)
    #print(OPA1.SYSTEM['PumpBeam'].lp_mic)
    get_indices(OPA1)

    print('End ------------')

if __name__ == "__main__":
    main()