import numpy as np
import math
from DrawBase import DrawBeam
import BeamBase


bar = BeamBase.BeamBase(25, 45, 2, 10, 1.25, 2.5, 0.5, 2)

bar.CalcBarArea()

for i in bar.BarConfiguration:
    for j in i:
        print (j.Center, j.Area)

draw = DrawBeam(bar)
draw.DrawBeam(True, True)
draw.Plot()

        
    



    
