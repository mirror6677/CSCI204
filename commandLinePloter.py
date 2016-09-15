class CommandLinePloter:
    """
    This class generate 2D plan and scatter plot in the command line.
    """
    def __init__(self):
        self.numRows = 10
        self.yIncrement = 0

        self.plotString = ""

    def twoDGenerator(self, xmin, xmax, ymin, ymax):
        """
        This method generates the 2D coodinate plan in terminal given the
        max and min values of x y axis, in the following form:
         9|
         8|
         7|
         6|
         5|
         4|
         3|
         2|
         1|
         0|
          ------------------------------------------
        """
        if self.plotString == "":
            xAxis = '-' * 2 * (int((xmax - xmin)) + 1)      ## 2 dashes for each x entry

            ## calculates the scale of the y-axis
            self.yIncrement = int((ymax - ymin) / (self.numRows - 1))
            yAxis = '|' * self.numRows

            for i in range(self.numRows + 1):
                if i == self.numRows:
                    self.plotString += '{:>8}'.format(' ') + xAxis
                else:
                    self.plotString += '{:>8}'.format(int(ymax - i * self.yIncrement))
                    self.plotString += yAxis[i] + '\n'

        ### uncomment the following line to print out the 2D plane.
        ### print(self.plotString)


    def twoDScatter(self, yList, xList = None):
        """
        This method takes in one list and another optional list as inputs, using
        the twoDGenerator method above to plot the lists as x and y values in the
        command line.
        """
        ymin = min(yList)
        ymax = max(yList)

        ydiff = ymax - ymin         # Calculate the range of y
        ymin -= ydiff/10
        ymax += ydiff/10

        if xList == None or type(xList[0]) == str:
            xList = list(range(len(yList)))
            xmin = 0
            xmax = len(yList)

        else:
            xmin = min(xList)
            xmax = max(xList)

            xdiff = xmax - xmin         # Calculate the range of x
            xmin -= xdiff/10
            xmax += xdiff/10

        self.twoDGenerator(xmin, xmax, ymin, ymax)         # Store the string of plane in self.plotString

        rowList = self.plotString.split('\n')

        ## calculate where each value in xList should be on the y-axis, represented by yPos
        for i in range(len(xList)):
            yPos = int((ymax - yList[i]) / self.yIncrement)

            ## run through each row (each y value) for each element in the xList
            ## if equal to its y value, then add *, else add space, to that row.
            for j in range(len(rowList)):
                if j == yPos:
                    rowList[j] += ' *'
                else:
                    rowList[j] += '  '

        self.plotString = '\n'.join(rowList)
        print(self.plotString)
