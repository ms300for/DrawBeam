import numpy as np
import math
import DrawBase
import BeamBase


bar = BeamBase.BeamBase(15, 45, 2, 20, 1.25, 2.5, 0.5, 2)
for i in bar.BarConfiguration:
    print(i.Center, i.Radius)
        
    



    
