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

from   SongList         import *   # SongList Class
from   Structures       import *   # Colour and Seconds Struct
from   Button           import *   # Button Class
from   ScrollingText    import *   # Scrolling Text Class
from   InformationBlock import *   # Information Block Class
from   ButtonBlock      import *   # Buttons Block Class
from   DirectoryBlock   import *   # Directory Block Class
from   TimeBlock        import *   # Directory Block Class
from   VolumeBlock      import *   # Volume Block Class
from   Music            import *   # Handles the music
from   FileHandler      import *   # For config file
from   StringTokenizer  import *   # String Tokenizer file
import pygame                      # For GUI

#######################################################################
#                                                                     #
#                        SIMPLEMP3PLAYER CLASS                        #
#                                                                     #
#######################################################################

class SimpleMP3Player(object):
    currentSong = 0   # Song number
    
    def __init__(self, directory):
        self.directory = directory   # Directory of app
        
        # Initialize pygame
        pygame.init()
        pygame.font.init()
        self.fps = 60

        # Read config file
        self.configFile()

        # Initialize song list
        self.songs = SongList(self.musicDirectory)
        self.musicDirectory = self.songs.getDirectory()
        self.musicDirectory = self.musicDirectory.rstrip("/") + "/"
        
        # Initialize music player
        self.musicPlayer = Music()

        # Set up song information
        path = self.songs.getPath(self.currentSong)
        title = self.songs.getTitle(self.currentSong)
        self.musicPlayer.setSongInformation(self.musicDirectory,
                                            path, title)
        
        # Call method to set up GUI
        self.setupGUI()

        # Call method to run app
        self.runApp()

    # Method sets up GUI
    def setupGUI(self):
        # Screen attributes
        self.screen = pygame.display.set_mode((280,277))
        pygame.display.set_caption("Simple MP3 Player")
        self.clock = pygame.time.Clock()      # For frames per second
        self.mouse = pygame.mouse.get_pos()   # For mouse position

        # App Icon
        iconFile = self.directory + self.iconPath
        self.icon = pygame.image.load(iconFile)
        pygame.display.set_icon(self.icon)

        # Setup GUI blocks
        self.setupButtons()
        self.setupInformation()
        self.setupDirectory()
        self.setupTime()
        self.volumeBlock = VolumeBlock(self.screen)
        self.musicPlayer.setVolume(self.volumeBlock.getVolume())

    # Method sets up buttons
    def setupButtons(self):
        self.buttonBlock = ButtonBlock(self.screen, self.directory, \
                                       self.mouse)

    # Method sets up Information Block
    def setupInformation(self):
        Title = self.songs.getTitle(self.currentSong)
        Path  = self.songs.getPath(self.currentSong)

        # Initialize Information Block
        self.informationBlock = InformationBlock(self.screen, Title, \
                                                 Path, self.fps)

    # Method sets up Directory Block
    def setupDirectory(self):
        Directory = self.songs.getDirectory()

        # Initialize Directory Block
        self.directoryBlock = DirectoryBlock(self.screen, Directory, \
                                             self.fps, self.mouse)

    # Method sets up Time Block
    def setupTime(self):
        Time = self.musicPlayer.getPosition()

        self.timeBlock = TimeBlock(self.screen, Time, self.fps)

    # Method handles a change in song
    def changeSong(self):
        title = self.songs.getTitle(self.currentSong)
        path  = self.songs.getPath(self.currentSong)
        self.informationBlock.setSongTitleAndPath(title, path)
        self.musicPlayer.setSongInformation(self.musicDirectory, path, title)
        self.musicPlayer.stop()
        self.musicPlayer.play()

    # Method runs app
    def runApp(self):
        run            = True
        sliderSelected = None
        sliderHovered  = False
        mouseDown      = False
        while run == True:
            self.screen.fill(Colour['BLACK'])
            self.mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():

                # Handle Quit event
                if event.type == pygame.QUIT:
                    self.saveFiles()
                    run = False

                # Handle mouse down events
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Handles volume slider
                    sliderSelected = self.volumeBlock.isInBounds(self.mouse[X], self.mouse[Y])
                    if sliderSelected:
                        mouseDown = True
                        self.volumeBlock.setDrawPercent(True)

                    # Handles Previous button
                    if self.buttonBlock.previousButton.obj.collidepoint(self.mouse):
                        good = False
                        while not good:
                            try:
                                self.buttonBlock.mouseDown("previous")
                                if (self.currentSong != 0):
                                    self.currentSong = self.currentSong - 1
                                    self.changeSong()
                                good = True
                            except:
                                good = False

                    # Handles Play button
                    elif self.buttonBlock.playButton.obj.collidepoint(self.mouse):
                        self.buttonBlock.mouseDown("play")
                        self.musicPlayer.play()

                    # handles Pause button
                    elif self.buttonBlock.pauseButton.obj.collidepoint(self.mouse):
                        self.buttonBlock.mouseDown("pause")
                        self.musicPlayer.pause()

                    # Handles Stop button
                    elif self.buttonBlock.stopButton.obj.collidepoint(self.mouse):
                        self.buttonBlock.mouseDown("stop")
                        self.musicPlayer.stop()
                        self.timeBlock.update(self.musicPlayer.getPosition())
                        
                    # Handles Next button
                    elif self.buttonBlock.nextButton.obj.collidepoint(self.mouse):
                        good = False
                        while not good:
                            try:
                                self.buttonBlock.mouseDown("next")
                                if (self.currentSong == self.songs.getSongCount() - 1):
                                    self.currentSong = 0
                                else:
                                    self.currentSong = self.currentSong + 1
                                self.changeSong()
                                good = True
                            except:
                                good = False
                                
                    # Handles changing directory
                    elif self.directoryBlock.directoryButton.obj.collidepoint(self.mouse):
                        good = False
                        while not good:
                            try:
                                self.songs.chooseDirectory()
                                self.musicDirectory = self.songs.getDirectory()
                                self.directoryBlock.mouseDown(self.musicDirectory)
                                self.currentSong = 0

                                title = self.songs.getTitle(self.currentSong)
                                path  = self.songs.getPath(self.currentSong)
                                self.informationBlock.setSongTitleAndPath(title, \
                                                                      path)
                                self.musicPlayer.setSongInformation(self.musicDirectory, \
                                                            path, title)
                                self.musicPlayer.stop()                        
                                self.musicPlayer.play()
                                good = True
                            except:
                                good = False

                # Handle mouse up events
                elif event.type == pygame.MOUSEBUTTONUP:
                    # Handles volume slider
                    mouseDown      = False
                    sliderSelected = None

                    # Handles mouse up on buttons
                    self.buttonBlock.mouseUp()
                    self.directoryBlock.mouseUp()

                # Handle Mouse Hover event for volume slider
                elif self.volumeBlock.isInBounds(self.mouse[X], self.mouse[Y]):
                    sliderHovered = True
                    self.volumeBlock.setDrawPercent(True)

                # Handle Mouse not Hover event for volume slider
                elif not self.volumeBlock.isInBounds(self.mouse[X], self.mouse[Y]):
                    sliderHovered = False

            # If slider is not hovered or selected, don't show percent
            if (not mouseDown and not sliderHovered and not sliderSelected):
                self.volumeBlock.setDrawPercent(False)

            # If slider is selected, allow mouse to move slider
            if sliderSelected:
                if (self.volumeBlock.isValid(self.mouse[X])):
                    self.volumeBlock.changeSlider(self.mouse[X])
                    self.musicPlayer.setVolume(self.volumeBlock.getVolume())

            self.volumeBlock.update()
            self.informationBlock.update()
            self.directoryBlock.update()
            self.timeBlock.update(self.musicPlayer.getPosition())
            self.buttonBlock.update()
            pygame.display.update()
            self.clock.tick(self.fps)
            
        # Clean exit
        pygame.quit()

    # Method reads in config file
    def configFile(self):
        fileObj = FileHandler("config")
        configArray = fileObj.read()
        tokenizer = StringTokenizer('\n')
        tokenizer.setString(configArray)
        
        # Directory
        token = tokenizer.getToken()
        index = token.index('=') + 1
        self.musicDirectory = token[index:]

        # Icon
        token = tokenizer.getToken()
        index = token.index('=') + 1
        self.iconPath = token[index:]

        # LastSong
        token = tokenizer.getToken()
        index = token.index('=') + 1
        self.currentSong = int(token[index:])

    # Method saves config file and song list
    def saveFiles(self):
        # Rewrite config file
        string = "Directory="    + self.musicDirectory + "\n" + \
                 "Icon="         + self.iconPath       + "\n" + \
                 "CurrentSong="  + str(self.currentSong)
        fileObj = FileHandler("config")
        fileObj.write(string, "")

        # Rewrite songs file
        fileObj = FileHandler("Songs")
        string = []
        for i in range(self.songs.getSongCount()):
            path = self.songs.getPath(i)
            title = self.songs.getTitle(i)
            string.append(path + "," + title)
        fileObj.write(string, "\n")
