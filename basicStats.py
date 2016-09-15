class BasicStats:
    """
    This class performs basic statistical analysis to the input list/dictionary.
    """
    def __init__(self):
        pass

    def createFreqMap(self, freqList):
        """
        This method takes in a list of words and returns a dictionary, whose
        keys are the unique words and values are the frequency of keys.
        """
        '''
        Runtime of this method is O(n^2), where n is the length of freqList.
        '''
        freqDict = {}

        for keys in freqList:
            if freqDict.get(keys) == None:
                freqDict[keys] = freqList.count(keys)

        return freqDict

    def topN(self, freqDict, n):
        """
        This method takes in a dictionary of word frequencies and returns another
        dictionary with the top n words and their frequencies.
        """
        '''
        Runtime of this method is O(m*n),
        where m is the length of freqDict, and n is n.
        '''
        topDict = {}

        for keys in freqDict:
            if len(topDict) < n:
                topDict[keys] = freqDict[keys]
            else:
                minKey = keys
                isTop = False
                for keys2 in topDict:
                    if freqDict[keys] > topDict[keys2]:
                        isTop = True
                        if freqDict[keys2] < freqDict[minKey]:
                            minKey = keys2
                if isTop:
                    topDict[keys] = freqDict[keys]
                    del topDict[minKey]
        return topDict

    def bottomN(self, freqDict, n):
        """
        This method takes in a dictionary of word frequencies and returns another
        dictionary with the bottom n words and their frequencies.
        """
        '''
        Runtime of this method is O(m*n),
        where m is the length of freqDict, and n is n.
        '''
        bottomDict = {}

        for keys in freqDict:
            if len(bottomDict) < n:
                bottomDict[keys] = freqDict[keys]
            else:
                maxKey = keys
                isBottom = False
                for keys2 in bottomDict:
                    if freqDict[keys] < bottomDict[keys2]:
                        isBottom = True
                        if freqDict[keys2] > freqDict[maxKey]:
                            maxKey = keys2
                if isBottom:
                    bottomDict[keys] = freqDict[keys]
                    del bottomDict[maxKey]
        return bottomDict

"""
Better way to do both at the same time:
    I am thinking about do both comparasons at the same time, meaning that when
    looping through the elements of the dictionary, check if it is greater than
    the smallest element of the topN dictionary or smaller than the largest element
    of the bottomN dictionary. I haven't tried this out so am still not sure if
    this will produce a smaller runtime.
"""
