import matplotlib.pyplot as plt
import numpy as np

class Draw():
    def __init__(self, xDim, yDim):
        self.xDim = xDim
        self.yDim = yDim
        self.Figure = plt.figure(figsize = (xDim/yDim*8, 8))

    def DrawRectangule(self, xMin, yMin, xMax, yMax, thickness, colorLine = 'black'):
        plt.plot([xMin, xMin], [yMin, yMax], color = colorLine)
        plt.plot([xMin, xMax], [yMin, yMin], color = colorLine)
        plt.plot([xMin, xMax], [yMax, yMax], color = colorLine)
        plt.plot([xMax, xMax], [yMin, yMax], color = colorLine)

    def Plot(self):
        plt.xlim(-2, self.xDim + 2)
        plt.ylim(-2, self.yDim + 2)
        plt.show()

    def SaveFig(self):
        plt.saveImg(self.Figure)


a = Draw(25, 35)
a.DrawRectangule(1, 1, 15, 15, 3)
a.Plot()
    
        
    



    
