########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# FileHandler class for a Simple MP3 Player                            #
#                                                                      #
# Created on 2016-11-13                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

import os   # File handling

########################################################################
#                                                                      #
#                          FILEHANDLER CLASS                           #
#                                                                      #
########################################################################

class FileHandler(object):
    def __init__(self, filename):
        directory = os.path.dirname(os.path.realpath(__file__))
        self.filename = directory + "/" + filename

    # Method overwrites file with given tokens
    def write(self, tokens, delimiter):
        try:
            # Declare output string
            outputString = ""

            # Open file as write
            fileObj = open(self.filename, 'w')

            # Create string to write to file
            for token in tokens:
                outputString = outputString + token + delimiter

            # Write tokens to file
            fileObj.write(outputString)

            # Close file
            fileObj.close()
        except:
            print ("Output file error.")

    # Method appends file with given tokens
    def append(self, tokens, delimiter):
        try:
            # Declare output string
            outputString = ""

            # Open file as write
            fileObj = open(self.filename, 'r+')

            # Create string to write to file
            for token in tokens:
                outputString = outputString + token + delimiter

            # Write tokens to file
            fileObj.write(outputString)

            # Close file
            fileObj.close()
        except:
            print ("Output file error.")

    # Method reads file and returns it's contents
    def read(self):
        try:
            # Open file as read
            fileObj = open(self.filename, 'r')

            # Storre file contents
            inputString = fileObj.read()

            # Close file
            fileObj.close()

            # Return file contents
            return inputString
        except:
            print ("Input file error.")
