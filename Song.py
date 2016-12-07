########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Song Class for a simple MP3 Player                                   #
#                                                                      #
# Created on 2016-11-30                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                              SONG CLASS                              #
#                                                                      #
########################################################################

class Song:
    varTitle  = ""
    varPath   = ""
    varPlayed = False

    # Constructor sets title and path
    def __init__(self, title, path):
        self.varTitle = title
        self.varPath  = path

    # Method returns song title
    def getTitle(self):
        return self.varTitle

    # Method returns song path
    def getPath(self):
        return self.varPath

    # Method returns whether or not song was played
    def getPlayed(self):
        return self.varPlayed

    # Method sets whether or not a song was played
    def setPlayed(self):
        self.varPlayed = True
