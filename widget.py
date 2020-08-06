import pygame

# Colors
white = (255, 255, 255)
green = (0, 128, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

# Button Class for the user input options
class Button(object):
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def changeColor(self):
        self.color = red

    def revertBetColor(self):
        self.color = white

    def revertColor(self):
        self.color = black

    def draw(self, win, outline=None):
        """
        Draw the button onto the window
        :param win: The pygame display window
        :param outline: Draw additional rectangle border if True
        :return: None
        """
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, black)
            win.blit(text, (self.x + (self.width // 2 - text.get_width() // 2), self.y + (self.height // 2 - text.get_height() // 2)))

    def isOver(self, pos):
        """
        Control the button click functionality
        :param pos: the (x, y) tuple location for the mouse
        :return: True if mouse cursor is within the button's location
        """
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
