from tkinter import *


def setup():

    import pygame, colors, constants, utilities, pathlib

    global screen

    pygame.init()
    screen = pygame.display.set_mode((constants.width, constants.height))
    screen.fill(colors.white)
    pygame.display.set_caption("Path finding algorithms")
    pygame.display.set_icon(pygame.image.load(str(utilities.rootDir().joinpath("images").joinpath("icon.png"))))

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



def okMessageBox(text):

    root = Tk()
    root.geometry("300x60")
    root.title("")


    label = Label(root, text = text)
    label.pack()

    def end():
        root.destroy()

    button = Button(root, text = "Ok", command = end)
    button.pack()

    root.mainloop()


def endMessageBox():

    from functools import partial

    root = Tk()
    root.geometry("300x60")
    root.title("Done")


    message = [None]

    def quit(message):

        message[0] = "Quit"
        root.destroy()

    def restart(message):

        message[0] = "Restart"
        root.destroy()

    buttonQuit = Button(root, text = "Quit", command = partial(quit, message))
    buttonQuit.pack()

    buttonRestart = Button(root, text = "Restart", command = partial(restart, message))
    buttonRestart.pack()

    root.mainloop()

    return message[0]



def chooseAlgoWindow():

    import utilities
    
    # Add a grid
    root = Tk()
    root.title("")
    frame = Frame(root)
    frame.pack(padx = 100)

    option = StringVar(frame)

    # Dictionary with options

    choices = utilities.parseFile(utilities.fromRootFile("algorithms.txt")).split("\n") # create list of algorithms from algorithms.txt
    option.set(choices[0]) # set the default option

    popupMenu = OptionMenu(frame, option, *choices)
    Label(frame, text = "Choose an algorithm").grid(row = 0, column = 0)
    popupMenu.grid(row = 1, column = 0)

    showSteps = BooleanVar()
    Checkbutton(frame, text = "Show steps", variable = showSteps).grid(row=3)

    def quit():
        frame.destroy()
        root.destroy()

    Button(frame, text = "Done", command = quit).grid(row = 4)

    frame.mainloop()

    return option.get(), showSteps.get()
