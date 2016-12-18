########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Shuffler Class for a Simple MP3 Player                               #
#                                                                      #
# Created on 2016-11-30                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

import random   # For shuffling array

########################################################################
#                                                                      #
#                           SHUFFLER CLASS                             #
#                                                                      #
########################################################################

class Shuffler:
    TIMES_TO_SHUFFLE = 10
    
    def __init__(self, arrayIn):
        self.array = arrayIn

    # Method returns array
    def getArray(self):
        return self.array

    # Method shuffles an array
    def shuffle(self):
        # Shuffles array 10 times
        for i in range(self.TIMES_TO_SHUFFLE):
            max = len(self.array) - 1
            randMax = len(self.array) - 1
            for x in range(max):
                index = random.randrange(randMax)
                temp = self.array[index]
                self.array[index] = self.array[randMax]
                self.array[randMax] = temp
                randMax = randMax - 1
