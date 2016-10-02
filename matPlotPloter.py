"""
Ignore everything in this class for now.
"""
import matplotlib
matplotlib.use('TkAgg')

import document, matPlotPloter, basicStats

import matplotlib.pyplot as plt

class MatPlotPloter:
    def __init__(self):
        self.xmin = None
        self.xmax = None
        self.ymin = None
        self.ymax = None

    def twoDGenerator(self):
        """
        This method generate the axis based on the given min and max values
        """
        plt.xlim(self.xmin, self.xmax)
        plt.ylim(self.ymin, self.ymax)

    def twoDScatter(self, yList, xList = None):
        """
        This method generate the scatter plot given a list of y values (yList)
        and an optional list of x value (xList, or range if not given).
        """
        self.ymin = min(yList)
        self.ymax = max(yList)

        ydiff = self.ymax - self.ymin         # Calculate the range of y
        self.ymin -= ydiff/10
        self.ymax += ydiff/10

        if xList == None or type(xList[0]) == str:
            xList = list(range(1, len(yList)+1))
            self.xmin = 0
            self.xmax = len(yList) + 1

        else:
            self.xmin = min(xList)
            self.xmax = max(xList)

            xdiff = self.xmax - self.xmin         # Calculate the range of x
            self.xmin -= xdiff/10
            self.xmax += xdiff/10

        self.twoDGenerator()

        for i in range(len(yList)):
            plt.scatter(xList[i], yList[i])

        plt.show()

    def twoDBarChart(self, yList, xList = None):
        """
        This method generate the bar chart given a list of y values (yList)
        and an optional list of x value (xList, or range if not given).
        """
        self.ymin = min(yList)
        self.ymax = max(yList)

        ydiff = self.ymax - self.ymin         # Calculate the range of y
        self.ymin -= ydiff/10
        self.ymax += ydiff/10

        if xList == None or type(xList[0]) == str:
            xList = list(range(1, len(yList)+1))
            self.xmin = 0
            self.xmax = len(yList) + 1

        else:
            self.xmin = min(xList)
            self.xmax = max(xList)

            xdiff = self.xmax - self.xmin         # Calculate the range of x
            self.xmin -= xdiff/10
            self.xmax += xdiff/10

        self.twoDGenerator()

        plt.bar(xList, yList, color = 'gray', align = 'center')

        plt.show()

def main():
    doc = document.Document('GrimmFairyTales.txt')
    doc.generateWhole()
    doc.getWordCount()

    wordList = doc._Document__wordList

    stats = basicStats.BasicStats()
    top10Dict = stats.topN(stats.createFreqMap(wordList), 10)

    top10Freq = []
    top10Words = []

    print('Top 10 words and their frequencies:')

    for word in top10Dict:
        top10Words.append(word)
        top10Freq.append(top10Dict[word])
        print(word + ':' + str(top10Dict[word]), end = '  ')

    print('\n\n')

    a=matPlotPloter.MatPlotPloter()
    a.twoDScatter(top10Freq)
    a.twoDBarChart(top10Freq)
