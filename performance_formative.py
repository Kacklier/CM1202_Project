from tkinter import *
import csv


class lecturer_menu(Frame):
    def __init__(self, master, previous):
        Frame.__init__(self, master)
        self.previous = previous
        self.grid()
