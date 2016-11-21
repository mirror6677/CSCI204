import document, documentStream, sentence, commandLinePloter, basicStats
import time

def main():
    filename = input('Please enter file name: ')

    doc = document.Document(filename)
    doc.generateWhole()
    doc.getWordCount()

    wordList = doc._Document__wordList

    stats = basicStats.BasicStats()
    tic = time.time()
    top10Dict = stats.topN(stats.createFreqMap(wordList), 50)
    toc = time.time()
    print('Traditional time:', toc-tic)

    tic = time.time()
    topWords, topFreq = stats.topNHeap(wordList, 50)
    toc = time.time()
    print('Heap sort time:', toc-tic)


    top10Freq = []
    top10Words = []

    print('Top 10 words and their frequencies:')

    for word in top10Dict:
        top10Words.append(word)
        top10Freq.append(top10Dict[word])
        print(word + ':' + str(top10Dict[word]), end = '  ')

    print('\n\n')

    for i in range(len(topWords)):
        print(topWords[i] + ': ' + str(topFreq[i]), end = '  ')

    '''
    graph = commandLinePloter.CommandLinePloter()
    graph.twoDBar(top10Freq)

    docS = documentStream.DocumentStream(filename)
    docS.writeWhole(doc)
    '''

if __name__ == "__main__":
    main()
