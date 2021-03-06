#Author: Jamie
from tkinter import *
from statisticsNew import *
from view_summative import view_summative


class performance(Frame):
    def __init__(self, master, previous, root):
        Frame.__init__(self, master)
        self.root = root
        self.previous = previous
        self.grid()
        self.init_window()
        self.init_buttons()

    def init_window(self):
        self.master.title("Lecturer Menu")
        self.master.minsize(500, 200)
        self.master.resizable(width=False, height=False)

    def init_buttons(self):
        btnForm = Button(self, text="View Performance on Formative Assessments", wraplength=100, font=("Calibri", 14), width=30, height=5)
        btnForm['command'] = self.open_performance_formative
        btnForm.grid(row=0, column=0, padx=15, pady=40)
        btnSumm = Button(self, text="View Performance on Summative Assessments", wraplength=100, font=("Calibri", 14), width=30, height=5)
        btnSumm['command'] = self.open_performance_summative
        btnSumm.grid(row=0, column=1)
        btnBack = btnForm = Button(self, text="Go Back", font=("Calibri", 14), width=15, height=2)
        btnBack['command'] = self.go_back
        btnBack.grid(row=1, column=0, columnspan=2)


    def open_performance_formative(self):
        # t2 = Toplevel(self.master)
        # self.master.withdraw()
        # performance_formative(t2, self.master)
        # t2.wm_protocol("WM_DELETE_WINDOW", self.root.destroy)
        openS()

    def open_performance_summative(self):
        t2 = Toplevel(self.master)
        self.master.withdraw()
        view_summative(t2, self.master)
        t2.wm_protocol("WM_DELETE_WINDOW", self.root.destroy)

    def go_back(self):
        self.master.destroy()
        self.previous.deiconify()
