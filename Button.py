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
    def __init__(self, text, img):
        self.text         = text
        self.is_hover     = False
        self.obj          = None
        self.image        = pygame.image.load(img)
        self.defaultImage = img

    # Decide what color the background of the button is accoring
    # to whether the mouse is hovering or not
    def color(self):
        if self.is_hover:
            return Colour['GRAY']
        else:
            return Colour['GRAY']

    # Draws button
    # rectcoord: x, y, width, height
    # imagecoord: x, y
    def draw(self, screen, mouse, rectcoord, imagecoord):
        self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
        screen.blit(self.image, imagecoord)
      
        # Change color if mouse over button
        self.check_hover(mouse)

    # Handles mouse hover event
    def check_hover(self, mouse):
        if self.obj.collidepoint(mouse):
            self.is_hover = True
        else:
            self.is_hover = False

    # Method sets image
    def setImage(self, img):
        self.image = pygame.image.load(img)

    # Method sets default image
    def setDefaultImage(self):
        self.image = pygame.image.load(self.defaultImage)
