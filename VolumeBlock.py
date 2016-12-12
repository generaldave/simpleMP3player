########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# VolumeBlock for a Simple MP3 Player                                  #
#                                                                      #
# Created on 2016-12-11                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Structures import *   # Colour and Seconds Struct
from   Slider     import *   # Slider Class
import pygame                # For GUI

#######################################################################
#                                                                     #
#                          VOLUME BLOCK CLASS                         #
#                                                                     #
#######################################################################

class VolumeBlock(object):
    def __init__(self, screen):
        self.screen = screen   # Screen

        # Slider attributes
        x            = 25
        y            = 119
        width        = 230
        position     = 50   # Percentage
        sliderColor  = Colour['BLUE']
        lowBarColor  = Colour['LIGHTBLUE']
        highBarColor = Colour['LIGHTGRAY']

        # Rect information
        self.rectCoordinates = (10, 100, 260, 33)
        self.rectColor       = Colour['GRAY']

        # Initialize Slider
        self.slider = Slider(screen, x, y, width, position, \
                        sliderColor, lowBarColor, highBarColor)

    # Method returns volume %
    def getVolume(self):
        return (self.slider.getPercent() / 100.0 / 6)

    # Method determines whether or not to draw volume indicator
    def setDrawPercent(self, value):
        self.slider.setDrawPercent(value)

    # Method moves slider with mouse
    def changeSlider(self, position):
        self.slider.changeSlider(position)

    # Method determines whether or not mouse is in boundaries of slider
    def isInBounds(self, mouseX, mouseY):
        return self.slider.isInBounds(mouseX, mouseY)

    # Method determines whether or not slider is in a valid position
    def isValid(self, mouseX):
        return self.slider.isValid(mouseX)

    # Method updates volumeblock
    def update(self):
        pygame.draw.rect(self.screen, self.rectColor, self.rectCoordinates)
        self.slider.update()
