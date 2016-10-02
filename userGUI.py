#from tkinter import Tk, Label, Button, Entry, END, W, E
import document, matPlotPloter, basicStats, commandLinePloter
import tkinter


class UserGUI:
    def __init__(self, master):
        self.master = master
        master.title("UserGUI")

        self.label = tkinter.Label(master, text="Filename:")
        self.entry = tkinter.Entry(master,validate='key')

        self.run_button = tkinter.Button(master, text="Run", command=lambda: self.update())

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=tkinter.W)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=tkinter.W+tkinter.E)

        self.run_button.grid(row=2, column=0,columnspan=3)

    def update(self):

        filename = self.entry.get()

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
