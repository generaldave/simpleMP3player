########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# SongList Class for a simple MP3 Player                               #
#                                                                      #
# Created on 2016-11-30                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Song            import *   # Song class
from   FileHandler     import *   # For config file
from   StringTokenizer import *   # String Tokenizer file
from   Shuffler        import *   # For shuffling songs
from   Structures      import *   # Structures File
import os                         # For searching Directories

#######################################################################
#                                                                     #
#                           SONGLIST CLASS                            #
#                                                                     #
#######################################################################

class SongList:
    # Constructor calls method to populate array with song objects
    def __init__(self, currentDirectory):
        self.songs     = []
        self.songCount = 0
        self.directory = currentDirectory

        # Decide directory and populate song list
        if (self.directory == ""):
            self.chooseDirectory()
            self.populateFromDirectory()
            self.shuffleSongs()
        else:
            self.populateFromFile()

    # Method sets main directory
    def chooseDirectory(self):
        # Choose a Directory
        self.directory = pickDirectory(self.directory)
        self.populateFromDirectory()
        self.shuffleSongs()

    # Method returns song count
    def getSongCount(self):
        return self.songCount

    # Method returns song title
    def getTitle(self, index):
        return self.songs[index].getTitle()

    # Method returns song path
    def getPath(self, index):
        return self.songs[index].getPath()

    # Method returns currently set directory
    def getDirectory(self):
        return self.directory + "/"

    # Method returns whether or not song was played
    def getPlayed(self, index):
        return self.varSongs[index].getPlayed()

    # Method sets whether or not a song was played
    def setPlayed(self, index):
        return self.songs[index].setPlayed()

    # Method sets directory
    def setDirectory(self, value):
        self.directory = value
        
    # Method creates exact path for given song
    def createPath(self, root, element):
        return root + "/" + element

    # Method populates array with song objects from file
    def populateFromFile(self):
        self.songs = []
        self.songCount = 0
        
        fileObj = FileHandler("Songs")
        fileString = fileObj.read()
        tokenizer = StringTokenizer("\n")
        tokenizer.setString(fileString)
        while not tokenizer.atEnd():
            self.songCount = self.songCount + 1
            token = tokenizer.getToken()
            index = token.index("/,")
            name = token[index + 2:]
            path = token[:index + 1]
            self.songs.append(Song(name, path))

    # Method populates array with song objects from directory
    def populateFromDirectory(self):
        self.songs = []
        self.songCount = 0
        for root, dirs, files in os.walk(self.directory):
            for element in files:
                if element.endswith(".mp3"):   # m4a/wma not supported
                    self.songCount = self.songCount + 1
                    name = element.rstrip(".mp3")
                    path = root.lstrip(self.directory) + "/"
                    self.songs.append(Song(name, path))

    # Method shuffles songs
    def shuffleSongs(self):
        shuffler = Shuffler(self.songs)
        shuffler.shuffle()
        self.songs = shuffler.getArray()
