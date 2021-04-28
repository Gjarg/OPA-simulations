from lib_opa import *
from lib_opa.calculation import allComponents#, get_indices
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
    Pump = (Pulse(lambda_c=0.515e-6,
                  duration=150e-15,
                  beta2=0_000e-30,
                  delay=0,
                  energy=125e-6,
                  radius=600e-6,
                  Framework=F1))
    Signal = (Pulse(lambda_c=1.03e-6,
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


    print("--" * 20 + "Test to check" + "--" * 20)
    #get_indices(OPA1)
    OPA1 = Opa('eee')
    OPA1.set_polar
    OPA1.add_component(F1,"OpaFramework")
    OPA1.add_component(Pump, "PumpBeam")
    OPA1.add_component(Signal, "SignalBeam")
    OPA1.add_component(Ppln, "OpaCrystal")
    allComponents(OPA1)
    #get_indices(OPA1)
    print('End ------------')
    print("--" * 20 + "Check BBO" + "--" * 20)

    # allComponents(OPA2)
    ### juste pour le dev##
    from lib_opa.new_refrac import get_material
    from lib_opa.calculation import generate_indices
    # bbo_crystal = get_material(OPA2.SYSTEM['OpaCrystal'].name)
    # BBO_no = bbo_crystal.nx(OPA2.SYSTEM['PumpBeam'].lp, T=None)
    # BBO_ne_theta = bbo_crystal.n_theta(
    #     OPA2.SYSTEM['PumpBeam'].lp, theta=OPA2.SYSTEM['OpaCrystal'].angle, T=None)
    # print(BBO_no[0:15], '\n', BBO_ne_theta[0:15])
    # print(OPA2.SYSTEM['OpaCrystal'].angle)

    OPA2 = Opa('ooe')
    OPA2.set_polar
    BBO = Crystal('BBO', 23.4)
    OPA2.add_component(BBO, "OpaCrystal")
    OPA2.add_component(F1, "OpaFramework")
    OPA2.add_component(Pump, "PumpBeam")
    OPA2.add_component(Signal, "SignalBeam")
    allComponents(OPA2)
    #print(OPA2.SYSTEM == OPA1.SYSTEM)
    #print(OPA2)
    #print(OPA2.SYSTEM['IdlerBeam'].lp)
    #generate_indices(OPA2)
    #generate_indices(OPA1)
    OPA3 = Opa('ooe')
    OPA3.set_polar
    NL = Crystal('NL', 45)
    OPA3.add_component(NL, "OpaCrystal")
    OPA3.add_component(F1, "OpaFramework")
    OPA3.add_component(Pump, "PumpBeam")
    OPA3.add_component(Signal, "SignalBeam")
    generate_indices(OPA2)

if __name__ == "__main__":
    main()
