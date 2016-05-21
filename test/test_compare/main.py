from reax_prim import *

print("ook")

pot_a = Potential('../resources/ffield_a')
pot_b = Potential('../resources/ffield_b')

params = Param('../resources/params')

comp = Compare(pot_a, pot_b, params)

comp.compare()
