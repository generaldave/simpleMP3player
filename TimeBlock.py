########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# TimeBlock Class for a Simple MP3 Player                              #
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
from   ScrollingText import *   # ScrollingText Class
import pygame                   # For GUI

########################################################################
#                                                                      #
#                          TIME BLOCK CLASS                            #
#                                                                      #
########################################################################

class TimeBlock(object):
    def __init__(self, screen, time, fps):
        self.screen = screen   # Screen
        self.fps    = fps      # Frames per second
        self.font   = pygame.font.SysFont("Helvetica", 14)

        # Directory information
        self.textColor   = Colour['COPPER']
        self.coordinates = (224, 108)
        self.time        = time

        # Setup Rectangle
        self.setupTime()

    # Method sets up time
    def setupTime(self):
        self.timer = self.font.render(self.time, True, self.textColor)
        self.screen.blit(self.timer, self.coordinates)

    # Method updates DirectoryBlock, redraw rec and scroll text
    def update(self, time):
        self.time = time
        self.setupTime()
