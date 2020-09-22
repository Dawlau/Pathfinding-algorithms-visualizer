import colors
import pygame
import utilities

side = 20

class Cell:

    def __init__(self, screen, row, col):
        self.color = colors.white
        self.row = row
        self.col = col
        self.rect = pygame.draw.rect(
                                     screen, 
                                     colors.white, 
                                     pygame.Rect(
                                                 utilities.MatricealToCartesian((row, col)), 
                                                 (side - 1, side - 1)
                                                )
                                    )