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

#######################################################################
#                                                                     #
#                                DRIVER                               #
#                                                                     #
#######################################################################

# Initialize app
def main():
    player = SimpleMP3Player(directory)

# Log file for errors
directory = os.path.dirname(os.path.realpath(__file__))
logFile = directory + "/logs/error.log"
logging.basicConfig(filename = logFile, filemode = 'w', \
                    level = logging.DEBUG,
                    format = '%(asctime)s - %(levelname)s: %(message)s', \
                    datefmt = '%m/%d/%Y %I:%M:%S %p')

# Begin app, or log error
try:
    main()
except:
    logging.exception("")
