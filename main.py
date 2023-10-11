import numpy as np
import math
from DrawBase import DrawBeam
import BeamBase


bar = BeamBase.BeamBase(20, 45, 2, 5, 1.25, 2.5, 0.5, 2)
for i in bar.BarConfiguration:
    print(i.Center, i.Radius)
#draw = DrawBeam(bar)
#draw.DrawBeam(True, True)
#draw.Plot()

        
    



    
