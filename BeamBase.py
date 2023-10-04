import matplotlib.pyplot as plt
import numpy as np

class BeamBase():

    AgressiveCovering = [2, 2.5, 3, 3.5] #cm
    
    def __init__(self, width, height, agressClass, quantBar, dBar, dAgreg, dEstribo):
        self.Width = width  #cm
        self.Height = height #cm
        
        self.AgressClass = agressClass #adm
        self.Covering = self.CalcCovering() #cm
        
        self.QuantBar = quantBar # adm
        self.DBar = dBar #cm
        self.DAgreg = dAgreg #cm
        self.DEstribo = dEstribo #cm


    def CalcCovering(self):
        if (self.AgressClass > 3):
            return self.AgressiveCovering[3]
        return self.AgressiveCovering[self.AgressClass]
    
    def CalcMinDistBar(self):
        return max([2, self.DBar, 1.2 * self.DAgreg])

    def CalcDistBar(self, QuantBar):
        return (self.Width - (2*self.Covering + 2*self.DEstribo + QuantBar*self.DBar))/(QuantBar - 1)

    def CalcMaxBarPerLine(self, QuantInit = 2):
        QuantMax = QuantInit
        minDist = self.CalcMinDistBar()
        dist = self.CalcDistBar(QuantMax)
        while (dist >= minDist or QuantMax < self.QuantBar):
            QuantMax += 1
            dist = self.CalcDistBar(QuantMax)
            
        return (QuantMax - 1)

bar = BeamBase(20, 40, 2, 5, 1.25, 1.25, 0.65)
print(bar.CalcCovering())
print(bar.CalcMinDistBar())
print(bar.CalcDistBar(3))
print(bar.CalcMaxBarPerLine())
        
    



    
