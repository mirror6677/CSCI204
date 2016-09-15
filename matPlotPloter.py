"""
Ignore everything in this class for now.
"""

import matplotlib.pyplot as plt

class MatPlotPloter:
    def __init__(self):
        pass

    def twoDGenerator(self, xmin, xmax, ymin, ymax):
        """
        This method generate the axis based on the given min and max values
        """
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)

    def twoDScatter(self, yList, xList = None):
        """
        This method generate the scatter plot given a list of y values (yList)
        and an optional list of x value (xList, or range if not given).
        """
        ymin = min(yList)
        ymax = max(yList)

        ydiff = ymax - ymin         # Calculate the range of y
        ymin -= ydiff/10
        ymax += ydiff/10

        if xList == None:
            xList = list(range(len(yList)))
            xmin = 0
            xmax = len(yList)

        else:
            xmin = min(xList)
            xmax = max(xList)

            xdiff = xmax - xmin         # Calculate the range of x
            xmin -= xdiff/10
            xmax += xdiff/10

        self.twoDGenerator(xmin, xmax, ymin, ymax)

        for i in range(len(yList)):
            plt.scatter(xList[i], yList[i])

        plt.show()
