#Author: Jamie
from tkinter import *
from tkinter import ttk
from resultworker import *


class view_summative(Frame):
    def __init__(self, master, previous):
        self.master = master
        self.studentnames = []
        self.studentresults = {}
        self.sortby = StringVar()
        self.sentmsg = StringVar()
        self.statusmsg = StringVar()
        self.generate_data("summative")
        self.init_window()
        self.color_lstbox()

    def init_window(self):
        self.sortType = {'summative': 'Summative Tests'}
        self.sortby = StringVar()
        self.sentmsg = StringVar()
        self.statusmsg = StringVar()
        c = ttk.Frame(self.master, padding=(5, 5, 12, 0))
        c.grid(column=0, row=0, sticky=NSEW)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        self.lbox = Listbox(c)
        self.lbox.insert("end", *self.studentnames)

        lbl = ttk.Label(c, text="Display students by assessment type:")
        g2 = ttk.Radiobutton(c, text=self.sortType['summative'], variable=self.sortby, value='summative')
        send = ttk.Button(c, text='Display Results', command=self.displayRes, default='active')
        sentlbl = ttk.Label(c, textvariable=self.sentmsg, anchor='center')
        status = ttk.Label(c, textvariable=self.statusmsg, anchor=W)

        # Grid all the widgets
        self.lbox.grid(column=0, row=0, rowspan=6, sticky=NSEW)
        lbl.grid(column=1, row=0, padx=10, pady=5)
        g2.grid(column=1, row=2, sticky=W, padx=20)
        send.grid(column=2, row=4, sticky=E)
        sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
        status.grid(column=0, row=6, columnspan=2, sticky=EW)
        c.grid_columnconfigure(0, weight=1)
        c.grid_rowconfigure(5, weight=1)

        self.lbox.bind('<<ListboxSelect>>', self.showData)
        self.lbox.bind('<Double-1>', self.displayRes)
        self.master.bind('<Return>', self.displayRes)

    def generate_data(self, test_type):
        tests = GetTests(test_type)
        students = []
        for test in tests:
            x = get_students_results(test[0], test[1])
            if len(x) > 0:
                students.append(get_students_results(test[0], test[1]))
            else:
                continue

        for student in students:
            for x in student:
                if len(x[0]) > 0:
                    self.studentnames.append(x[0])
                    self.studentresults[x[0]] = x[1]

    def showData(self, *args):
        idxs = self.lbox.curselection()
        if len(idxs) == 1:
            idx = int(idxs[0])
            student_name = self.studentnames[idx]
            student_result = self.studentresults[student_name]
            self.statusmsg.set(f"The result of student {student_name} is {student_result}%")
        self.sentmsg.set('')

    def displayRes(self, *args):
        self.studentnames = []
        self.studentresults = {}
        idxs = self.lbox.curselection()
        if len(idxs) == 1:
            idx = int(idxs[0])
            self.lbox.see(idx)
            # to_check = self.sortType[self.sortby.get()].replace(" ", "").lower()
            self.sentmsg.set("Displayed students for %s" % (self.sortType[self.sortby.get()]))

    def color_lstbox(self):
        # Colorize alternating lines of the listbox
        for i in range(0, len(self.studentnames), 2):
            self.lbox.itemconfigure(i, background='#f0f0ff')

        self.sortby.set('summative')
        self.sentmsg.set('')
        self.statusmsg.set('')
        self.lbox.selection_set(0)
        self.showData()
