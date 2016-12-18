########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# ScrollingText Class for a Simple MP3 Player                          #
#                                                                      #
# Created on 2016-12-3                                                 #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

import pygame   # For GUI

########################################################################
#                                                                      #
#                         SCROLLINGTEXT CLASS                          #
#                                                                      #
########################################################################

class ScrollingText(object):
    def __init__(self, screen, text, fontSize, x, y, \
                 areaCoord, fps, color, seconds):
        self.screen = screen   # Screen
        self.fps    = fps      # Frames per second
        self.font   = pygame.font.SysFont("Helvetica", fontSize)
        pygame.font.init()
        
        # Scrolling text information
        self.text      = text
        self.textColor = color
        self.x         = x
        self.y         = y
        self.areaCoord = areaCoord
        self.position  = 0

        # To handle scrolling
        self.counter = 1
        self.seconds = seconds

        
        # Draw scrolling text
        self.drawText()

    # Method draws scrolling text
    def drawText(self):
        self.scrollingText = self.font.render(self.text, True,
                                              self.textColor)
        self.screen.blit(self.scrollingText, (self.x, self.y))

    # Method handles scrolling of text
    def update(self):
        # Store coordinate varibales
        x      = self.position
        y      = self.areaCoord[1]
        width  = self.areaCoord[2]
        height = self.areaCoord[3]

        # Draw Text
        self.screen.blit(self.scrollingText, \
                              (self.x, self.y), \
                              (x, y, width, height))

        # Only scroll if text is wider than box
        if self.scrollingText.get_width() > width:
            # Delay scroll by given number of seconds
            if self.counter < self.fps * self.seconds:
                self.counter = self.counter + 1
            else:            
                if self.position < self.scrollingText.get_width():
                    self.position = self.position + 1
                else:
                    self.position = 0
                    self.counter = 1
