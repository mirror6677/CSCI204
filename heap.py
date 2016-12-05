def topNHeap(wordList, n):
    """
    This method takes in a list of words and returns a list with the top n words
    and a list of their frequencies (divided by the total number of words).
    """
    '''
    The construction of the complete tree is O(n^2).
    The process of taking out the top N is O(n).
    '''
    # Construct a list of unique words and their frequencies.
    total = len(wordList)
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
        topNFreq.append(frequencies[1]/total)

        words[1] = words.pop()
        frequencies[1] = frequencies.pop()

    return topNWords, topNFreq

def bottomNHeap(wordList, n):
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
