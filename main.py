import document, documentStream, sentence, commandLinePloter, basicStats

def main():
    filename = input('Please enter file name: ')

    doc = document.Document(filename)
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
    graph = commandLinePloter.CommandLinePloter()
    graph.twoDBar(top10Freq)

    docS = documentStream.DocumentStream(filename)
    docS.writeWhole(doc)


if __name__ == "__main__":
    main()
