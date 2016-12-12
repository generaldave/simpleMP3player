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

#######################################################################
#                                                                     #
#                            BUTTON CLASS                             #
#                                                                     #
#######################################################################

class Button:
    def __init__(self, screen, text, img):
        self.screen       = screen
        self.text         = text
        self.is_hover     = False
        self.obj          = None
        self.image        = pygame.image.load(img)
        self.defaultImage = img

        self.color = Colour['GRAY']

    # Draws button
    # rectcoord: x, y, width, height
    # imagecoord: x, y
    def draw(self, mouse, rectcoord, imagecoord):
        self.obj  = pygame.draw.rect(self.screen, self.color, rectcoord)
        self.screen.blit(self.image, imagecoord)
      
        # Change color if mouse over button
        self.check_hover(mouse)

    # Handles mouse hover event
    def check_hover(self, mouse):
        if self.obj.collidepoint(mouse):
            self.is_hover = True
        else:
            self.is_hover = False

    # Method sets default image
    def setDefaultImage(self):
        self.image = pygame.image.load(self.defaultImage)
