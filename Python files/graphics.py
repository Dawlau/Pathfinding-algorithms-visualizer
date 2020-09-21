def setup():

    import pygame, colors, constants

    global screen

    pygame.init()
    screen = pygame.display.set_mode((constants.width, constants.height))
    screen.fill(colors.white)
    pygame.display.set_caption("Path finding algorithms")

    pygame.display.set_icon(pygame.image.load("images/icon.png"))

    pygame.display.flip()


def initFonts():

    import pygame

    pygame.font.init()

    global CMMS30

    CMMS30 = pygame.font.SysFont("Comic Sans MS", 30)

def createText(screen, font, text, color, position):
    renderText = font.render(text, True, color)
    Rect = screen.blit(renderText, position)

    return Rect