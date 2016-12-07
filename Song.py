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
    title  = ""
    path   = ""

    # Constructor sets title and path
    def __init__(self, title, path):
        self.title = title
        self.path  = path

    # Method returns song title
    def getTitle(self):
        return self.title

    # Method returns song path
    def getPath(self):
        return self.path
