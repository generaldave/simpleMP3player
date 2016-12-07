# David Fuller
#
# 7-27-2016

# Define a string tokenizer class
class StringTokenizer(object):
    # Constructor
    def __init__(self, delimiter):
        self.string = ""
        self.currentIndex = 0
        self.delimiter = delimiter

    # Mutator sets string to tokenize
    def setString(self, string):
        self.string = string

    # Accessor: returns string
    def getString(self):
        return self.string

    # Decide whether or not tokenizer is at the
    # end of the string
    def atEnd(self):
        if (self.currentIndex == len(self.string)):
            return True
        return False

    # Return next token
    def getToken(self):
        newIndex = self.string.find(self.delimiter, self.currentIndex)
        if (newIndex >= 0):
            tempString = self.string[self.currentIndex:newIndex]
            self.currentIndex = newIndex + 1
        else:
            tempString = self.string[self.currentIndex:]
            self.currentIndex = len(self.string)
        return tempString
