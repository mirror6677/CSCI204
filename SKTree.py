"""This file contains the starting block for decisiontree in scikit
    You Will need to add functions/methods to convert data into needed format,
    See treedemo.py
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz


class SKTree:

    def __init__(self):
        self.tree = None
        self.labels = None
        self.depth = None

    def train(self, data, labels, depth):
        """We assume that data is a 2D python list, the target in colum 0"""
        self.labels = labels
        self.depth = depth

        x = [None]*len(data)
        y = [None]*len(data)

        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t


        self.tree = DecisionTreeClassifier(criterion="entropy", max_depth=depth, random_state=0)
        self.tree = self.tree.fit(x,y)

    def eval(self, data):
        """We assume that data is a 2D python list, with the target [0] == None"""

        x = [None]*len(data)
        for row in range(len(data)):
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t

        y = self.tree.predict(x)
        print(y)
        #Now you will have to get the values from y and move them to the targe column of data
        for row in range(len(x)):
            x[row][0] = y[row]
        return x

    def toDot(self, filename):
        dot_data = export_graphviz(self.tree, out_file=filename, feature_names=self.labels)
