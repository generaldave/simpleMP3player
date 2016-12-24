########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# SongsBlock Class for a Simple MP3 Player                             #
#                                                                      #
# Created on 2016-12-13                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Structures import *   # Colour and Seconds Struct
import pygame                # For GUI

########################################################################
#                                                                      #
#                          SONG BLOCK CLASS                            #
#                                                                      #
########################################################################

class SongsBlock(object):
    def __init__(self, screen, directory, songs, index):
        self.screen    = screen      # Screen
        self.directory = directory   # Directory of app
        self.songs     = songs       # List of songs
        self.index     = index       # Song index
        self.font      = pygame.font.SysFont("Helvetica", 14)

        self.sticky = pygame.image.load(self.directory + \
                                        "/images/sticky.png")

        # Song List Block information
        self.rectCoord = (20, 186, 260, 101)
        self.rectColor = Colour['DARKGRAY']
        self.textColor = Colour['DARKCOPPER']

        # Song coordinates
        self.previousCoord = (53, 209)
        self.currentCoord  = (53, 231)
        self.nextCoord     = (53, 253)

        # Set up rectangle
        self.setupRect()
        self.drawSongs()

    # Method returns song count
    def getSongCount(self):
        return self.songs.getSongCount()

    # Method sets up rectangle
    def setupRect(self):
        self.songlistRect = pygame.draw.rect(self.screen, \
                                             self.rectColor, \
                                             self.rectCoord)

    # Method draws songs
    def drawSongs(self):
        self.screen.blit(self.sticky, (25, 222))

        songcount = self.songs.getSongCount()
        # Previous Song
        if (songcount >= 3):
            if (self.index == 0):
                index = songcount - 1
            else:
                index = self.index - 1
            previousSong  = self.songs.getTitle(index)[:32]
            self.previous = self.font.render(previousSong, True, \
                                             self.textColor)
            self.screen.blit(self.previous, self.previousCoord)
        
        # Current Song
        currentSong  = self.songs.getTitle(self.index)[:32]
        self.current = self.font.render(currentSong, True, \
                                        self.textColor)
        self.screen.blit(self.current, self.currentCoord)
        
        # Next Song
        if (songcount >= 3):
            if (self.index == songcount - 1):
                index = 0
            else:
                index = self.index + 1
            nextSong  = self.songs.getTitle(index)[:32]
            self.next = self.font.render(nextSong, True, \
                                         self.textColor)
            self.screen.blit(self.next, self.nextCoord)

    # Method updates Song List Block
    def update(self, index):
        self.index = index
        self.setupRect()
        self.drawSongs()
