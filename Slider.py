import pygame
import math
from Structures import *

class Slider(object):
    def __init__(self, screen, x, y, width, position, \
                 color, lowcolor, highcolor):
        self.screen            = screen
        self.x                 = x
        self.y                 = y
        self.width             = width
        self.percent           = position
        self.currentPosition   = int(width * (position / 100)) + x
        self.sliderColor       = color
        self.lowBarColor       = lowcolor
        self.highBarColor      = highcolor
        self.drawPercent       = False
        
        self.font = pygame.font.SysFont("Helvetica", 14)

    def getPercent(self):
        return self.percent

    def setDrawPercent(self, value):
        self.drawPercent = value

    def drawLowBar(self):
        if (self.currentPosition == self.width + self.x):
            coords = (self.x, self.y, self.currentPosition - self.x, 5)
        elif (self.currentPosition < self.width + self.x):
            coords = (self.x, self.y, self.width, 5)
        
        self.lowRect = pygame.draw.rect(self.screen, \
                                        self.lowBarColor, \
                                        coords)

    def drawHighBar(self):
        if (self.currentPosition < self.width + self.x):
            coords = (self.currentPosition , self.y, \
                      self.width - self.currentPosition + self.x, 5)
            self.lowRect = pygame.draw.rect(self.screen, \
                                            self.highBarColor, \
                                            coords)

    def indicatorPosition(self):
        position = 0
        if (self.percent <= 9):
            position = (self.currentPosition - 4, self.y - 20)
        elif (self.percent <= 99):
            position = (self.currentPosition - 8, self.y - 20)
        else:
            position = (self.currentPosition - 12, self.y - 20)
        return position

    def drawSlider(self):
        coords = (self.currentPosition, self.y + 3)
        self.sliderCircle = pygame.draw.circle(self.screen, \
                                               self.sliderColor, \
                                               coords, 8)

        if (self.drawPercent):
            self.sliderPercent = self.font.render(str(self.percent), \
                                                True, \
                                                Colour['LIGHTBLUE'])
            self.screen.blit(self.sliderPercent, self.indicatorPosition())
                                                

    def changeSlider(self, position):
        self.currentPosition = position
        self.percent = int((position - self.x) / self.width*100)

    def isInBounds(self, mouseX, mouseY):
        if math.hypot(self.currentPosition - mouseX, \
                      self.y + 3 - mouseY) <= 8:
            return self
        return None

    def isValid(self, mouseX):
        if (mouseX < self.x or mouseX > self.width + self.x):
            return False
        return True

    def update(self):
        self.drawLowBar()
        self.drawHighBar()
        self.drawSlider()

def main():
    pygame.init()
    pygame.font.init()

    # Screen attributes
    screen = pygame.display.set_mode((280,46))
    pygame.display.set_caption("Slider Class")
    clock = pygame.time.Clock()      # For frames per second
    mouse = pygame.mouse.get_pos()   # For mouse position

    # Slider attributes
    x            = 20
    y            = 20
    width        = 240
    position     = 50   # Percentage
    sliderColor  = Colour['BLUE']
    lowBarColor  = Colour['LIGHTBLUE']
    highBarColor = Colour['LIGHTGRAY']

    # Initialize Slider
    slider = Slider(screen, x, y, width, position, \
                    sliderColor, lowBarColor, highBarColor)

    # Run app
    run = True
    sliderSelected = None
    sliderHovered  = False
    mouseDown      = False
    while run:
        screen.fill(Colour['BLACK'])
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Handle Quit event
            if event.type == pygame.QUIT:
                run = False
                break

            # Handle Mouse Down event
            elif event.type == pygame.MOUSEBUTTONDOWN:                
                sliderSelected = slider.isInBounds(mouse[X], mouse[Y])
                if sliderSelected:
                    mouseDown = True
                    slider.setDrawPercent(True)

            # Handle Mouse Up event
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseDown      = False
                sliderSelected = None

            # Handle Mouse Hover event
            elif slider.isInBounds(mouse[X], mouse[Y]):
                sliderHovered = True
                slider.setDrawPercent(True)

            # Handle Mouse not Hover event
            elif not slider.isInBounds(mouse[X], mouse[Y]):
                sliderHovered = False

        # If slider is not hovered or selected, don't show percent
        if (not mouseDown and not sliderHovered and not sliderSelected):
            slider.setDrawPercent(False)

        # If slider is selected, allow mouse to move slider
        if sliderSelected:
            if (slider.isValid(mouse[X])):
                slider.changeSlider(mouse[X])

        #### GRAY RECTANGLE ####
##        coords = (10, 10, 285, 26)
##        pygame.draw.rect(screen, Colour['GRAY'], coords)
        #### GRAY RECTANGLE ####
        
        slider.update()
        pygame.display.update()
        clock.tick(60)

    # Quit app
    pygame.quit()

# Begin app
if __name__ == '__main__':
    main()
