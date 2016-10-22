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
            else:
                print(f + ' is not a valid filter!')

    def normalizeWhitespace(self):
        """
        This method deletes all extra whitespaces, and convert any returns to
        a single white space.
        """
        for i in range(doc._Document__sentence.length):
            doc._Document__sentence[i] = ' '.join(doc._Document__sentence[i].split())

    def normalizeCase(self):
        """
        This method converts any uppercase letters to lowercase.
        """
        for i in range(doc._Document__sentence.length):
            doc._Document__sentence[i] = doc._Document__sentence[i].lower()

    def stripNull(self):
        """
        This method deletes all special characters that are not in the standard
        ASCII set of letters and numbers.
        """
        for i in range(doc._Document__sentence.length):
            doc._Document__sentence[i] = ''.join([char for char in doc._Document__sentence[i] if 0 <= ord(char) <= 127])

    def stripNumbers(self):
        """
        This method deletes all numbers from the document.
        """
        for i in range(doc._Document__sentence.length):
            doc._Document__sentence[i] = ''.join([char for char in doc._Document__sentence[i] if char not in '0123456789'])
