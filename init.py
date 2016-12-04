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

        # Initialize buttons
        self.previousButton  = Button('previous', \
                                      self.directory + \
                                      "/images/previous.png")
        self.playButton      = Button('play', \
                                      self.directory + \
                                      "/images/play.png")
        self.pauseButton     = Button('pause', \
                                      self.directory + \
                                      "/images/pause.png")
        self.stopButton      = Button('stop', \
                                      self.directory + \
                                      "/images/stop.png")
        self.nextButton      = Button('next', \
                                      self.directory + \
                                      "/images/next.png")
        self.directoryButton = Button('next', \
                                      self.directory + \
                                      "/images/directory.png")

        self.setupInformation()
        self.setupDirectory()
        self.setupTime()

    # Method draws buttons
    def drawButtons(self):
        self.previousButton.draw(self.screen, self.mouse, \
                                 (10,100,52,52), (11,101))
        self.playButton.draw(self.screen, self.mouse, \
                             (62,100,52,52), (63,101))
        self.pauseButton.draw(self.screen, self.mouse, \
                              (114,100,52,52), (115,101))
        self.stopButton.draw(self.screen, self.mouse, \
                             (166,100,52,52), (167,101))
        self.nextButton.draw(self.screen, self.mouse, \
                             (218,100,52,52), (219,101))
        self.directoryButton.draw(self.screen, self.mouse, \
                                 (10,182,52,52), (11,183))

    # Method sets up Information Block
    def setupInformation(self):
        Title = "War Pigs"
        Path  = "Black Sabbath/Paranoid"

        # Initialize Information Block
        self.informationBlock = InformationBlock(self.screen, Title, \
                                                 Path, self.fps)

    # Method sets up Directory Block
    def setupDirectory(self):
        Directory = "/media/generaldave/storage/Music/"

        # Initialize Directory Block
        self.directoryBlock = DirectoryBlock(self.screen, Directory, \
                                             self.fps)

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
                    if self.previousButton.obj.collidepoint(self.mouse):
                        image = self.directory + "/images/previousDown.png"
                        self.previousButton.setImage(image)
                    elif self.playButton.obj.collidepoint(self.mouse):
                        image = self.directory + "/images/playDown.png"
                        self.playButton.setImage(image)
                    elif self.pauseButton.obj.collidepoint(self.mouse):
                        image = self.directory + "/images/pauseDown.png"
                        self.pauseButton.setImage(image)
                    elif self.stopButton.obj.collidepoint(self.mouse):
                        image = self.directory + "/images/stopDown.png"
                        self.stopButton.setImage(image)
                    elif self.nextButton.obj.collidepoint(self.mouse):
                        image = self.directory + "/images/nextDown.png"
                        self.nextButton.setImage(image)
                        title = "Paranoid"
                        path  = "Black Sabbath/Paranoid"
                        self.informationBlock.setSongTitleAndPath(title, \
                                                                  path)
                    elif self.directoryButton.obj.collidepoint(self.mouse):
                        image = self.directory + "/images/directoryDown.png"
                        self.directoryButton.setImage(image)
                        Directory = "/New/Directory/"
                        self.directoryBlock.setDirectory(Directory)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.previousButton.setDefaultImage()
                    self.playButton.setDefaultImage()
                    self.pauseButton.setDefaultImage()
                    self.stopButton.setDefaultImage()
                    self.nextButton.setDefaultImage()
                    self.directoryButton.setDefaultImage()
            
            self.informationBlock.update()
            self.directoryBlock.update()
            self.timeBlock.update("2:35")
            self.drawButtons()
            pygame.display.update()
            self.clock.tick(self.fps)
            
        # Clean exit
        pygame.quit()
