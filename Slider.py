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

from   Structures import *   # Structures file
import pygame                # For GUI
import math                  # For comparing mouse location

#######################################################################
#                                                                     #
#                             SLIDER CLASS                            #
#                                                                     #
#######################################################################

class Slider(object):
    def __init__(self, screen, x, y, width, position, \
                 color, lowcolor, highcolor):
        self.screen            = screen   # Screen

        # Slider information
        self.x                 = x
        self.y                 = y
        self.width             = width
        self.percent           = position
        self.currentPosition   = int(width * (position / 100)) + x
        self.sliderColor       = color
        self.lowBarColor       = lowcolor
        self.highBarColor      = highcolor
        self.drawPercent       = False
        
        self.font = pygame.font.SysFont("Helvetica", 14)

    # Return slider percent
    def getPercent(self):
        return self.percent

    # Decide whether or not to draw percent
    def setDrawPercent(self, value):
        self.drawPercent = value

    # Draw bar before slider
    def drawLowBar(self):
        if (self.currentPosition == self.width + self.x):
            coords = (self.x, self.y, self.currentPosition - self.x, 5)
        elif (self.currentPosition < self.width + self.x):
            coords = (self.x, self.y, self.width, 5)
        
        self.lowRect = pygame.draw.rect(self.screen, \
                                        self.lowBarColor, \
                                        coords)

    # Draw bar after slider
    def drawHighBar(self):
        if (self.currentPosition < self.width + self.x):
            coords = (self.currentPosition , self.y, \
                      self.width - self.currentPosition + self.x, 5)
            self.lowRect = pygame.draw.rect(self.screen, \
                                            self.highBarColor, \
                                            coords)

    # Determine coordinates of percentage indicator
    def indicatorPosition(self):
        position = 0
        if (self.percent <= 9):
            position = (self.currentPosition - 4, self.y - 20)
        elif (self.percent <= 99):
            position = (self.currentPosition - 8, self.y - 20)
        else:
            position = (self.currentPosition - 12, self.y - 20)
        return position

    # Draw slider
    def drawSlider(self):
        coords = (self.currentPosition, self.y + 3)
        self.sliderCircle = pygame.draw.circle(self.screen, \
                                               self.sliderColor, \
                                               coords, 8)

        if (self.drawPercent):
            self.sliderPercent = self.font.render(str(self.percent), \
                                                True, \
                                                Colour['LIGHTBLUE'])
            self.screen.blit(self.sliderPercent, self.indicatorPosition())
                                                

    # Change percent and position of slider
    def changeSlider(self, position):
        self.currentPosition = position
        self.percent = int((position - self.x) / self.width*100)

    # Decide whether or not mouse is in boundaries of slider
    def isInBounds(self, mouseX, mouseY):
        if math.hypot(self.currentPosition - mouseX, \
                      self.y + 3 - mouseY) <= 8:
            return self
        return None

    # Decide whether or not slider is in a valid position
    def isValid(self, mouseX):
        if (mouseX < self.x or mouseX > self.width + self.x):
            return False
        return True

    # Update slider
    def update(self):
        self.drawLowBar()
        self.drawHighBar()
        self.drawSlider()
