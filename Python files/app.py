from cell import Cell, side
from constants import width, height
import graphics



class App:

    rows = height // side
    cols = width // side
    
    def __init__(self, screen):
        self.reset(screen)



    def reset(self, screen):
        import colors, pygame

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

        pygame.display.flip() # call it once to avoid flickering


    

    def runStage1(self, screen, event):

        import pygame, utilities
        from startCell import StartCell
        from stopCell import StopCell
        from colors import red

        if self.openmessagebox:
            graphics.okMessageBox("Choose start and stop cells.")
            self.openmessagebox = False
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            clickCoords = pygame.mouse.get_pos()
            row, col = utilities.CartesianToMatriceal(clickCoords)

            if self.grid[row][col].color == red:
                return

            self.grid[row][col].changeColor(red)

            if self.start is None:
                self.start = (row, col)
                self.grid[row][col] = StartCell(screen, row, col)
            elif self.stop is None:
                self.stop = (row, col)
                self.grid[row][col] = StopCell(screen, row, col)
        
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
            self.openmessagebox = True
            return

        elif event.type == pygame.MOUSEBUTTONDOWN and self.MouseEvent == 0:
            self.MouseEvent += 1
            
        elif event.type == pygame.MOUSEMOTION and self.MouseEvent == 1:
            clickCoords = event.pos

            row, col = utilities.CartesianToMatriceal(clickCoords)

            if self.grid[row][col].color == black or (row, col) == self.start or (row, col) == self.stop:
                return

            self.grid[row][col].changeColor(black)
        elif event.type == pygame.MOUSEBUTTONUP and self.MouseEvent == 1:
            self.MouseEvent = 0
            




    def runStage3(self):

        import algorithms

        if self.openmessagebox:
            algorithm, showSteps = graphics.chooseAlgoWindow()
            self.openmessagebox = False

        status = None

        if algorithm == "Bfs":
            status = algorithms.Bfs(self.grid, self.start, self.stop, showSteps)
        elif algorithm == "Dfs":
            status = algorithms.Dfs(self.grid, self.start, self.stop, showSteps)
        elif algorithm == "A*":
            status = algorithms.Astar(self.grid, self.start, self.stop, showSteps)
        elif algorithm == "Greedy Best-First Search":
            status = algorithms.GreedyBestfs(self.grid, self.start, self.stop, showSteps)

        if status == 0: # no path
            graphics.okMessageBox("There is no path")
        else:
            graphics.okMessageBox("Path found!")

        self.state = 4
        self.openmessagebox = True



    def runStage4(self, screen):

        import pygame, sys

        message = graphics.endMessageBox()

        if message == "Quit":
            pygame.quit()
            sys.exit()
        elif message == "Restart":
            self.reset(screen)



    def run(self, screen):

        import pygame, sys

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]: # Quit
                pygame.quit()
                sys.exit()

            if self.state == 1:
                self.runStage1(screen, event)
            elif self.state == 2:
                self.runStage2(event)
            elif self.state == 3:
                self.runStage3()
            elif self.state == 4:
                self.runStage4(screen)