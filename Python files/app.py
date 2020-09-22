import copy
from cell import Cell, side
from constants import width, height
import graphics

class App:

    def __init__(self):
        pass

    def run(self, screen):
        import colors
        screen.fill(colors.black)
        for row in range(width // side):
            for col in range(height // side):
                cell = Cell(graphics.screen, row, col)

        