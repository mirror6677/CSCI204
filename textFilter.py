import document

class TextFilter:
    """
    This class takes a document and a list of strings (filters to be applied),
    and applies the filters in the list to the document.
    """
    def __init__(self, doc, filterList):
        self.doc = doc
        self.filterList = filterList

    def apply(self):
        """
        Applies filterList, which may include: normalize whitespace, normalize
        case, strip null characters, and strip numbers.
        """
        for f in self.filterList:
            if f == 'normalize whitespace':
                self.normalizeWhitespace()
            elif f == 'normalize case':
                self.normalizeCase()
            elif f == 'strip null characters':
                self.stripNull()
            elif f == 'strip numbers':
                self.stripNumbers()
            elif f == 'strip common words':
                self.stripFile()
            else:
                print(f + ' is not a valid filter!')

    def normalizeWhitespace(self):
        """
        This method deletes all extra whitespaces, and convert any returns to
        a single white space.
        """
        for i in range(len(self.doc._Document__sentence)):
            self.doc._Document__sentence[i].sentence = ' '.join(self.doc._Document__sentence[i].sentence.split())

    def normalizeCase(self):
        """
        This method converts any uppercase letters to lowercase.
        """
        for i in range(len(self.doc._Document__sentence)):
            self.doc._Document__sentence[i].sentence = self.doc._Document__sentence[i].sentence.lower()

    def stripNull(self):
        """
        This method deletes all special characters that are not in the standard
        ASCII set of letters and numbers.
        """
        for i in range(len(self.doc._Document__sentence)):
            self.doc._Document__sentence[i].sentence = ''.join([char for char in self.doc._Document__sentence[i].sentence if 97 <= ord(char) <= 122 or 65 <= ord(char) <= 90 or 48 <= ord(char) <= 57 or ord(char) == 32])

    def stripNumbers(self):
        """
        This method deletes all numbers from the document.
        """
        for i in range(len(self.doc._Document__sentence)):
            self.doc._Document__sentence[i].sentence = ''.join([char for char in self.doc._Document__sentence[i].sentence if char not in '0123456789'])

    def stripFile(self):
        """
        This method opens a file of common words to be striped out.
        Note: this should be used after stripNull was called.
              this method also strips out all extra whitespaces.
        """
        file = open('filterwords.txt', 'r')
        text = file.read()
        wordList = text.split()

        for i in range(len(self.doc._Document__sentence)):
            words = self.doc._Document__sentence[i].sentence.split()
            self.doc._Document__sentence[i].sentence = ' '.join([word for word in words if word not in wordList])

def main():
    d = document.Document('test.txt')
    d.generateWhole()
    #t = TextFilter(d, ['normalize whitespace', 'normalize case', 'strip null characters', 'strip numbers'])
    t = TextFilter(d, ['strip common words'])
    t.apply()
    for i in d._Document__sentence:
        print(i.sentence)

main()
