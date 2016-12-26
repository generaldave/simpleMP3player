########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# ButtonBlock Class for a Simple MP3 Player                            #
#                                                                      #
# Created on 2016-12-4                                                 #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Button import *   # Button Class
import pygame            # For GUI

########################################################################
#                                                                      #
#                        DIRECTORY BLOCK CLASS                         #
#                                                                      #
########################################################################

class ButtonBlock(object):
    def __init__(self, screen, directory, mouse):
        self.screen    = screen      # Screen
        self.directory = directory   # Directory of app
        self.mouse     = mouse       # For mouse position

        # Previous button information
        self.previousRectCoord = (20,132,52,52)
        self.previousCoord     = (21,133)
        self.previousUp        = "/images/previous.png"
        self.previousDown      = "/images/previousDown.png"

        # Play button information
        self.playRectCoord = (72,132,52,52)
        self.playCoord     = (73,133)
        self.playUp        = "/images/play.png"
        self.playDown      = "/images/playDown.png"

        # Pause button information
        self.pauseRectCoord = (124,132,52,52)
        self.pauseCoord     = (125,133)
        self.pauseUp        = "/images/pause.png"
        self.pauseDown      = "/images/pauseDown.png"

        # Stop button information
        self.stopRectCoord = (176,132,52,52)
        self.stopCoord     = (177,133)
        self.stopUp        = "/images/stop.png"
        self.stopDown      = "/images/stopDown.png"

        # Next button information
        self.nextRectCoord = (228,132,52,52)
        self.nextCoord     = (229,133)
        self.nextUp        = "/images/next.png"
        self.nextDown      = "/images/nextDown.png"

        # Store button images
        self.previousImage = self.previousUp
        self.playImage     = self.playUp
        self.pauseImage    = self.pauseUp
        self.stopImage     = self.stopUp
        self.nextImage     = self.nextUp
        
        # Setup ButtonBlock
        self.setupButtons()

    # Method Draws buttons
    def drawButtons(self):
        self.previousButton.draw(self.mouse, self.previousRectCoord, \
                                 self.previousCoord)
        self.playButton.draw(self.mouse, self.playRectCoord, \
                             self.playCoord)
        self.pauseButton.draw(self.mouse, self.pauseRectCoord, \
                              self.pauseCoord)
        self.stopButton.draw(self.mouse, self.stopRectCoord, \
                             self.stopCoord)
        self.nextButton.draw(self.mouse, self.nextRectCoord, \
                             self.nextCoord)

    # Method sets up buttons
    def setupButtons(self):
        # Initialize buttons
        self.previousButton = Button(self.screen, 'next', \
                                     self.directory + \
                                     self.previousImage, \
                                     Colour['GRAY'])
        self.playButton     = Button(self.screen, 'next', \
                                     self.directory + \
                                     self.playImage, \
                                     Colour['GRAY'])
        self.pauseButton    = Button(self.screen, 'next', \
                                     self.directory + \
                                     self.pauseImage, \
                                     Colour['GRAY'])
        self.stopButton     = Button(self.screen, 'next', \
                                     self.directory + \
                                     self.stopImage, \
                                     Colour['GRAY'])
        self.nextButton     = Button(self.screen, 'next', \
                                     self.directory + \
                                     self.nextImage, \
                                     Colour['GRAY'])

        # Draw Buttons
        self.drawButtons()

    # Method changes image for mouse hover
    def mouseHover(self, button):
        if (button == "Previous"):
            self.previousImage = self.previousDown
        elif (button == "Play"):
            self.playImage = self.playDown
        elif (button == "Pause"):
            self.pauseImage = self.pauseDown
        elif (button == "Stop"):
            self.stopImage = self.stopDown
        elif (button == "Next"):
            self.nextImage = self.nextDown
            
    # Method changes image for mouse unhover
    def mouseUnHover(self, button):
        if (button == "Previous"):
            self.previousImage = self.previousUp        
        elif (button == "Play"):
            self.playImage = self.playUp            
        elif (button == "Pause"):
            self.pauseImage = self.pauseUp
        elif (button == "Stop"):
            self.stopImage = self.stopUp
        elif (button == "Next"):
            self.nextImage  = self.nextUp
    
    # Method determines whether or not mouse is in bounds of a button
    def isInBounds(self, mouse, button):
        if (button == "Previous"):
            return self.previousButton.checkHover(mouse)
        elif (button == "Play"):
            return self.playButton.checkHover(mouse)
        elif (button == "Pause"):
            return self.pauseButton.checkHover(mouse)
        elif (button == "Stop"):
            return self.stopButton.checkHover(mouse)
        elif (button == "Next"):
            return self.nextButton.checkHover(mouse)
        
    # Method updates ButtonBlock, redraw buttons
    def update(self):
        self.setupButtons()
