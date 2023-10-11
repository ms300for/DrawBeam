import matplotlib.pyplot as plt
import numpy as np
from BeamBase import BeamBase

class Draw():
    def __init__(self, xDim, yDim):
        self.xDim = xDim
        self.yDim = yDim
        self.Figure = plt.figure(figsize = (xDim/yDim*8, 8))

    def DrawRectangule(self, xMin, yMin, xMax, yMax, colorLine = 'black'):
        plt.plot([xMin, xMin], [yMin, yMax], color = colorLine)
        plt.plot([xMin, xMax], [yMin, yMin], color = colorLine)
        plt.plot([xMin, xMax], [yMax, yMax], color = colorLine)
        plt.plot([xMax, xMax], [yMin, yMax], color = colorLine)

    def DrawCircle(self, center, radius, color='black'):
        circle = plt.Circle(center, radius, color=color, fill=False)
        plt.gca().add_patch(circle)

    def Plot(self):
        plt.xlim(-2, self.xDim + 2)
        plt.ylim(-2, self.yDim + 2)
        plt.show()

    def SaveFig(self):
        plt.saveImg(self.Figure)


class DrawBeam(Draw):
    def __init__(self, beamBase):
        self.Beam = beamBase
        super().__init__(beamBase.Width, beamBase.Height)

    def DrawBeam(self, drawArmor, writeDim):
        self.DrawRectangule(0, 0, self.Beam.Width, self.Beam.Height)
        if (drawArmor):
            self.DrawArmor(writeDim)

    def DrawArmor(self, writeDim):
        self.DrawRectangule(0 + self.Beam.Covering, 0 + self.Beam.Covering, self.Beam.Width - self.Beam.Covering, self.Beam.Height - self.Beam.Covering, "red")
        self.DrawRectangule(0 + self.Beam.Covering + self.Beam.DEstribo,
                            0 + self.Beam.Covering + self.Beam.DEstribo,
                            self.Beam.Width - self.Beam.Covering - self.Beam.DEstribo,
                            self.Beam.Height - self.Beam.Covering - self.Beam.DEstribo, "red")

        for i in self.Beam.BarConfiguration:
            self.DrawCircle(i.Center, i.Radius)
        
    



    
