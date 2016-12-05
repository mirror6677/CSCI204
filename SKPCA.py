"""This file contains the starting block for PCA in scikit
    You will need to add functions/methods to convert data into needed format,
    See treedemo.py
"""

import pandas as pd
import numpy as np
import math
from sklearn import decomposition

class SKPCA:

    def __init__(self):
        self.pca_h = None
        self.ncomp = 0
        self.labels = None
        self.X = None
        self.author = None

    def train(self, data, labels, ncomp = 2):
        """Data is a 2d data list.
           Each row in the 2dlist is sample (all samples probably of a word)
           The first column is the label idenity the sample ("A")
           labels are where the sample came frome, such as from JamesJoyce sisters
        """
        self.ncomp = ncomp
        self.labels = labels

        #Strip the first column
        x = [None]*len(data)
        y = [None]*len(data)

        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t
        self.author = y

        self.pca_h = decomposition.PCA(ncomp)
        self.pca_h.fit(x)
        self.X = self.pca_h.transform(x)

    def eval(self, data):
        x = [None] * len(data)
        author = []

        for row in range(len(data)):
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t

        pca_eval = decomposition.PCA(2)
        pca_eval.fit(x)
        self.anaTable = pca_eval.transform(x)

        for row in range(len(self.anaTable)):
            disList = []
            x1 = self.anaTable[row][0]
            y1 = self.anaTable[row][1]
            for subrow in range(len(self.X)):
                x2 = self.X[subrow][0]
                y2 = self.X[subrow][1]
                disList.append(self.dis(x1,x2,y1,y2))
            author.append(self.author[disList.index(min(disList))])
        return author

    @staticmethod
    def dis(x1,x2,y1,y2):
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
