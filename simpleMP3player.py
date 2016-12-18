########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Driver for a simple MP3 Player                                       #
#                                                                      #
# Created on 2016-12-2                                                 #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   init import *   # init Class - Initializes GUI
import logging         # Log any errors
import os              # For filesystem paths

########################################################################
#                                                                      #
#                                DRIVER                                #
#                                                                      #
########################################################################

# Initialize app
def main():
    player = SimpleMP3Player(directory)

# Begin app, or log error
try:
    # Log file for errors
    directory   = os.path.dirname(os.path.realpath(__file__))
    logFile     = directory + "/logs/error.log"
    errorFormat = '%(asctime)s - %(levelname)s: %(message)s'
    dateFormat  = '%m/%d/%Y %I:%M:%S %p'
    logging.basicConfig(filename = logFile, filemode = 'w', \
                        level = logging.DEBUG,
                        format = errorFormat, \
                        datefmt = dateFormat)
    main()
except:
    logging.exception("")
