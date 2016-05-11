from reax_prim import Potential
from reax_prim import Param

#Potential("ffield.reax.cho")
#Potential("ffield").write("ffield.out")

param = Param()
param.read('params')
param.write_random_order('out.txt', 200)

param.set_random
