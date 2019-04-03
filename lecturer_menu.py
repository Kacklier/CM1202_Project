from tkinter import *
from create_test import create_test
from performance import performance


class lecturer_menu(Frame):
    def __init__(self, master, previous):
        Frame.__init__(self, master)
        self.previous = previous
        self.grid()
        self.init_window()
        self.init_buttons()

    def init_window(self):
        self.master.title("Lecturer Menu")
        self.master.minsize(500, 200)
        self.master.resizable(width=False, height=False)

    def init_buttons(self):
        btnCreate = Button(self, text="Create an assessment", wraplength=90, font=("Calibri", 14), width=20, height=3)
        btnCreate['command'] = self.open_creation
        btnCreate.grid(row=0, column=0, padx=15, pady=40)
        btnPerf = Button(self, text="View Performance", wraplength=100, font=("Calibri", 14), width=20, height=3)
        btnPerf['command'] = self.open_performance
        btnPerf.grid(row=0, column=1)
        btnModify = Button(self, text="Modify an assessment", wraplength=90, font=("Calibri", 14), width=20, height=3)
        btnModify['command'] = self.open_modify
        btnModify.grid(row=0, column=2, padx=15)
        btnBack = Button(self, text="Go back to login", wraplength=70, font=("Calibri", 14), width=15, height=2)
        btnBack['command'] = self.open_login
        btnBack.grid(row=1, column=1, pady=40)

    def open_creation(self):
        t2 = Toplevel(self.master)
        self.master.withdraw()
        create_test(t2, self.master)
        t2.wm_protocol("WM_DELETE_WINDOW", self.previous.destroy)

    def open_performance(self):
        t2 = Toplevel(self.master)
        self.master.withdraw()
        performance(t2, self.master, self.previous)
        t2.wm_protocol("WM_DELETE_WINDOW", self.previous.destroy)

    def open_modify(self):
        pass
        # NJABULO
        # t2 = Toplevel(self.master)
        # self.master.withdraw()
        # [NAME](t2)
        # t2.wm_protocol("WM_DELETE_WINDOW", self.previous.destroy)

    def open_login(self):
        self.master.destroy()
        self.previous.deiconify()
