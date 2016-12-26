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

########################################################################
#                                                                      #
#                        DIRECTORY BLOCK CLASS                         #
#                                                                      #
########################################################################

class DirectoryBlock(object):
    def __init__(self, screen, directory, musicDirectory, fps, mouse):
        self.screen         = screen           # Screen
        self.directory      = directory        # Directory of app
        self.musicDirectory = musicDirectory   # Music directory
        self.fps            = fps              # Frames per second
        self.mouse          = mouse            # For mouse position
        self.timer          = Seconds['THREE']
        self.image          = "/images/directory.png"
        
        # Rect information
        self.rectCoordinates = (20, 290, 260, 52)
        self.rectColor       = Colour['GRAY']

        # Directory information
        self.textColor       = Colour['COPPER']
        self.X               = 77
        self.Y               = 307
        self.musicDirectory  = musicDirectory.rstrip(SLASH) + SLASH
        self.areaCoordinates = (0, 0, 198, 52)
        self.fontSize        = 17

        # Setup DirectoryBlock
        self.setupRect()
        self.setupDirectory()

    # Method sets up rect
    def setupRect(self):
        self.directoryRect = pygame.draw.rect(self.screen,        \
                                              self.rectColor,     \
                                              self.rectCoordinates)

    # Method draws button
    def drawButton(self):
        imagePath = self.directory + self.image
        self.directoryButton = Button(self.screen, 'directory', imagePath, \
                                      Colour['GRAY'])
        self.directoryButton.draw(self.mouse, \
                                 (20,290,52,52), (21,291))

    # Method sets up directory
    def setupDirectory(self):
        self.drawButton()
        
        self.directoryText = ScrollingText(self.screen,                \
                                           self.musicDirectory,        \
                                           self.fontSize,              \
                                           self.X, self.Y,             \
                                           self.areaCoordinates,       \
                                           self.fps, self.textColor,   \
                                           self.timer)

    # Method handles directory work
    def mouseDown(self, directory):
        self.musicDirectory = directory
        self.setupDirectory()

    # Method changes image for mouse hover
    def mouseHover(self):
        self.image = "/images/directoryDown.png"
        self.drawButton()      

    # Method changes image for mouse down
    def mouseUnHover(self):
        self.image = "/images/directory.png"
        self.drawButton()

    # Method decides whether mouse is in boundaries of directory button
    def isInBounds(self, mouse):
        return self.directoryButton.checkHover(mouse)

    # Method updates DirectoryBlock, redraw rec and scroll text
    def update(self):
        self.setupRect()
        self.directoryText.update()
        self.drawButton()
