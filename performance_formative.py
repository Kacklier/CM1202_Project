from tkinter import *
import csv


class performance_formative(Frame):
    def __init__(self, master, previous):
        Frame.__init__(self, master)
        self.previous = previous
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("Performance in Formative Tests")
        # self.master.minsize(500, 200)
        self.master.resizable(width=False, height=False)

        self.txtDisplay = Text(self, height=25, width=90)
        self.txtDisplay.tag_configure("boldfont", font=('MS', 8, 'bold'))
        self.txtDisplay.tag_configure("normfont", font=('MS', 8))
        self.txtDisplay.grid(row=0, column=0)

        tabResults = ""
        tabResults += ("\t" + "\t" + "\t" + "\t" + "\t")

        self.txtDisplay.insert(END, tabResults + "% of")
