from tkinter import *
import csv


class performance_formative(Frame):
    def __init__(self, master, previous):
        Frame.__init__(self, master)
        self.tests = []
        self.previous = previous
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("Performance in Formative Tests")
        # self.master.minsize(500, 200)
        self.master.resizable(width=False, height=False)

        btnBack = Button(self, text="Back", font=('Calibri', 14), command=self.go_back)
        self.txtDisplay = Text(self, height=25, width=95)
        self.txtDisplay.tag_configure("boldfont", font=('MS', 8, 'bold'))
        self.txtDisplay.tag_configure("normfont", font=('MS', 8))
        self.txtDisplay.grid(row=0, column=0)
        btnBack.grid(row=1, column=0)

        self.txtDisplay.insert(END, "\t\t\t% of times answered correctly" + "\t\t\tQuestion most often answered incorrectly" + "\t\t\tNumber of attempts", 'boldfont')
        with open("tests\\tests.csv", 'r+', newline='') as csvFile:
            reader = list(csv.reader(csvFile))
            print(reader)
            for lst in reader:
                flag = 0
                if lst[0] == "TITLE":
                    for d in self.tests:
                        if lst[1] == d["TITLE"]:
                            flag = 1

    def go_back(self):
        self.master.destroy()
        self.previous.deiconify()
