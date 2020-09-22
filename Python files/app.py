import copy
from cell import Cell, side
from constants import width, height
import graphics
from tkinter import *
from tkinter import messagebox

class App:

    rows = height // side
    cols = width // side
    
    def __init__(self, screen):
        import utilities
        self.reset(screen)



    def reset(self, screen):
        import colors

        self.start = None
        self.stop = None
        self.state = 1
        self.openmessagebox = True

        self.grid = [] * self.rows
        for row in range(self.rows):
            self.grid.append([None] * self.cols)

        screen.fill(colors.black)
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = Cell(graphics.screen, row, col)


    def stage1MessageBox(self):

        self.openmessagebox = False

        root = Tk()
        root.geometry("300x50")
        root.title("")

        def end():
            root.destroy()

        w = Label(root, text="Choose start and stop cells.")
        b = Button(root, text = "Ok", command = end)
        w.pack()
        b.pack()

        root.mainloop()

    
    def runStage1(self, event):

        import pygame, utilities
        from colors import red

        if self.openmessagebox:
            self.stage1MessageBox()
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            clickCoords = pygame.mouse.get_pos()
            row, col = utilities.CartesianToMatriceal(clickCoords)

            if self.grid[row][col].color is red:
                return

            self.grid[row][col].changeColor(red)

            if self.start is None:
                self.start = (row, col)
            elif self.stop is None:
                self.stop = (row, col)
        
        if self.start is not None and self.stop is not None:
            self.state = 2
            self.openmessagebox = True


    def run(self, screen):

        import pygame

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]: # Quit
                pygame.quit()
                sys.exit()

            if self.state == 1:
                self.runStage1(event)
                

            elif self.state == 2:
                continue