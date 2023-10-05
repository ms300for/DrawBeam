import matplotlib.pyplot as plt
import numpy as np



class SteelBarLine():
    def __init__(self, x, y, radios):
        self.Center = (x, y)
        self.Radios = radios

class BeamBase():

    AgressiveCovering = [2, 3, 3, 3.5] #cm
    
    def __init__(self, width, height, agressClass, quantBar, dBar, dAgreg, dEstribo, av):
        self.Width = width  #cm
        self.Height = height #cm
        
        self.AgressClass = agressClass #adm
        self.Covering = self.CalcCovering() #cm
        
        self.QuantBar = quantBar # adm
        self.DBar = dBar #cm
        self.DAgreg = dAgreg #cm
        self.DEstribo = dEstribo #cm
        self.Av = av #cm

        self.BarConfiguration = self.CalcBarConfiguration(0, self.Av)


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

    def CalcBarConfiguration(self, idealNumber = 0, xInit = 0, yInit = 0):
        
        maxNumber = self.CalcMaxBarPerLine()
        numberPerLine = idealNumber if idealNumber <= maxNumber and idealNumber != 0 else maxNumber
        numberPerLine = numberPerLine if numberPerLine <= self.QuantBar else self.QuantBar

        barList = []
        yInitial = self.Covering + self.DEstribo + self.DBar/2 if yInit == 0 else yInit
        xInitial = self.Covering + self.DEstribo + self.DBar/2 if xInit == 0 else xInit
        
        for i in range(0, (self.QuantBar//numberPerLine + 1)):
            if i == 0:
               [barList.append(i) for i in self.DistrLineBar(numberPerLine, xInit, yInitial,'uniforme')]

        for i in barList:
            print (i.Center)
                
        
    def DistrLineBar(self, quantBar, xPos, yPos, distType = 'uniforme'):
        # uniforme - barras distribuídas a mesma distância
        # bordas - concentra as barras na borda
        steelBars = []
        xInit = xPos
        if (distType == 'uniforme' or not (quantBar % 2 == 0)):
            dist = self.CalcDistBar(quantBar)
            for i in range(quantBar):
                steelBars.append(SteelBarLine(xInit, yPos, self.DBar))
                xInit += dist + self.DBar

        else:
            dist = self.CalcMinDistBar()
            for i in range(0, quantBar/2):
                steelBars.append(steelBarline(xInit, yPos, self.DBar))
                xInit += dist + self.Dbar
            xInit = self.Width - xPos
            for i in range(0, quantBar/2):
                steelBars.append(steelBarline(xInit, yPos, self.DBar))
                xnit -= dist + self.Dbar

        return steelBars
#self, width, height, agressClass, quantBar, dBar, dAgreg, dEstribo, av):
bar = BeamBase(20, 45, 2, 3, 1.25, 0.5, 0.05, 2)
bar = BeamBase(20, 45, 2, 4, 1.25, 0.5, 0.05, 2)
        
    



    
