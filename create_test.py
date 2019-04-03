#Author: Wojtek
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import csv
import datetime


class create_test(Frame):
    def __init__(self, master, previous):
        Frame.__init__(self, master)
        self.number_questions = 0
        self.number_answers = 0
        self.dynamic_objects = []
        self.questions = {}
        self.answers = []
        self.previous = previous
        self.grid()
        self.init_window()
        self.init_title()
        self.init_type_select()
        self.init_test_duration()
        self.init_dates()
        self.init_buttons()

    def init_window(self):
        self.master.title("Create a new test")
        self.master.minsize(506, 0)
        self.master.resizable(width=False, height=False)

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
        rbtType2.grid(row=1, column=2, sticky=W, padx=10)
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
        chkCheck = Checkbutton(self, text="Do you want to use start and end dates?", variable=self.varDates, font=("Calibri", 12))
        chkCheck.grid(row=4, column=1, sticky=E, columnspan=2)

    def init_buttons(self):
        btnAdd = Button(self, text="Add a question", font=("Calibri", 12), width=16, height=1)
        btnAdd['command'] = self.add_question
        btnAdd.grid(row=(self.number_questions + 5), column=0, columnspan=2)
        btnSubmit = Button(self, text="Submit test", font=("Calibri", 12), width=16, height=1)
        btnSubmit['command'] = self.submit_test
        btnSubmit.grid(row=(self.number_questions + 5), column=2, columnspan=2)
        btnBack = Button(self, text="Cancel", font=("Calibri", 12), width=10, height=1)
        btnBack['command'] = self.test_cancel
        btnBack.grid(row=(self.number_questions + 5), column=0, sticky=W)
        self.dynamic_objects.append(btnBack)
        self.dynamic_objects.append(btnAdd)
        self.dynamic_objects.append(btnSubmit)

    def test_cancel(self):
        msgBox = messagebox.askquestion("Cancel", "Are you sure you want to cancel creating the assessment?", icon="warning")
        if msgBox == 'yes':
            self.master.destroy()
            self.previous.deiconify()

    def add_question(self):
        if self.number_questions == 10:
            messagebox.showerror("Error", "You can only have up to 10 questions")
        else:
            self.dynamic_objects[2].destroy()
            self.dynamic_objects[1].destroy()
            self.dynamic_objects[0].destroy()
            self.dynamic_objects.remove(self.dynamic_objects[2])
            self.dynamic_objects.remove(self.dynamic_objects[1])
            self.dynamic_objects.remove(self.dynamic_objects[0])
            lblQues = Label(self, text="Enter the question here:", font=("Calibri", 12, "bold"))
            self.dynamic_objects.append(lblQues)
            lblQues.grid(row=(self.number_questions + 5), column=0, sticky=SW)
            self.txtQues = Text(self, font=("Calibri", 12), width=35, height=4)
            self.dynamic_objects.append(self.txtQues)
            scrlQues = Scrollbar(self, command=self.txtQues.yview)
            self.dynamic_objects.append(scrlQues)
            self.txtQues['yscrollcommand'] = scrlQues.set
            self.txtQues.grid(row=(self.number_questions + 5), column=1, columnspan=2, rowspan=2, sticky=W)
            scrlQues.grid(row=(self.number_questions + 5), column=3, columnspan=3, rowspan=2)
            self.answer_correct = IntVar()
            self.answer_correct.set(1)
            self.add_question_buttons()

    def add_question_buttons(self):
        btnFinishQ = Button(self, text="Finish Question", font=("Calibri", 10))
        btnFinishQ['command'] = self.finish_question
        btnFinishQ.grid(row=(self.number_questions + self.number_answers + 7), column=1, sticky=E)
        btnRemoveAns = Button(self, text="Remove answer", font=("Calibri", 10))
        btnRemoveAns['command'] = self.remove_answer
        btnRemoveAns.grid(row=(self.number_questions + self.number_answers + 7), column=0, sticky=E)
        btnAddAns = Button(self, text="Add an answer", font=("Calibri", 10))
        btnAddAns['command'] = self.add_answer
        btnAddAns.grid(row=(self.number_questions + self.number_answers + 7), column=0, sticky=W)
        btnCancel = Button(self, text="Cancel the question", font=("Calibri", 10))
        btnCancel['command'] = self.cancel_question
        btnCancel.grid(row=(self.number_questions + self.number_answers + 7), column=2, sticky=E)
        self.dynamic_objects.append(btnRemoveAns)
        self.dynamic_objects.append(btnFinishQ)
        self.dynamic_objects.append(btnAddAns)
        self.dynamic_objects.append(btnCancel)

    def cancel_question(self):
        for i in range(len(self.dynamic_objects) - 1, -1, -1):
            self.dynamic_objects[i].destroy()
            self.dynamic_objects.remove(self.dynamic_objects[i])
        self.number_answers = 0
        self.init_buttons()

    def add_answer(self):
        if self.number_answers == 6:
            messagebox.showerror("Error", "There can only be up to 6 answers")
        else:
            for i in range(len(self.dynamic_objects) - 1, len(self.dynamic_objects) - 5, -1):
                self.dynamic_objects[i].destroy()
                self.dynamic_objects.remove(self.dynamic_objects[i])
            self.answer_obj = []
            self.answer_obj.append(Label(self, text=("Answer " + str(self.number_answers + 1) + ":"), font=("Calibri", 12, "bold")))
            self.answer_obj[0].grid(row=(self.number_questions + self.number_answers + 7), column=0, sticky=W)
            self.answer_obj.append(Entry(self, width=20, font=("Calibri", 12)))
            self.answer_obj[1].grid(row=(self.number_questions + self.number_answers + 7), column=1, sticky=W)
            self.answer_obj.append(Radiobutton(self, text="Correct", font=("Calibri", 12), variable=self.answer_correct, value=(self.number_answers + 1)))
            self.answer_obj[2].grid(row=(self.number_questions + self.number_answers + 7), column=2)
            self.answers.append(self.answer_obj[:])
            self.number_answers += 1

            for obj in self.answer_obj:
                self.dynamic_objects.append(obj)
            self.add_question_buttons()

    def finish_question(self):
        if self.txtQues.get("1.0", "end-1c") == '':
            messagebox.showerror("Error", "Please enter a question")
        elif self.answers == []:
            messagebox.showerror("Error", "Make sure there is at least 1 answer")
        else:
            flag = 0
            for lst in self.answers:
                if lst[1].get() == '':
                    flag = 1
                    messagebox.showerror("Error", "Make sure that each answer is filled in")
            if flag == 0:
                self.questions["Question_" + str(self.number_questions + 1)] = self.txtQues.get("1.0", "end-1c")
                lstAns = []
                for lst in self.answers:
                    lstAns.append(lst[1].get())
                self.questions["Answers_" + str(self.number_questions + 1)] = lstAns
                self.questions["Correct_Ans_" + str(self.number_questions + 1)] = self.answer_correct.get()
                lblNew = Label(self, font=("Calibri", 12))
                lblNew.grid(row=(self.number_questions + 5), column=0, columnspan=4, sticky=W)
                label_text = ""
                if len(self.questions["Question_" + str(self.number_questions + 1)]) >= 36:
                    label_text = self.questions["Question_" + str(self.number_questions + 1)][:33] + "..."
                else:
                    label_text = self.questions["Question_" + str(self.number_questions + 1)]
                lblNew['text'] = ("Question " + str(self.number_questions + 1) + ": " + label_text)
                self.number_questions += 1
                self.answers = []
                self.cancel_question()

    def remove_answer(self):
        if not self.answers == []:
            for i in range(len(self.dynamic_objects) - 1, len(self.dynamic_objects) - 8, -1):
                self.dynamic_objects[i].destroy()
                self.dynamic_objects.remove(self.dynamic_objects[i])
            self.answers.remove(self.answers[len(self.answers) - 1])
            self.number_answers -= 1
            self.add_question_buttons()

    def submit_test(self):
        msgBox = messagebox.askquestion("Submit", "Are you sure you want to submit the assessment?")
        if msgBox == 'yes':
            if self.questions == {}:
                messagebox.showerror("Error", "Please create at least one question")
            else:
                with open('tests\\tests.csv', 'r+', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    reader = csv.reader(csvFile)
                    counter = 1
                    for line in reader:
                        if line[0] == "TEST":
                            counter += 1
                    writer.writerow(["TEST", counter])
                    writer.writerow(["TITLE", self.inpTitle.get()])
                    writer.writerow(["TYPE", self.varType.get()])
                    writer.writerow(["DURATION", self.varDuration.get()])
                    writer.writerow(["DATES", self.calStart.get(), self.calEnd.get()])
                    writer.writerow(["USE_DATES", self.varDates.get()])
                    for i in range(1, self.number_questions + 1):
                        writer.writerow(["QUESTION_NO", i])
                        writer.writerow(["QUESTION", self.questions["Question_" + str(i)]])
                        counter = 1
                        for ans in self.questions["Answers_" + str(i)]:
                            if ans == self.questions["Answers_" + str(i)][self.questions["Correct_Ans_" + str(i)] - 1]:
                                writer.writerow(["ANSWER_" + str(counter), ans, 1])
                            else:
                                writer.writerow(["ANSWER_" + str(counter), ans, 0])
                            counter += 1
                self.master.destroy()
                self.previous.deiconify()
