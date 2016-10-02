import documentStream
import sentence

class Document:
    """
    This class stores and hides all information about the file to be analyzed.
    """

    def __init__(self,filename):
        self.__sentence = []
        self.__referenceID = 0
        self.__wordCount = 0
        self.__lineCount = 0
        self.__charCount = 0

        self.filename = filename
        self.__title = None
        self.__author = None

        self.__wordList = []

    # sentence getter
    @property
    def sentence(self):
        return self.__sentence

    # sentence setter
    @sentence.setter
    def sentence(self, sentence):
        self.__sentence = sentence


    # reference number ID getter
    @property
    def referenceID(self):
        return self.__referenceID

    # reference number ID setter
    @referenceID.setter
    def referenceID(self, referenceID):
        self.__referenceID = referenceID


    # word count getter
    @property
    def wordCount(self):
        return self.__wordCount

    # word count setter
    @wordCount.setter
    def wordCount(self, wordCount):
        self.__wordCount = wordCount


    # line count getter
    @property
    def lineCount(self):
        return self.__lineCount

    # line count setter
    @lineCount.setter
    def lineCount(self, lineCount):
        self.__lineCount = lineCount


    # Character count getter
    @property
    def charCount(self):
        return self.__charCount

    # Character count setter
    @charCount.setter
    def charCount(self, charCount):
        self.__charCount = charCount


    def generateWhole(self):
        """
        This method uses the readWhole method in DocumentStream and the
        parseWords method in Sentence to parse out information about the
        title (if one exists), as well as store the list of sentences in
        self.__document.
        """
        docStream = documentStream.DocumentStream(self.filename)
        self.__sentence = docStream.readWhole()

        wordList = self.__sentence[0].parseWords()
        isTitle = True

        for word in wordList:
            if not word[0].isupper():
                isTitle = False
                break

        if 'Gutenberg' in self.__sentence[0].sentence:
            self.__title, self.__author = docStream.gutenberg(self.__sentence)

    def getWordCount(self):
        """
        This method returns the number of words (wordCount) in a document.
        """
        if self.__wordCount != 0:
            return self.__wordCount
        else:
            for sent in self.__sentence:
                self.__wordList.extend(sent.parseWords())

            self.__wordCount = len(self.__wordList)

            return self.__wordCount

    def getLineCount(self):
        """
        This method returns the number of lines (paragraphs) in a document.
        """
        if self.__lineCount != 0:
            return self.__lineCount
        else:
            f = open(self.filename, 'r')

            ### Use readline() until the end of the file, increment lineCount by 1.

            while True:
                self.__lineCount += 1
                line = f.readline()
                if line == '':
                    self.__lineCount -= 1
                    break

            f.close()

            return self.__lineCount
