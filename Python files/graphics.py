def setup():

    import pygame, colors, constants

    global screen

    pygame.init()
    screen = pygame.display.set_mode((constants.width, constants.height))
    screen.fill(colors.white)
    pygame.display.set_caption("Path finding algorithms")

    pygame.display.set_icon(pygame.image.load("../images/icon.png"))

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

    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x60")
    root.title("")


    label = tk.Label(root, text = text)
    label.pack()

    def end():
        root.destroy()

    button = tk.Button(root, text = "Ok", command = end)
    button.pack()

    root.mainloop()


def endMessageBox():

    import tkinter as tk
    from functools import partial

    root = tk.Tk()
    root.geometry("300x60")
    root.title("Done")

    label = tk.Label(root, text = "Done")
    label.pack()


    message = [None]

    def quit(message):

        message[0] = "Quit"
        root.destroy()

    def restart(message):

        message[0] = "Restart"
        root.destroy()

    buttonQuit = tk.Button(root, text = "Quit", command = partial(quit, message))
    buttonQuit.pack()

    buttonRestart = tk.Button(root, text = "Restart", command = partial(restart, message))
    buttonRestart.pack()

    root.mainloop()

    return message[0]