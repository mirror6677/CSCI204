import document, matPlotPloter, basicStats, heap, decisionTree, textFilter, SKPCA, SKTree
import tkinter
import matplotlib.pyplot as plt

class UserGUI:
    def __init__(self, master):
        self.master = master
        master.title("UserGUI")

        self.introGUI()

    def introGUI(self):
        self.label = tkinter.Label(self.master, text="Number of documents to be analyzed:")
        self.label2 = tkinter.Label(self.master, text="Characteristic categories (if ID3 or SKTree was chosen):")

        self.entry = tkinter.Entry(self.master)
        self.entry2 = tkinter.Entry(self.master)

        self.radioLabel = tkinter.Label(self.master, text="Choose a training method:")

        self.methodVar = tkinter.IntVar()
        self.radio1 = tkinter.Radiobutton(self.master, text='ID3', variable=self.methodVar, value=1)
        self.radio2 = tkinter.Radiobutton(self.master, text='SKTree', variable=self.methodVar, value=2)
        self.radio3 = tkinter.Radiobutton(self.master, text='SKPCA', variable=self.methodVar, value=3)

        self.filterLabel = tkinter.Label(self.master, text="Text filters (if TKPCA was chosen): ")

        self.filterVar = [None] * 5
        self.filter1 = tkinter.Checkbutton(self.master, text='Normalize whitespace', variable=self.filterVar[0], onvalue=1, offvalue=0)
        self.filter2 = tkinter.Checkbutton(self.master, text='Normalize case', variable=self.filterVar[1], onvalue=2, offvalue=0)
        self.filter3 = tkinter.Checkbutton(self.master, text='Strip null characters', variable=self.filterVar[2], onvalue=3, offvalue=0)
        self.filter4 = tkinter.Checkbutton(self.master, text='Strip numbers', variable=self.filterVar[3], onvalue=4, offvalue=0)
        self.filter5 = tkinter.Checkbutton(self.master, text='Strip common words', variable=self.filterVar[4], onvalue=5, offvalue=0)

        self.label.grid(row=0, column=0, sticky=tkinter.W)
        self.label2.grid(row=6, column=0, sticky=tkinter.W)
        self.radioLabel.grid(row=2, column=0, sticky=tkinter.W)
        self.filterLabel.grid(row=8, column=0, sticky=tkinter.W)

        self.entry.grid(row=1, column=0, sticky=tkinter.W)
        self.entry2.grid(row=7, column=0, sticky=tkinter.W)

        self.radio1.grid(row=3, column=0, sticky=tkinter.W)
        self.radio2.grid(row=4, column=0, sticky=tkinter.W)
        self.radio3.grid(row=5, column=0, sticky=tkinter.W)

        self.filter1.grid(row=9, column=0, sticky=tkinter.W)
        self.filter2.grid(row=10, column=0, sticky=tkinter.W)
        self.filter3.grid(row=11, column=0, sticky=tkinter.W)
        self.filter4.grid(row=12, column=0, sticky=tkinter.W)
        self.filter5.grid(row=13, column=0, sticky=tkinter.W)

        self.button = tkinter.Button(self.master, text="Confirm", command=lambda: self.mainGUI())

        self.button.grid(row=14, column=0)

    def mainGUI(self):
        self.num = int(self.entry.get())

        self.oneDlist = ['author'] + self.entry2.get().split(',')        # characteristics list

        self.filterVar = [i for i in self.filterVar if i != 0]      # text filters list

        self.nameLabel = tkinter.Label(self.master, text="Document Names:")
        self.charLabel = tkinter.Label(self.master, text="Characteristics:")
        self.charLabel2 = tkinter.Label(self.master, text='(author[if for training], '+self.entry2.get()+')')
        #self.filterLabel = tkinter.Label(self.master, text="Text Filters:")
        #self.statLabel = tkinter.Label(self.master, text="Statistical Method:")
        self.trainLabel = tkinter.Label(self.master, text="  For training?  ")
        self.predictLabel = tkinter.Label(self.master, text="  For predicting?  ")
        self.resultLabel = tkinter.Label(self.master, text="  RESULTS:    ")

        self.nameEntry = []
        self.charEntry = []
        #self.filterEntry = []
        #self.statEntry = []
        self.trainBox = []
        self.predictBox = []
        self.tVar = []
        self.pVar = []

        for i in range(self.num):
            var1 = tkinter.IntVar()
            var2 = tkinter.IntVar()
            self.tVar.append(var1)
            self.pVar.append(var2)

            self.nameEntry.append(tkinter.Entry(self.master))
            self.charEntry.append(tkinter.Entry(self.master))
            #self.filterEntry.append(tkinter.Entry(self.master))
            #self.statEntry.append(tkinter.Entry(self.master))

            self.trainBox.append(tkinter.Checkbutton(self.master, variable=self.tVar[i]))
            self.predictBox.append(tkinter.Checkbutton(self.master, variable=self.pVar[i]))

            self.nameEntry[i].grid(row=i+2, column=0)
            self.charEntry[i].grid(row=i+2, column=1)
            #self.filterEntry[i].grid(row=i+2, column=2)
            #self.statEntry[i].grid(row=i+2, column=3)

            self.trainBox[i].grid(row=i+2, column=2)
            self.predictBox[i].grid(row=i+2, column=3)

        self.run_button = tkinter.Button(self.master, text="Run", command=lambda: self.update())

        # LAYOUT

        self.nameLabel.grid(row=0, column=0, sticky=tkinter.W)
        self.charLabel.grid(row=0, column=1, sticky=tkinter.W)
        self.charLabel2.grid(row=1, column=1, sticky=tkinter.W)
        #self.filterLabel.grid(row=0, column=2, sticky=tkinter.W)
        #self.statLabel.grid(row=0, column=3, sticky=tkinter.W)
        self.trainLabel.grid(row=0, column=2)
        self.predictLabel.grid(row=0, column=3)
        self.resultLabel.grid(row=0, column=4, sticky=tkinter.W)

        self.run_button.grid(row=self.num+2, column=0,columnspan=4)

        self.label.destroy()
        self.label2.destroy()
        self.entry.destroy()
        self.entry2.destroy()
        self.button.destroy()
        self.radioLabel.destroy()
        self.radio1.destroy()
        self.radio2.destroy()
        self.radio3.destroy()
        self.filterLabel.destroy()
        self.filter1.destroy()
        self.filter2.destroy()
        self.filter3.destroy()
        self.filter4.destroy()
        self.filter5.destroy()

    def update(self):
        try:
            for l in self.resultL:
                l.destroy()
        except:
            pass

        print(self.methodVar.get())
        self.filenamesT = []
        self.filenamesP = []

        if self.methodVar.get() != 3:
            self.twoDlistT = []
            self.twoDlistP = []
        else:
            authorListT = []

        for i in range(len(self.nameEntry)):
            if self.tVar[i].get():
                self.filenamesT.append(self.nameEntry[i].get())

                if self.methodVar.get() != 3:
                    self.twoDlistT.append(self.charEntry[i].get().split(','))
                else:
                    authorListT.append(self.charEntry[i].get())

            elif self.pVar[i].get():
                self.filenamesP.append(self.nameEntry[i].get())

                if self.methodVar.get() != 3:
                    self.twoDlistP.append([None] + self.charEntry[i].get().split(','))

        if self.methodVar.get() == 1:
            authorListP = id3(self.oneDlist, self.twoDlistT, self.twoDlistP)
        elif self.methodVar.get() == 2:
            authorListP = skTree(self.oneDlist, self.twoDlistT, self.twoDlistP)
        elif self.methodVar.get() == 3:
            authorListP = skPCA(self.filenamesT, self.filenamesP, self.filterVar, authorListT)

        self.result(authorListP)

        '''
        for filename in filenamesT + filenamesP:
            doc = document.Document(filename)
            doc.generateWhole()
            doc.getWordCount()

            wordList = doc._Document__wordList

            topWords, topFreq = heap.topNHeap(wordList, 10)

            print('Top 10 words and their frequencies:')

            for i in range(len(topWords)):
                print(topWords[i] + ':' + str(topFreq[i]), end = '  ')

            print('\n\n')

            graph = matPlotPloter.MatPlotPloter()
            graph.twoDBarChart(topFreq, topWords)

        matGraph = matPlotPloter.MatPlotPloter()
        matGraph.twoDScatter(top10Freq)
        matGraph.twoDBarChart(top10Freq)
        '''

    def result(self, authorListP):
        self.authorLabel = []
        c = 0
        for i in range(len(self.pVar)):
            if not self.tVar[i].get() and self.pVar[i].get():
                self.authorLabel.append(authorListP[c])
                c += 1
            else:
                self.authorLabel.append('')

        self.resultL = []
        for i in range(len(self.authorLabel)):
            self.resultL.append(tkinter.Label(self.master, text=self.authorLabel[i]))
            self.resultL[i].grid(row=i+2, column=4, sticky=tkinter.W)

