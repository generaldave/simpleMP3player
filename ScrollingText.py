import pygame   # For GUI

class ScrollingText(object):
    def __init__(self, surface, text, fontSize, x, y, \
                 areaCoord, fps, color, seconds):
        self.counter = 1
        pygame.font.init()
        self.font = pygame.font.SysFont("Helvetica", fontSize)
        
        self.surface = surface
        self.text = text
        self.x = x
        self.y = y
        self.color = color

        self.seconds = seconds

        self.areaCoord = areaCoord
        self.position = 0

        self.fps = fps

        self.scrollingText = self.font.render(self.text, True,
                                              self.color)
        self.surface.blit(self.scrollingText, (self.x, self.y))
        
    def update(self):
        x = self.position
        y = self.areaCoord[1]
        width = self.areaCoord[2]
        height = self.areaCoord[3]
        self.surface.blit(self.scrollingText, \
                              (self.x, self.y), \
                              (x, y, width, height))

        # Only scroll if text is wider than box
        if self.scrollingText.get_width() > width:
            # Delay scroll by given number of seconds
            if self.counter < self.fps * self.seconds:
                self.counter = self.counter + 1
            else:            
                if self.position < self.scrollingText.get_width():
                    self.position = self.position + 1
                else:
                    self.position = 0
                    self.counter = 1
