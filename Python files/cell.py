import colors
import pygame
import utilities

side = 20

class Cell:

    def __init__(self, screen, row, col):
        self.color = colors.white
        self.row = row
        self.col = col
        self.screen = screen
        self.rect = pygame.draw.rect(
                                     screen, 
                                     colors.white, 
                                     pygame.Rect(
                                                 utilities.MatricealToCartesian((row, col)), 
                                                 (side - 1, side - 1)
                                                )
                                    )


    
    def changeColor(self, color):
        self.color = color
        self.rect = pygame.draw.rect(
                                     self.screen, 
                                     color, 
                                     pygame.Rect(
                                                 utilities.MatricealToCartesian((self.row, self.col)), 
                                                 (side - 1, side - 1)
                                                )
                                    )