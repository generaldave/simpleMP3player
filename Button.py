########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Button Class for a Simple MP3 Player                                 #
#                                                                      #
# Created on 2016-12-2                                                 #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Structures import *   # Colour Struct
import pygame                # For GUI

########################################################################
#                                                                      #
#                            BUTTON CLASS                              #
#                                                                      #
########################################################################

class Button:
    def __init__(self, screen, text, img, color):
        self.screen       = screen
        self.text         = text
        self.isHover      = False
        self.obj          = None
        self.image        = pygame.image.load(img)
        self.defaultImage = img

        self.color = color

    # Draws button
    # rectcoord: x, y, width, height
    # imagecoord: x, y
    def draw(self, mouse, rectcoord, imagecoord):
        self.rectcoord = rectcoord
        self.obj  = pygame.draw.rect(self.screen, self.color, rectcoord)
        self.screen.blit(self.image, imagecoord)

    # Handles mouse hover event
    def checkHover(self, mouse):
        x      = self.rectcoord[0]
        y      = self.rectcoord[1]
        width  = self.rectcoord[2]
        height = self.rectcoord[3]

        if ((mouse[X] >= x and mouse[X] <= x + width) and \
            (mouse[Y] >= y and mouse[Y] <= y + height)):
            return True
        else:
            return False

    # Method sets default image
    def setDefaultImage(self):
        self.image = pygame.image.load(self.defaultImage)
