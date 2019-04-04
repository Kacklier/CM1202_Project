from tkinter import *
import csv


class performance_formative(Frame):
    def __init__(self, master, previous):
        Frame.__init__(self, master)
        self.results = []
        self.tests = []
        self.previous = previous
        self.grid()
        self.get_data()
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

        for lst in self.resreader:
            if not lst[0] == "TEST":
                if lst[0] == "TITLE":
                    self.results.append([])
                self.results[len(self.results) - 1].append(lst)
        for lst in self.results:
            if lst[2][1] == "summative":
                self.results.remove(lst)
        for lst in self.testreader:
            if lst[0] == "TEST":
                self.tests.append([])
            self.tests[len(self.tests) - 1].append(lst)
        for lst in self.tests:
            if lst[2][1] == "summative":
                self.tests.remove(lst)

        print(self.results)
        print(self.tests)

    def get_data(self):
        with open("tests\\results.csv", 'r+', newline='') as csvFile:
            self.resreader = list(csv.reader(csvFile))
        with open("tests\\tests.csv", 'r+', newline='') as csvFile:
            self.testreader = list(csv.reader(csvFile))

    def go_back(self):
        self.master.destroy()
        self.previous.deiconify()
