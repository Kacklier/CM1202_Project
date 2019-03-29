from tkinter import *
from tkcalendar import DateEntry
from test_db_template import Test
import shelve
import datetime

number_questions = 0
dynamic_objects = []
answers = {}
questions = {}
answer_lst = []


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

    def init_window(self, master):
        master.title("Create a new test")
        master.minsize(506, 0)
        # the size is adjusted automatically to fit every element, however
        # it can be adjusted manutally with master.geometry() function
        # master.geometry("{}x{}".format("400", "300"))

    def init_title(self):
        lblTitle = Label(self, text="Enter test title:", font=("Calibri", 12, "bold"))
        lblTitle.grid(row=0, column=0, sticky=W)

        inpTitle = Entry(self, width=35, font=("Calibri", 12))
        inpTitle.grid(row=0, column=1, sticky=W, columnspan=3)

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

        calStart = DateEntry(self, width=10, borderwidth=2, locale="en_GB")
        calStart.grid(row=3, column=1, sticky=E)

        now = datetime.datetime.now()

        calEnd = DateEntry(self, width=10, borderwidth=2, locale="en_GB", month=(now.month + 1))
        calEnd.grid(row=3, column=2, sticky=E)

        chkCheck = Checkbutton(self, text="Do you want to use start and end dates?", font=("Calibri", 12))
        chkCheck.grid(row=4, column=1, sticky=E, columnspan=2)

    def init_questions(self):
        global dynamic_objects
        btnAdd = Button(self, text="Add a question", font=("Calibri", 12), width=16, height=1)
        dynamic_objects.append(btnAdd)
        btnAdd['command'] = self.add_question
        btnAdd.grid(row=(number_questions + 5), column=0, columnspan=3)
# dynamic_objects index:  0=btnAdd, 1=lblQues, 2=txtQues, 3=scrlQues, 4=btnAddAns, 5=btnCancel
# 6=

    def add_question(self):
        global number_questions
        dynamic_objects[0].destroy()
        dynamic_objects.remove(dynamic_objects[0])
        self.aText = []
        self.aChkbox = []
        btnFinishQ = Button(self, text="Finish Question", font=("Calibri", 12))
        btnFinishQ['command'] = self.finish_question
        btnFinishQ.grid(row=(number_questions + 4), column=0, sticky=NW)
        dynamic_objects.append(btnFinishQ)
        lblQues = Label(self, text="Enter the question here:", font=("Calibri", 12, "bold"))
        dynamic_objects.append(lblQues)
        lblQues.grid(row=(number_questions + 5), column=0, sticky=SW)
        txtQues = Text(self, font=("Calibri", 12), width=35, height=4)
        dynamic_objects.append(txtQues)
        scrlQues = Scrollbar(self, command=txtQues.yview)
        dynamic_objects.append(scrlQues)
        txtQues['yscrollcommand'] = scrlQues.set
        txtQues.grid(row=(number_questions + 5), column=1, columnspan=2, rowspan=2, sticky=W)
        scrlQues.grid(row=(number_questions + 5), column=3, columnspan=3, rowspan=2)
        self.add_question_buttons()

    def add_question_buttons(self):
        btnAddAns = Button(self, text="Add an answer", font=("Calibri", 12))
        btnAddAns['command'] = self.add_answer
        btnAddAns.grid(row=(number_questions + len(answers) + 7), column=0)
        btnCancel = Button(self, text="Cancel the question", font=("Calibri", 12))
        btnCancel['command'] = self.cancel_question
        btnCancel.grid(row=(number_questions + len(answers) + 7), column=1, columnspan=2)
        dynamic_objects.append(btnAddAns)
        dynamic_objects.append(btnCancel)

    def cancel_question(self):
        for i in range(len(dynamic_objects) - 1, -1, -1):
            dynamic_objects[i].destroy()
            dynamic_objects.remove(dynamic_objects[i])
        self.init_questions()

    def add_answer(self):
        global anwsers
        for i in range(len(dynamic_objects) - 1, len(dynamic_objects) - 3, -1):
            dynamic_objects[i].destroy()
            dynamic_objects.remove(dynamic_objects[i])
        answer = []
        answer.append(Label(self, text="Answer " + str(len(answers) + 1) + ":", font=("Calibri", 12, "bold")))
        answer[0].grid(row=(number_questions + len(answers) + 7), column=0, sticky=W)
        answer.append(Entry(self, width=25, font=("Calibri", 12)))
        answer[1].grid(row=(number_questions + len(answers) + 7), column=1, columnspan=2, sticky=W)
        answers[len(answers)] = answer
        answer.append(Checkbutton(self, text="Correct", font=("Calibri", 12)))
        answer[2].grid(row=(number_questions + len(answers) + 6), column=2)

        for a in answer:
            dynamic_objects.append(a)
        print(str(answer))
        self.add_question_buttons()


    def finish_question(self):
        pass
    def submit_test(self):
        global number_questions
        # db = shelve.open('tests\\tests')
        # test_count = len(db)
