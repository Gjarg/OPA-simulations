import sys

class Opa:

    def __init__(self, Opa_PM):
        self.Opa_PM = Opa_PM
        self.SYSTEM = {}

    @property
    def set_polar(self):

        while isinstance(self.Opa_PM, str) == False or len(self.Opa_PM) != 3:
            #input = raw_input()
            try:
                print('Please enter the right phase matching for OPA creation')
                sys.exit()
            except ValueError:
                pass

        for k in self.Opa_PM:
            if k != 'e':
                if k != 'o':
                    print('Please enter a right Type of phase matching')
                    sys.exit()

        self.idler_polar = self.Opa_PM[0]
        self.signal_polar = self.Opa_PM[1]
        self.pump_polar = self.Opa_PM[2]
    def add_component(self, comp, name):
        self.SYSTEM[name]=comp
