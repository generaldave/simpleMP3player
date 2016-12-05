########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Music Class for a Simple MP3 Player                                  #
#                                                                      #
# Created on 2016-12-5                                                 #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

import pygame   # For GUI
import os       # For filesystem path

#######################################################################
#                                                                     #
#                             MUSIC CLASS                             #
#                                                                     #
#######################################################################

class Music(object):
    def __init__(self):
        directory = os.path.dirname(os.path.realpath(__file__)) + "/"
        path         = "Music/Eminem/"
        song         = "2 Evil Deeds.mp3"
        self.song    = directory + path + song
        self.paused  = False
        self.playing = False

    # Method plays / unpauses a song accodringly
    def play(self):
        if self.paused:
            self.pause()
        else:
            if not self.playing:
                self.playing = True
                pygame.mixer.music.load(self.song)
                pygame.mixer.music.play(0)

    # Method pauses / unpauses a song accordingly
    def pause(self):
        if  self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.paused = True
            pygame.mixer.music.pause()

    # Method stops song
    def stop(self):
        self.playing = False
        pygame.mixer.music.stop()

    # Method sets volume
    def setVolume(self, value):
        pygame.mixer.set_volume(value)

    # Methd returns position in song. If none playing, returns 00:00
    def getPosition(self):
        if self.playing:
            position = pygame.mixer.music.get_pos()
            return self.millisecondConverter(position)
        return "00:00"

    # Method returns whether player is busy or not
    def busy(self):
        return pygame.mixer.music.get_busy()

    # Method converts milliseconds to minutes : seconds
    def millisecondConverter(self, value):
        minutes = str(int((value / (1000 * 60)) % 60))
        seconds = str(int(value / 1000) % 60)

        if (len(minutes) < 2):
            minutes = "0" + minutes

        if (len(seconds) < 2):
            seconds = "0" + seconds

        return minutes + ":" + seconds
            

        