def id3(attrList,twoDListT,twoDListP,depth = 5):
    aTree = decisionTree.DecisionTree(twoDListT,attrList,depth)
    authorList = []
    data = aTree.eval(twoDListP)
    for row in data:
        authorList.append(row[0])
    return authorList

def skTree(attrList,twoDListT,twoDListP,depth = 5):
    aTree = SKTree.SKTree()

    processDict = {}
    trainList, processDict = preprocess(twoDListT, processDict)

    aTree.train(trainList, attrList, depth)
    authorList = []

    predictList, processDict = preprocess(twoDListP, processDict)

    data = aTree.eval(predictList)
    print(data)
    for row in data:
        for i in processDict:
            if processDict[i] == row[0]:
                authorList.append(i)

    return authorList

def preprocess(inList, inDict):
    outList = []
    for i in range(len(inList)):
        outList.append([])

    for i in range(len(inList)):
        for element in inList[i]:
            if element not in inDict:
                inDict[element] = len(inDict)

            outList[i].append(inDict[element])

    return outList, inDict


def skPCA(filenamesT, filenamesP, filterList, authorList):
    """ This function takes in a list of file names for training, a list of
        filenames for predicting, and a list of text filters to be applied.
    """
    # train
    word2D = []
    freq2D = []
    for filename in filenamesT:
        doc = document.Document(filename)
        doc.generateWhole()

        tf = textFilter.TextFilter(doc, filterList)
        tf.apply()

        doc.getWordCount()
        wl = doc._Document__wordList

        words, frequencies = heap.topNHeap(wl, 50)
        word2D.append(words)
        freq2D.append(frequencies)

    trainData = []
    for author in authorList:
        trainData.append([author])

    wordList = []
    for i in range(50):
        currentWord = word2D[0][i]
        freqList = [freq2D[0][i]]

        found2 = True
        for j in range(1, len(word2D)):
            found = False

            for k in range(50):
                if currentWord == word2D[j][k]:
                    found = True
                    freqList.append(freq2D[j][k])
                    break

            if not found:
                found2 = False

        if found2:
            for m in range(len(freqList)):
                trainData[m].append(freqList[m])

            wordList.append(currentWord)

    pca = SKPCA.SKPCA()
    pca.train(trainData, wordList)

    # predict
    predictData = []
    for filename in filenamesP:
        predictData.append([None])
        doc = document.Document(filename)
        doc.generateWhole()

        tf = textFilter.TextFilter(doc, filterList)
        tf.apply()

        doc.getWordCount()
        wl = doc._Document__wordList
        total = len(wl)

        for w in wordList:
            count = 0
            for ww in wl:
                if w == ww:
                    count += 1

            predictData[-1].append(count/total)

    returnData = pca.eval(predictData)

    plt.plot(pca.X[0], pca.X[1], 'bs', pca.anaTable[0], pca.anaTable[1], 'g^')
    plt.show()

    return returnData




root = tkinter.Tk()
my_gui = UserGUI(root)
root.mainloop()
