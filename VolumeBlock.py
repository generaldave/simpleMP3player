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

########################################################################
#                                                                      #
#                          VOLUME BLOCK CLASS                          #
#                                                                      #
########################################################################

class VolumeBlock(object):
    def __init__(self, screen, directory):
        self.screen    = screen      # Screen
        self.directory = directory   # Directory of app

        # Slider attributes
        x            = 55
        y            = 116
        width        = 150
        position     = 50   # Percentage
        sliderColor  = Colour['COPPER']
        lowBarColor  = Colour['DARKCOPPER']
        highBarColor = Colour['GRAY']

        # Rect information
        self.rectCoordinates = (20, 97, 260, 33)
        self.rectColor       = Colour['DARKGRAY']

        # Initialize speaker image
        self.speaker = pygame.image.load(self.directory + \
                                         "/images/speaker.png")

        # Initialize Slider
        self.slider = Slider(screen, x, y, width, position, \
                        sliderColor, lowBarColor, highBarColor)

    # Method returns volume %
    def getVolume(self):
        return (self.slider.getPercent() / 100.0 / 2)

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
        self.screen.blit(self.speaker, (25, 107))
        self.slider.update()
