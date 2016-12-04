########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# InformationBlock Class for a Simple MP3 Player                       #
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
#                       INFORMATON BLOCK CLASS                        #
#                                                                     #
#######################################################################

class InformationBlock(object):
    def __init__(self, screen, title, path, fps):
        self.screen = screen   # Screen
        self.fps    = fps      # Frames per second
        self.timer  = Seconds['THREE']

        # Rect information
        self.rectCoordinates = (10, 10, 260, 80)
        self.rectColor       = Colour['GRAY']

        # Song information
        self.textColor            = Colour['BLUE']
        self.X                    = 15
        self.title                = title
        self.titleAreaCoordinates = (0, 0, 175, 80)
        self.titleFontSize        = 22
        self.titleY               = 18
        self.path                 = path
        self.pathAreaCoordinates  = (0, 0, 250, 80)
        self.pathFontSize         = 17
        self.pathY                = 55

        # Setup objects
        self.setupRect()
        self.setupSongTitle()
        self.setupSongPath()

    # Method changes song title and path
    def setSongTitleAndPath(self, title, path):
        self.title = title
        self.path  = path
        self.setupSongTitle()
        self.setupSongPath()

    # Method sets up rect
    def setupRect(self):
        self.informationRect = pygame.draw.rect(self.screen,        \
                                                self.rectColor,     \
                                                self.rectCoordinates)

    # Method sets up song title
    def setupSongTitle(self):
        self.songTitle = ScrollingText(self.screen, self.title,   \
                                       self.titleFontSize,        \
                                       self.X, self.titleY,       \
                                       self.titleAreaCoordinates, \
                                       self.fps, self.textColor,  \
                                       self.timer)

    # Method sets up song path
    def setupSongPath(self):
        self.songPath = ScrollingText(self.screen, self.path,   \
                                      self.titleFontSize,       \
                                      self.X, self.pathY,       \
                                      self.pathAreaCoordinates, \
                                      self.fps, self.textColor, \
                                      self.timer)

    # Method updates InformationBlock, redraw rect and scroll text
    def update(self):
        self.setupRect()
        self.songTitle.update()
        self.songPath.update()
