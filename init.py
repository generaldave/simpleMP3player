########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# GUI Initiator for a Simple MP3 Player                                #
#                                                                      #
# Created on 2016-12-2                                                 #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Structures       import *   # Colour and Seconds Struct
from   Button           import *   # Button Class
from   ScrollingText    import *   # Scrolling Text Class
from   InformationBlock import *   # Information Block Class
from   ButtonBlock      import *   # Buttons Block Class
from   DirectoryBlock   import *   # Directory Block Class
from   TimeBlock        import *   # Directory Block Class
import pygame                      # For GUI

#######################################################################
#                                                                     #
#                        SIMPLEMP3PLAYER CLASS                        #
#                                                                     #
#######################################################################

class SimpleMP3Player(object):
    def __init__(self, directory):
        self.directory = directory
        
        # Initialize pygame
        pygame.init()
        pygame.font.init()
        self.fps = 60
        
        # Call method to set up GUI
        self.setupGUI()

        # Call method to run app
        self.runApp()

    # Method sets up GUI
    def setupGUI(self):
        # Screen attributes
        self.screen = pygame.display.set_mode((280,244))
        pygame.display.set_caption("Simple MP3 Player")
        self.clock = pygame.time.Clock()      # For frames per second
        self.mouse = pygame.mouse.get_pos()   # For mouse position

        # App Icon
        iconFile = self.directory + "/images/icon.gif"
        self.icon = pygame.image.load(iconFile)
        pygame.display.set_icon(self.icon)

        # Setup GUI blocks
        self.setupButtons()
        self.setupInformation()
        self.setupDirectory()
        self.setupTime()

    # Method sets up buttons
    def setupButtons(self):
        self.buttonBlock = ButtonBlock(self.screen, self.directory, \
                                       self.mouse)

    # Method sets up Information Block
    def setupInformation(self):
        Title = "Song Title"
        Path  = "Path/From/Main/Directory"

        # Initialize Information Block
        self.informationBlock = InformationBlock(self.screen, Title, \
                                                 Path, self.fps)

    # Method sets up Directory Block
    def setupDirectory(self):
        Directory = "/Main/Directory/"

        # Initialize Directory Block
        self.directoryBlock = DirectoryBlock(self.screen, Directory, \
                                             self.fps, self.mouse)

    # Method sets up Time Block
    def setupTime(self):
        Time = "2:35"

        self.timeBlock = TimeBlock(self.screen, Time, self.fps)

    # Method runs app
    def runApp(self):
        run = True
        while run == True:
            self.screen.fill(Colour['BLACK'])
            self.mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttonBlock.previousButton.obj.collidepoint(self.mouse):
                        self.buttonBlock.mouseDown("previous")
                    elif self.buttonBlock.playButton.obj.collidepoint(self.mouse):
                        self.buttonBlock.mouseDown("play")
                    elif self.buttonBlock.pauseButton.obj.collidepoint(self.mouse):
                        self.buttonBlock.mouseDown("pause")
                    elif self.buttonBlock.stopButton.obj.collidepoint(self.mouse):
                        self.buttonBlock.mouseDown("stop")
                    elif self.buttonBlock.nextButton.obj.collidepoint(self.mouse):
                        self.buttonBlock.mouseDown("next")
                        title = "Song Two"
                        path  = "Next/Path"
                        self.informationBlock.setSongTitleAndPath(title, \
                                                                  path)
                    elif self.directoryBlock.directoryButton.obj.collidepoint(self.mouse):
                        directory = "/New/Directory/"
                        self.directoryBlock.mouseDown(directory)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.buttonBlock.mouseUp()
                    self.directoryBlock.mouseUp()
            
            self.informationBlock.update()
            self.directoryBlock.update()
            self.timeBlock.update("2:35")
            self.buttonBlock.update()
            pygame.display.update()
            self.clock.tick(self.fps)
            
        # Clean exit
        pygame.quit()
