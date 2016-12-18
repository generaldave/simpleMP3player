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

########################################################################
#                                                                      #
#                           SONGLIST CLASS                             #
#                                                                      #
########################################################################

class SongList:
    # Constructor calls method to populate array with song objects
    def __init__(self, directory, musicDirectory):
        self.songs          = []
        self.songCount      = 0
        self.directory      = directory        # App directory
        self.musicDirectory = musicDirectory   # Music directory
        self.chosen         = True             # Was directory chosen

        # Decide directory and populate song list
        if (self.musicDirectory == ""):
            self.chooseDirectory()
        else:
            self.populateFromFile()

    # Method gets self.chosen
    def getChosen(self):
        return self.chosen

    # Method sets main directory
    def chooseDirectory(self):
        # Choose a Directory
        previousDirectory = self.musicDirectory
        directory = pickDirectory(self.musicDirectory)
        if (directory and self.isValid(directory)):
            self.chosen = True
            self.musicDirectory = directory
            self.populateFromDirectory()
            self.shuffleSongs()
        else:
            self.chosen = False

    # Method decides whether chosen directory contains .mp3s
    def isValid(self, directory):
        for root, dirs, files in os.walk(directory):
            for element in files:
                if element.endswith(MP3):
                    return True
        return False

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
        return self.musicDirectory + SLASH

    # Method returns whether or not song was played
    def getPlayed(self, index):
        return self.varSongs[index].getPlayed()

    # Method sets whether or not a song was played
    def setPlayed(self, index):
        return self.songs[index].setPlayed()

    # Method sets directory
    def setDirectory(self, value):
        self.musicDirectory = value
        
    # Method creates exact path for given song
    def createPath(self, root, element):
        return root + SLASH + element

    # Method populates array with song objects from file
    def populateFromFile(self):
        self.songs = []
        self.songCount = 0
        
        fileObj = FileHandler(self.directory, "Songs")
        fileString = fileObj.read()
        tokenizer = StringTokenizer(NEWLINE)
        tokenizer.setString(fileString)
        while not tokenizer.atEnd():
            self.songCount = self.songCount + 1
            token = tokenizer.getToken()
            index = token.index("/,")
            name  = token[index + 2:]
            path  = token[:index + 1]
            self.songs.append(Song(name, path))

    # Method populates array with song objects from directory
    def populateFromDirectory(self):
        self.songs = []
        self.songCount = 0
        for root, dirs, files in os.walk(self.musicDirectory):
            for element in files:
                if element.endswith(MP3):
                    self.songCount = self.songCount + 1
                    mp3Index = len(element) - len(MP3)
                    name = element[:mp3Index]
                    slashIndex = len(self.musicDirectory) + len(SLASH)
                    path = root[slashIndex:] + SLASH
                    self.songs.append(Song(name, path))

    # Method shuffles songs
    def shuffleSongs(self):
        shuffler = Shuffler(self.songs)
        shuffler.shuffle()
        self.songs = shuffler.getArray()
