########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# DirectoryBlock Class for a Simple MP3 Player                         #
#                                                                      #
# Created on 2016-12-4                                                 #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Structures    import *   # Colour and Seconds Struct
from   ScrollingText import *   # ScrollingText Class
import pygame                   # For GUI

#######################################################################
#                                                                     #
#                        DIRECTORY BLOCK CLASS                        #
#                                                                     #
#######################################################################

class DirectoryBlock(object):
    def __init__(self, screen, directory, fps):
        self.screen = screen   # Screen
        self.fps    = fps      # Frames per second
        self.timer  = Seconds['THREE']

        # Rect information
        self.rectCoordinates = (10, 182, 260, 52)
        self.rectColor       = Colour['GRAY']

        # Directory information
        self.textColor       = Colour['BLUE']
        self.X               = 67
        self.Y               = 200
        self.directory       = directory
        self.areaCoordinates = (0, 0, 198, 52)
        self.fontSize        = 17

        # Setup Rectangle
        self.setupRect()
        self.setupDirectory()

    # Method changes directory
    def setDirectory(self, directory):
        self.directory = directory
        self.setupDirectory()

    # Method sets up rect
    def setupRect(self):
        self.directoryRect = pygame.draw.rect(self.screen,        \
                                              self.rectColor,     \
                                              self.rectCoordinates)

    # Method sets up directory
    def setupDirectory(self):
        self.directory = ScrollingText(self.screen, self.directory,   \
                                       self.fontSize, self.X, self.Y, \
                                       self.areaCoordinates,          \
                                       self.fps, self.textColor,      \
                                       self.timer)

    # Method updates DirectoryBlock, redraw rec and scroll text
    def update(self):
        self.setupRect()
        self.directory.update()
