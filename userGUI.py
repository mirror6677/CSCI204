#from tkinter import Tk, Label, Button, Entry, END, W, E
import document, matPlotPloter, basicStats, commandLinePloter
import tkinter


class UserGUI:
    def __init__(self, master):
        self.master = master
        master.title("UserGUI")

        self.introGUI()

    def introGUI(self):
        self.label = tkinter.Label(self.master, text="Number of documents to be analyzed:")
        self.label2 = tkinter.Label(self.master, text="Characteristic categories:")

        self.entry = tkinter.Entry(self.master)
        self.entry2 = tkinter.Entry(self.master)

        self.label.grid(row=0, column=0, sticky=tkinter.W)
        self.label2.grid(row=2, column=0, sticky=tkinter.W)

        self.entry.grid(row=1, column=0)
        self.entry2.grid(row=3, column=0)

        self.button = tkinter.Button(self.master, text="Confirm", command=lambda: self.mainGUI(int(self.entry.get())))

        self.button.grid(row=4, column=0)

    def mainGUI(self, num):
        self.nameLabel = tkinter.Label(self.master, text="Document Names:")
        self.charLabel = tkinter.Label(self.master, text="Characteristics:")
        self.charLabel2 = tkinter.Label(self.master, text='('+self.entry2.get()+')')
        self.filterLabel = tkinter.Label(self.master, text="Text Filters:")
        self.statLabel = tkinter.Label(self.master, text="Statistical Method:")
        self.trainLabel = tkinter.Label(self.master, text="  For training?  ")
        self.predictLabel = tkinter.Label(self.master, text="  For predicting?  ")
        self.resultLabel = tkinter.Label(self.master, text="  RESULTS:    ")

        self.nameEntry = []
        self.charEntry = []
        self.filterEntry = []
        self.statEntry = []
        self.trainBox = []
        self.predictBox = []

        for i in range(num):
            self.nameEntry.append(tkinter.Entry(self.master))
            self.charEntry.append(tkinter.Entry(self.master))
            self.filterEntry.append(tkinter.Entry(self.master))
            self.statEntry.append(tkinter.Entry(self.master))

            self.trainBox.append(tkinter.Checkbutton(self.master))
            self.predictBox.append(tkinter.Checkbutton(self.master))

            self.nameEntry[i].grid(row=i+2, column=0)
            self.charEntry[i].grid(row=i+2, column=1)
            self.filterEntry[i].grid(row=i+2, column=2)
            self.statEntry[i].grid(row=i+2, column=3)

            self.trainBox[i].grid(row=i+2, column=4)
            self.predictBox[i].grid(row=i+2, column=5)

        self.run_button = tkinter.Button(self.master, text="Run", command=lambda: self.update())

        # LAYOUT

        self.nameLabel.grid(row=0, column=0, sticky=tkinter.W)
        self.charLabel.grid(row=0, column=1, sticky=tkinter.W)
        self.charLabel2.grid(row=1, column=1, sticky=tkinter.W)
        self.filterLabel.grid(row=0, column=2, sticky=tkinter.W)
        self.statLabel.grid(row=0, column=3, sticky=tkinter.W)
        self.trainLabel.grid(row=0, column=4)
        self.predictLabel.grid(row=0, column=5)
        self.resultLabel.grid(row=0, column=6, sticky=tkinter.W)

        self.run_button.grid(row=num+2, column=0,columnspan=6)

        self.label.destroy()
        self.label2.destroy()
        self.entry.destroy()
        self.entry2.destroy()
        self.button.destroy()

    def update(self):
        filenamesT = []
        characteristicsT = []
        filtersT = []
        statsMethodsT = []

        filenamesP = []
        characteristicsP = []
        filtersP = []
        statsMethodsP = []

        for i in range(len(self.nameEntry)):
            if self.trainBox[i]:
                filenamesT.append(self.nameEntry[i].get())
                characteristicsT.append(self.charEntry[i].get())
                filtersT.append(self.filterEntry[i].get())
                statsMethodsT.append(self.statEntry[i].get())

            elif self.predictBox[i]:
                filenamesP.append(self.nameEntry[i].get())
                characteristicsP.append(self.charEntry[i].get())
                filtersP.append(self.filterEntry[i].get())
                statsMethodsP.append(self.statEntry[i].get())

        for filename in filenamesT + filenamesP:
            doc = document.Document(filename)
            doc.generateWhole()
            doc.getWordCount()

            wordList = doc._Document__wordList

            stats = basicStats.BasicStats()
            topWords, topFreq = stats.topNHeap(wordList, 10)

            print('Top 10 words and their frequencies:')

            for i in range(len(topWords)):
                print(topWords[i] + ':' + str(topFreq[i]), end = '  ')

            print('\n\n')

            graph = matPlotPloter.MatPlotPloter()
            graph.twoDBarChart(topFreq, topWords)

        '''
        graph = commandLinePloter.CommandLinePloter()
        graph.twoDBar(top10Freq)
        graph.twoDScatter(top10Freq)
        '''

        #docS = documentStream.DocumentStream(filename)
        #docS.writeWhole(doc)

        print(top10Dict)

        matGraph = matPlotPloter.MatPlotPloter()
        matGraph.twoDScatter(top10Freq)
        matGraph.twoDBarChart(top10Freq)


root = tkinter.Tk()
my_gui = UserGUI(root)
root.mainloop()
