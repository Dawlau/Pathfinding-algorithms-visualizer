import graphics
import pygame
import sys

def main():

    from homescreen import HomeScreen

    graphics.setup()
    graphics.initFonts()

    homescreen = HomeScreen()
    homescreen.play(graphics.screen)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]: # Quit
                pygame.quit()
                sys.exit()

        pygame.display.flip() # call it once to avoid flickering

main()