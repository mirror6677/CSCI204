class Sentence:
    """
    This class takes in a string (sentence) and can parse the sentence
    into list of words and characters.
    """

    def __init__(self, sentence):
        self.wordCount = 0
        self.charCount = 0

        if sentence[-1] in '!?.;':
            self.punctuation = sentence[-1]
            self.sentence = sentence[:-1]
        else:
            self.punctuation = ''
            self.sentence = sentence

    def parseWords(self):
        """
        This method parses the words in sentence and return a list of words.
        """
        wordList = []
        word = ''

        for char in self.sentence:
            if char != ' ':
                word += char
            elif word != '':
                wordList.append(word)
                word = ''

        if word != '':
            wordList.append(word)

        return wordList

    def parseChar(self):
        """
        This method parses the characters in sentence and return a list of characters.
        """
        charList = []

        for char in self.sentence:
            charList.append(char)

        return charList
