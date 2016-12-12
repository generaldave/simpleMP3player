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

#######################################################################
#                                                                     #
#                          COLOUR STRUCTURE                           #
#                                                                     #
#######################################################################

Colour = {'WHITE'     : (255, 255, 255), \
          'BLACK'     : (0, 0, 0),       \
          'GRAY'      : (100,100,100),   \
          'LIGHTGRAY' : (143, 143, 143), \
          'BLUE'      : (55,130,231),    \
          'LIGHTBLUE' : (120, 163, 222)}

#######################################################################
#                                                                     #
#                          SECONDS STRUCTURE                          #
#                                                                     #
#######################################################################

Seconds = {'ZERO'  : 0, \
           'ONE'   : 1, \
           'TWO'   : 2, \
           'THREE' : 3, \
           'FOUR'  : 4, \
           'FIVE'  : 5}

#######################################################################
#                                                                     #
#                         X AND Y COORDINATES                         #
#                                                                     #
#######################################################################

X = 0
Y = 1

#######################################################################
#                                                                     #
#                          DIRECTORY CHOOSER                          #
#                                                                     #
#######################################################################

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
