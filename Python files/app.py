from cell import Cell, side
from constants import width, height
import graphics



class App:

    rows = height // side
    cols = width // side
    
    def __init__(self, screen):
        self.reset(screen)



    def reset(self, screen):
        import colors

        self.start = None
        self.stop = None
        self.state = 1
        self.openmessagebox = True
        self.MouseEvent = 0

        self.grid = [] * self.rows
        for row in range(self.rows):
            self.grid.append([None] * self.cols)

        screen.fill(colors.black)
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = Cell(graphics.screen, row, col)



    

    def runStage1(self, event):

        import pygame, utilities
        from colors import red

        if self.openmessagebox:
            graphics.okMessageBox("Choose start and stop cells.")
            self.openmessagebox = False
            

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


    
    def runStage2(self, event):

        import pygame, utilities
        from colors import black, red

        if self.openmessagebox:
            graphics.okMessageBox("Build walls\nPress spacebar when you are done")
            self.openmessagebox = False

        if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
            self.state = 3
            return

        elif event.type == pygame.MOUSEBUTTONDOWN and self.MouseEvent == 0:
            self.MouseEvent += 1
            
        elif event.type == pygame.MOUSEMOTION and self.MouseEvent == 1:
            clickCoords = event.pos

            row, col = utilities.CartesianToMatriceal(clickCoords)

            if self.grid[row][col].color is black or self.grid[row][col].color is red:
                return

            self.grid[row][col].changeColor(black)
        elif event.type == pygame.MOUSEBUTTONUP and self.MouseEvent == 1:
            self.MouseEvent = 0
            


    def runStage3(self):
        pass



    def runStage4(self):
        pass



    def run(self, screen):

        import pygame

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]: # Quit
                pygame.quit()
                sys.exit()

            if self.state == 1:
                self.runStage1(event)
            elif self.state == 2:
                self.runStage2(event)
            elif self.state == 3:
                self.runStage3()
            elif self.state == 4:
                self.runStage4()