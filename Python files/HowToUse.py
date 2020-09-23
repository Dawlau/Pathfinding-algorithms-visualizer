# this file implements the How to Use section

from tkinter import *
import tkinter.font as tkFont

fontFamily = "Arial"
fontSize = 15
backgroundColor = "black"
textColor = "white"
borderWidth = 10
minrootWidth = 300
minrootHeight = 300
startrootWidth = 600
startrootHeight = 600

class HowToUse:

    def __init__(self):

        self.root = Tk()
        self.root.title("How to use")
        self.root.geometry(str(startrootWidth) + "x" + str(startrootHeight))
        self.root.minsize(minrootWidth, minrootHeight)

        self.packText()

        self.root.mainloop()


    def packText(self):

        import utilities

        tkArial30 = tkFont.Font(family = fontFamily, size = fontSize)

        txt = Text(self.root, width = 16, height = 5, font = tkArial30, bg = backgroundColor, fg = textColor, bd = borderWidth)

        txt.pack(side = LEFT, fill = BOTH, expand = YES)

        yscrollbar = Scrollbar(self.root, orient = VERTICAL, command = txt.yview)
        yscrollbar.pack(side = RIGHT, fill = Y)
        txt["yscrollcommand"] = yscrollbar.set


        txt.insert(END, utilities.parseFile(utilities.fromRootFile("HowToUse.txt")))