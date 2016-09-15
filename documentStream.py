import document
import sentence
import documentStreamError as dse
import os.path

class DocumentStream:
    """
    This class handles file read and write tasks.
    """

    def __init__(self, filename):
        self.filename = filename

    def readWhole(self):
        """
        This method read from a file and returns a list of Sentence objects.
        """
        try:
            if os.path.isfile(self.filename) == False:
                raise dse.DocumentStreamError("Not a file!")
        except dse.DocumentStreamError as E:
            print(E.data)
            exit()

        f = open(self.filename, 'r')

        fileString = f.read()
        f.close()

        fileString = [c for c in fileString if c not in ['\n', '\t']]   # Remove all returns in the string

        sentenceList = []
        sent = ''
        spaceState = False


        ### If char is .!?; or new line, append sentence to sentenceList
        ### and reset sentence to empty string.

        for char in fileString:
            if char == ' ':
                if spaceState == True and len(sent) > 0:
                    sentenceList.append(sentence.Sentence(sent))
                    sent = ''
                elif spaceState == False:
                    sent += char
                spaceState = True
            else:
                spaceState = False
                sent += char
                if char in '.!?;':
                    sentenceList.append(sentence.Sentence(sent))
                    sent = ''

        if sent != '':
            sentenceList.append(sentence.Sentence(sent))

        ### Handles the case that a sentence begins or ends with a space character.

        for i in range(len(sentenceList)):
            if sentenceList[i].sentence[0] == ' ':
                sentenceList[i] = sentence.Sentence(sentenceList[i].sentence[1:])
            if sentenceList[i].sentence[-1] == ' ':
                sentenceList[i] = sentence.Sentence(sentenceList[i].sentence[:-1])

        return sentenceList

    def writeWhole(self, document):
        """
        This method takes a Document object as input, and writes it into a file,
        with one sentence per output line.
        """
        sentenceString + ''

        for i in range(len(document._Document__sentence)):
            sentenceString += document._Document__sentence[i].sentence + '\n'

        newFilename = self.filename[:-4] + '_copy.txt'
        f = open(newFilename, 'w')
        f.write(sentenceString)
        f.close()
