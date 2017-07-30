import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

import subfolder.subsub.equation_area as equa

x, y= 10, 10
x2=20

rect = equa.calc_rect(x,y)
tri = equa.calc_tri(x,y)
circ = equa.calc_circle(x)
trap = equa.calc_trap(x,x2,y)

a = equa.TABLE % (x,x2,y,rect,tri,circ,trap)
print(a)
