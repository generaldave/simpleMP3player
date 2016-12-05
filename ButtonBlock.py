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
import os                # For filesystem paths

#######################################################################
#                                                                     #
#                        DIRECTORY BLOCK CLASS                        #
#                                                                     #
#######################################################################

class ButtonBlock(object):
    # File's directory
    path = os.path.dirname(os.path.realpath(__file__))
    
    def __init__(self, screen, directory, mouse):
        self.screen   = screen   # Screen
        self.mouse    = mouse    # For mouse position

        # Previous button information
        self.previousRectCoord = (10,100,52,52)
        self.previousCoord     = (11,101)
        self.previousUp        = "/images/previous.png"
        self.previousDown      = "/images/previousDown.png"

        # Play button information
        self.playRectCoord = (62,100,52,52)
        self.playCoord     = (63,101)
        self.playUp        = "/images/play.png"
        self.playDown      = "/images/playDown.png"

        # Pause button information
        self.pauseRectCoord = (114,100,52,52)
        self.pauseCoord     = (115,101)
        self.pauseUp        = "/images/pause.png"
        self.pauseDown      = "/images/pauseDown.png"

        # Stop button information
        self.stopRectCoord = (166,100,52,52)
        self.stopCoord     = (167,101)
        self.stopUp        = "/images/stop.png"
        self.stopDown      = "/images/stopDown.png"

        # Next button information
        self.nextRectCoord = (218,100,52,52)
        self.nextCoord     = (219,101)
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
                                     self.path + \
                                     self.previousImage)
        self.playButton     = Button(self.screen, 'next', \
                                     self.path + \
                                     self.playImage)
        self.pauseButton    = Button(self.screen, 'next', \
                                     self.path + \
                                     self.pauseImage)
        self.stopButton     = Button(self.screen, 'next', \
                                     self.path + \
                                     self.stopImage)
        self.nextButton     = Button(self.screen, 'next', \
                                     self.path + \
                                     self.nextImage)

        # Draw Buttons
        self.drawButtons()

    # Method changes image for mouse down
    def mouseDown(self, button):
        if (button == "previous"):
            self.previousImage = self.previousDown
        elif (button == "play"):
            self.playImage = self.playDown
        elif (button == "pause"):
            self.pauseImage = self.pauseDown
        elif (button == "stop"):
            self.stopImage = self.stopDown
        elif (button == "next"):
            self.nextImage = self.nextDown
            
    # Method changes image for mouse down
    def mouseUp(self):
        self.previousImage = self.previousUp
        self.playImage     = self.playUp
        self.pauseImage    = self.pauseUp
        self.stopImage     = self.stopUp
        self.nextImage     = self.nextUp

    # Method updates ButtonBlock, redraw buttons
    def update(self):
        self.setupButtons()
