#Author: Wojtek
from tkinter import *
from tkcalendar import DateEntry
import csv
import datetime

number_questions = 0


class create_test(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.init_window(master)
        self.init_title()
        self.init_type_select()
        self.init_test_duration()
        self.init_dates()
        self.init_questions()
        self.init_buttons()

    def init_window(self, master):
        master.title("Create a new test")
        master.minsize(506, 0)
        # the size is adjusted automatically to fit every element, however
        # it can be adjusted manutally with master.geometry() function
        # master.geometry("{}x{}".format("400", "300"))

    def init_title(self):
        lblTitle = Label(self, text="Enter test title:", font=("Calibri", 12, "bold"))
        lblTitle.grid(row=0, column=0, sticky=W)

        self.inpTitle = Entry(self, width=35, font=("Calibri", 12))
        self.inpTitle.grid(row=0, column=1, sticky=W, columnspan=3)

    def init_type_select(self):
        lblType = Label(self, text="Select type of test:", font=("Calibri", 12, "bold"))
        lblType.grid(row=1, column=0, sticky=W)

        self.varType = StringVar()

        rbtType1 = Radiobutton(self, text="Summative", font=("Calibri", 12), variable=self.varType, value="summative")
        rbtType1.grid(row=1, column=1, sticky=W)

        rbtType2 = Radiobutton(self, text="Formative", font=("Calibri", 12), variable=self.varType, value="formative")
        rbtType2.grid(row=1, column=2, sticky=W)
        self.varType.set("summative")

    def init_test_duration(self):
        lblDuration1 = Label(self, text="Select test duration:", font=("Calibri", 12, "bold"))
        lblDuration1.grid(row=2, column=0, sticky=W)

        lblDuration2 = Label(self, text="minutes", font=("Calibri", 12))
        lblDuration2.grid(row=2, column=2, sticky=W)

        self.varDuration = IntVar()

        durations = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
        self.varDuration.set(60)
        drpDuration = OptionMenu(self, self.varDuration, *durations)
        drpDuration.grid(row=2, column=1, sticky=E)

    def init_dates(self):
        lblDate1 = Label(self, text="Choose start and end dates:", font=("Calibri", 12, "bold"))
        lblDate1.grid(row=3, column=0, sticky=W)

        self.calStart = DateEntry(self, width=10, borderwidth=2, locale="en_GB")
        self.calStart.grid(row=3, column=1, sticky=E)

        now = datetime.datetime.now()

        self.calEnd = DateEntry(self, width=10, borderwidth=2, locale="en_GB", month=(now.month + 1))
        self.calEnd.grid(row=3, column=2, sticky=E)

        self.varDates = IntVar()
        chkDates = Checkbutton(self, text="Do you want to use start and end dates?", variable=self.varDates, font=("Calibri", 12))
        chkDates.grid(row=4, column=1, sticky=E, columnspan=2)

    def init_questions(self):
        lblQ1 = Label(self, text="Question 1:", font=("Calibri", 12, "bold"))
        lblQ1.grid(row=5, column=0, sticky=W)

        self.txtQ1 = Text(self, font=("Calibri", 12), height=4, width=35)
        self.txtQ1.grid(row=5, column=1, columnspan=2)

        self.scrQ1 = Scrollbar(self, command=self.txtQ1.yview)
        self.txtQ1['yscrollcommand'] = self.scrQ1.set

        self.scrQ1.grid(row=5, column=3)

        lblAnswers1 = Label(self, font=("Calibri", 12, "bold"), text="Answers:")
        lblAnswers1.grid(row=6, column=0, sticky=W)

        self.varA1 = IntVar()
        self.varA1.set(1)
        lblAnswers11 = Label(self, font=("Calibri", 12, "bold"), text="1")
        lblAnswers11.grid(row=6, column=0, sticky=E)
        self.txtA11 = Entry(self, width=35, font=("Calibri", 12))
        self.txtA11.grid(row=6, column=1, columnspan=2)
        rdoA11 = Radiobutton(self, text="Correct answer", variable=self.varA1, value=1)
        rdoA11.grid(row=7, column=1, columnspan=2)

        lblAnswers12 = Label(self, font=("Calibri", 12, "bold"), text="2")
        lblAnswers12.grid(row=8, column=0, sticky=E)
        self.txtA12 = Entry(self, width=35, font=("Calibri", 12))
        self.txtA12.grid(row=8, column=1, columnspan=2)
        rdoA12 = Radiobutton(self, text="Correct answer", variable=self.varA1, value=2)
        rdoA12.grid(row=9, column=1, columnspan=2)

        lblAnswers13 = Label(self, font=("Calibri", 12, "bold"), text="3")
        lblAnswers13.grid(row=10, column=0, sticky=E)
        self.txtA13 = Entry(self, width=35, font=("Calibri", 12))
        self.txtA13.grid(row=10, column=1, columnspan=2)
        rdoA13 = Radiobutton(self, text="Correct answer", variable=self.varA1, value=3)
        rdoA13.grid(row=11, column=1, columnspan=2)

        lblAnswers14 = Label(self, font=("Calibri", 12, "bold"), text="4")
        lblAnswers14.grid(row=12, column=0, sticky=E)
        self.txtA14 = Entry(self, width=35, font=("Calibri", 12))
        self.txtA14.grid(row=12, column=1, columnspan=2)
        rdoA14 = Radiobutton(self, text="Correct answer", variable=self.varA1, value=4)
        rdoA14.grid(row=13, column=1, columnspan=2)


        lblQ2 = Label(self, text="Question 2:", font=("Calibri", 12, "bold"))
        lblQ2.grid(row=14, column=0, sticky=W)

        self.txtQ2 = Text(self, font=("Calibri", 12), height=4, width=35)
        self.txtQ2.grid(row=14, column=1, columnspan=2)

        self.scrQ2 = Scrollbar(self, command=self.txtQ2.yview)
        self.txtQ2['yscrollcommand'] = self.scrQ2.set

        self.scrQ2.grid(row=14, column=3)

        lblAnswers2 = Label(self, font=("Calibri", 12, "bold"), text="Answers:")
        lblAnswers2.grid(row=15, column=0, sticky=W)

        self.varA2 = IntVar()
        self.varA2.set(1)
        lblAnswers21 = Label(self, font=("Calibri", 12, "bold"), text="1")
        lblAnswers21.grid(row=15, column=0, sticky=E)
        self.txtA21 = Entry(self, width=35, font=("Calibri", 12))
        self.txtA21.grid(row=15, column=1, columnspan=2)
        rdoA21 = Radiobutton(self, text="Correct answer", variable=self.varA2, value=1)
        rdoA21.grid(row=16, column=1, columnspan=2)

        lblAnswers22 = Label(self, font=("Calibri", 12, "bold"), text="2")
        lblAnswers22.grid(row=17, column=0, sticky=E)
        self.txtA22 = Entry(self, width=35, font=("Calibri", 12))
        self.txtA22.grid(row=17, column=1, columnspan=2)
        rdoA22 = Radiobutton(self, text="Correct answer", variable=self.varA2, value=2)
        rdoA22.grid(row=18, column=1, columnspan=2)

        lblAnswers23 = Label(self, font=("Calibri", 12, "bold"), text="3")
        lblAnswers23.grid(row=19, column=0, sticky=E)
        self.txtA23 = Entry(self, width=35, font=("Calibri", 12))
        self.txtA23.grid(row=19, column=1, columnspan=2)
        rdoA23 = Radiobutton(self, text="Correct answer", variable=self.varA2, value=3)
        rdoA23.grid(row=20, column=1, columnspan=2)

        lblAnswers24 = Label(self, font=("Calibri", 12, "bold"), text="4")
        lblAnswers24.grid(row=21, column=0, sticky=E)
        self.txtA24 = Entry(self, width=35, font=("Calibri", 12))
        self.txtA24.grid(row=21, column=1, columnspan=2)
        rdoA24 = Radiobutton(self, text="Correct answer", variable=self.varA2, value=4)
        rdoA24.grid(row=22, column=1, columnspan=2)

    def init_buttons(self):
        btnSubmit = Button(self, text="Submit", font=("Calibri", 12,), width=20, command=self.submit_test)
        btnSubmit.grid(row=23, column=0, columnspan=3)

    def submit_test(self):
        with open('tests\\tests.csv', 'r+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            reader = csv.reader(csvFile)
            counter = 1
            for line in reader:
                if line[0] == "TEST":
                    counter += 1
            writer.writerow(["TEST", counter])
            writer.writerow(["TYPE", self.varType.get()])
            writer.writerow(["DURATION", self.varDuration.get()])
            writer.writerow(["DATES", self.calStart.get(), self.calEnd.get()])
            writer.writerow(["USE_DATES", self.varDates.get()])
            writer.writerow(["QUESTION_NO", 1])
            writer.writerow(["QUESTION", self.txtQ1.get("1.0", "end-1c")])
            answers1 = ["ANSWER_1", "ANSWER_2", "ANSWER_3", "ANSWER_4"]
            answers2 = [self.txtA11.get(), self.txtA12.get(), self.txtA13.get(), self.txtA14.get(),
                        self.txtA21.get(), self.txtA22.get(), self.txtA23.get(), self.txtA24.get()]
            counter = 0
            for i in answers1:
                if str(self.varA1.get()) in i:
                    writer.writerow([i, answers2[counter], 1])
                else:
                    writer.writerow([i, answers2[counter], 0])
                counter += 1
            writer.writerow(["QUESTION_NO", 2])
            writer.writerow(["QUESTION", self.txtQ2.get("1.0", "end-1c")])
            for i in answers1:
                if str(self.varA2.get()) in i:
                    writer.writerow([i, answers2[counter], 1])
                else:
                    writer.writerow([i, answers2[counter], 0])
