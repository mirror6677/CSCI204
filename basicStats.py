import sllink, sStack
import random

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

    def slinkFreq(self, freqList):
        """
        This method takes in a list of words and returns the head of a linked list,
        whose first data is a word and second data is the frequency of the word.
        """
        '''
        Runtime of this method is O(n^2), where n is the length of the freqList
        '''
        freqSlink = sllink.SLink()

        for word in freqList:
            runner = freqSlink.head

            while runner != None:
                if runner.data[0] == word:
                    runner.data[1] += 1
                    break

                runner = runner.next

            if runner == None:
                freqSlink.add([word, 1])

        return freqSlink.head

    def topNSlink(self, head, n):
        """
        This method takes in the head of a Sllink of word frequencies and returns
        a SStack with the top n words and their frequencies.
        """
        '''
        Runtime of this method is O(m*n),
        where m is the length of freqSlink, and n is n.
        '''
        count = 0
        runner = head
        freqStack = sStack.SStack()

        while runner != None:

            if count < n:
                freqStack.push(runner)

            else:
                minNode = freqStack.head
                runner2 = freqStack.head

                while runner2 != None:
                    if runner2.data[1] < minNode.data[1]:
                        minNode = runner2

                    runner2 = runner2.next

                if minNode.data[1] < runner.data[1]:
                    minNode.data = runner.data

            count += 1
            runner = runner.next

        return freqStack.head

    def topNHeap(self, wordList, n):
        """
        This method takes in a list of words and returns a list with the top n words
        and a list of their frequencies.
        """
        '''
        The construction of the complete tree is O(n^2).
        The process of taking out the top N is O(n).
        '''
        # Construct a list of unique words and their frequencies.
        words = [None]
        frequencies = [0]
        for word in wordList:
            try:
                i = words.index(word)
                frequencies[i] += 1
            except:
                words.append(word)
                frequencies.append(1)

        # Fix up the maximum frequency, add to the topN list, and remove from the heap.
        topNWords = []
        topNFreq = []
        for num in range(n):
            for i in range(len(words)-1, 1, -1):
                if frequencies[i] > frequencies[i//2]:
                    value = words[i]
                    words[i] = words[i//2]
                    words[i//2] = value
                    value = frequencies[i]
                    frequencies[i] = frequencies[i//2]
                    frequencies[i//2] = value

            topNWords.append(words[1])
            topNFreq.append(frequencies[1])

            words[1] = words.pop()
            frequencies[1] = frequencies.pop()

        return topNWords, topNFreq

    def bottomNHeap(self, wordList, n):
        """
        This method takes in a list of words and returns a list with the bottom n words
        and a list of their frequencies.
        """
        '''
        The construction of the complete tree is O(n^2).
        The process of taking out the bottom N is O(n).
        '''
        # Construct a list of unique words and their frequencies.
        words = [None]
        frequencies = [0]
        for word in wordList:
            try:
                i = words.index(word)
                frequencies[i] += 1
            except:
                words.append(word)
                frequencies.append(1)

        # Fix up the minimum frequency, add to the bottomN list, and remove from the heap.
        bottomNWords = []
        bottomNFreq = []
        for num in range(n):
            for i in range(len(words)-1, 1, -1):
                if frequencies[i] < frequencies[i//2]:
                    value = words[i]
                    words[i] = words[i//2]
                    words[i//2] = value
                    value = frequencies[i]
                    frequencies[i] = frequencies[i//2]
                    frequencies[i//2] = value

            bottomNWords.append(words[1])
            bottomNFreq.append(frequencies[1])

            words[1] = words.pop()
            frequencies[1] = frequencies.pop()

        return bottomNWords, bottomNFreq


def main():
    words = ['a', 'b', 'c', 'd', 'e']
    wList = []
    for i in range(20):
        wList.append(random.choice(words))

    print(wList)
    s = BasicStats()
    print(s.bottomNHeap(wList, 3))

#main()
