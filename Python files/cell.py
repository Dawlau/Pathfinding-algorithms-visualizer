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

    
    def addArrow(self, direction):

        import pathlib, utilities, pygame

        path = utilities.rootDir().joinpath("images")
        if direction == "left":
            path = path.joinpath("leftarrow.png")
        elif direction == "right":
            path = path.joinpath("rightarrow.png")
        elif direction == "up":
            path = path.joinpath("uparrow.png")
        else:
            path = path.joinpath("downarrow.png")

        path = str(path)
        image = pygame.image.load(path)
        self.screen.blit(image, utilities.MatricealToCartesian((self.row, self.col)))