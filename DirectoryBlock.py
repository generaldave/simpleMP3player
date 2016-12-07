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
from   Button        import *   # Button Class
from   ScrollingText import *   # ScrollingText Class
import pygame                   # For GUI
import os                       # For filesystem paths

#######################################################################
#                                                                     #
#                        DIRECTORY BLOCK CLASS                        #
#                                                                     #
#######################################################################

class DirectoryBlock(object):
    # File's directory
    path = os.path.dirname(os.path.realpath(__file__))
    
    def __init__(self, screen, directory, fps, mouse):
        self.screen = screen    # Screen
        self.fps    = fps       # Frames per second
        self.mouse  = mouse     # For mouse position
        self.timer  = Seconds['THREE']
        self.image  = "/images/directory.png"
        
        # Rect information
        self.rectCoordinates = (10, 182, 260, 52)
        self.rectColor       = Colour['GRAY']

        # Directory information
        self.textColor       = Colour['BLUE']
        self.X               = 67
        self.Y               = 200
        self.directory       = directory.rstrip("/") + "/"
        self.areaCoordinates = (0, 0, 198, 52)
        self.fontSize        = 17

        # Setup DirectoryBlock
        self.setupRect()
        self.setupDirectory()

    # Method changes directory
##    def setDirectory(self, directory):
##        self.setupDirectory()

    # Method sets up rect
    def setupRect(self):
        self.directoryRect = pygame.draw.rect(self.screen,        \
                                              self.rectColor,     \
                                              self.rectCoordinates)

    # Method sets up directory
    def setupDirectory(self):
        imagePath = self.path + self.image
        self.directoryButton = Button(self.screen, 'directory', imagePath)
        self.directoryButton.draw(self.mouse, \
                                 (10,182,52,52), (11,183))
        
        self.directoryText = ScrollingText(self.screen, self.directory,   \
                                           self.fontSize, self.X, self.Y, \
                                           self.areaCoordinates,          \
                                           self.fps, self.textColor,      \
                                           self.timer)

    # Method changes image for mouse down
    def mouseDown(self, directory):
        self.image = "/images/directoryDown.png"
        self.directory = directory
        self.setupDirectory()

    # Method changes image for mouse down
    def mouseUp(self):
        self.image = "/images/directory.png"
        self.setupDirectory()

    # Method updates DirectoryBlock, redraw rec and scroll text
    def update(self):
        self.setupRect()
        self.directoryText.update()
        self.directoryButton.draw(self.mouse, \
                                 (10,182,52,52), (11,183))
