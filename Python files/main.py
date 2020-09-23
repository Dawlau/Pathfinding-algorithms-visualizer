#! /usr/bin/python3

import graphics
import pygame
import sys



def main():


    from homescreen import HomeScreen
    from app import App

    graphics.setup()
    graphics.initFonts()

    homescreen = HomeScreen()
    homescreen.play(graphics.screen)


    app = App(graphics.screen)
    while True:
        app.run(graphics.screen)
        pygame.display.flip() # call it once to avoid flickering

main()