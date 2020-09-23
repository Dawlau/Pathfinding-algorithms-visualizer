from cell import Cell

class StopCell(Cell):

    def __init__(self, screen, row, col):
        super().__init__(screen, row, col)

        import pathlib, utilities, pygame

        path = str(utilities.rootDir().joinpath("images").joinpath("target.png"))
        self.image = pygame.image.load(path)
        screen.blit(self.image, utilities.MatricealToCartesian((row, col)))


    def changeColor(self, color):

        import utilities

        super().changeColor(color)
        self.screen.blit(self.image, utilities.MatricealToCartesian((self.row, self.col)))
