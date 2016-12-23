########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Structures for a Simple MP3 Player                                   #
#                                                                      #
# Created on 2016-12-2                                                 #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from tkinter import *   # Used for directory chooser window
from tkinter import filedialog

########################################################################
#                                                                      #
#                              CONSTANTS                               #
#                                                                      #
########################################################################

TITLE      = "Path of MP3s"   # App title
RESOLUTION = (301,423)        # App resolution = w x h
NEWLINE    = "\n"             # New line character
MP3        = ".mp3"           # Supported music file extension
SLASH      = "/"              # Used for directories
SONGEND    = 444              # End of song
X          = 0                # X coordinate for mouse
Y          = 1                # Y coordinate for mouse

########################################################################
#                                                                      #
#                          COLOUR STRUCTURE                            #
#                                                                      #
########################################################################

Colour = {'WHITE'      : (255, 255, 255), \
          'BLACK'      : (0, 0, 0),       \
          'GRAY'       : (30, 32, 30),    \
          'DARKGRAY'   : (15, 17, 15),    \
          'COPPER'     : (163, 141, 109), \
          'DARKCOPPER' : (143, 121, 89)}

########################################################################
#                                                                      #
#                          SECONDS STRUCTURE                           #
#                                                                      #
########################################################################

Seconds = {'ZERO'  : 0, \
           'ONE'   : 1, \
           'TWO'   : 2, \
           'THREE' : 3, \
           'FOUR'  : 4, \
           'FIVE'  : 5}

########################################################################
#                                                                      #
#                          DIRECTORY CHOOSER                           #
#                                                                      #
########################################################################

def pickDirectory(currentDirectory):
    # Start a hidden tkinter window
    root = Tk()
    root.withdraw()

    # Directory chooser options
    options = {}
    options['initialdir'] = currentDirectory
    options['mustexist']  = False
    options['parent']     = root
    options['title']      = "Choose music directory"

    # Choose directory
    directory = filedialog.askdirectory(**options)

    # Kill tkinter object
    root.destroy()

    # Return directory
    return directory
