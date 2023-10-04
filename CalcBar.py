import numpy as np
import math

# YNL - Linha Neutra
# DBar - Diâmetro da Barra #cm
# DxMin - Distância mínima entre barras ah #cm
# QuantBar - Quantidade de barras
# 

def CalcDistBar(DimX, C, DE, DBar, QuantBar):
    return (DimX - (2*C + 2*DE + QuantBar*DBar))/(QuantBar - 1)

def CalcMinDist(DBar, DAgreg):
    return max([2, DBar, 1.2*DAgreg])

def CalcMaxBarPerLine(DimX, C, DE, DBar, DAgreg = 2.5, QuantInit = 2):
    QuantMax = QuantInit
    minDist = CalcMinDist(DBar, DAgreg)
    dist = CalcDistBar(DimX, C, DE, DBar, QuantMax)
    print("minDist: ", minDist)
    print("Dist:", dist)
    while (dist >= minDist):
        QuantMax += 1
        dist = CalcDistBar(DimX, C, DE, DBar, QuantMax)
        print(dist)
    print(QuantMax - 1)
        


CalcMaxBarPerLine(20, 3, 0.5, 1.25)
#CalcDistBar(20, 3, 0.5, 1.25, 1)
    
        
    



    
