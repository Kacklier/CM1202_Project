#Author: Wojtek
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import csv
import datetime

number_questions = 0
number_answers = 0
dynamic_objects = []
questions = {}
answers = []


class create_test(Frame):
    def __init__(self, master, previous):
        Frame.__init__(self, master)
        self.previous = previous
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

    def init_questions(self):
        global dynamic_objects
        btnAdd = Button(self, text="Add a question", font=("Calibri", 12), width=16, height=1)
        btnAdd['command'] = self.add_question
        btnAdd.grid(row=(number_questions + 5), column=0, columnspan=2)
        btnSubmit = Button(self, text="Submit test", font=("Calibri", 12), width=16, height=1)
        btnSubmit['command'] = self.submit_test
        btnSubmit.grid(row=(number_questions + 5), column=2, columnspan=2)
        dynamic_objects.append(btnAdd)
        dynamic_objects.append(btnSubmit)

    def add_question(self):
        global number_questions
        if number_questions == 10:
            messagebox.showerror("Error", "You can only have up to 10 questions")
        else:
            dynamic_objects[0].destroy()
            dynamic_objects[1].destroy()
            dynamic_objects.remove(dynamic_objects[1])
            dynamic_objects.remove(dynamic_objects[0])
            lblQues = Label(self, text="Enter the question here:", font=("Calibri", 12, "bold"))
            dynamic_objects.append(lblQues)
            lblQues.grid(row=(number_questions + 5), column=0, sticky=SW)
            self.txtQues = Text(self, font=("Calibri", 12), width=35, height=4)
            dynamic_objects.append(self.txtQues)
            scrlQues = Scrollbar(self, command=self.txtQues.yview)
            dynamic_objects.append(scrlQues)
            self.txtQues['yscrollcommand'] = scrlQues.set
            self.txtQues.grid(row=(number_questions + 5), column=1, columnspan=2, rowspan=2, sticky=W)
            scrlQues.grid(row=(number_questions + 5), column=3, columnspan=3, rowspan=2)
            self.answer_correct = IntVar()
            self.answer_correct.set(1)
            self.add_question_buttons()

    def add_question_buttons(self):
        global dynamic_objects
        btnFinishQ = Button(self, text="Finish Question", font=("Calibri", 10))
        btnFinishQ['command'] = self.finish_question
        btnFinishQ.grid(row=(number_questions + number_answers + 7), column=1, sticky=E)
        btnRemoveAns = Button(self, text="Remove answer", font=("Calibri", 10))
        btnRemoveAns['command'] = self.remove_answer
        btnRemoveAns.grid(row=(number_questions + number_answers + 7), column=0, sticky=E)
        btnAddAns = Button(self, text="Add an answer", font=("Calibri", 10))
        btnAddAns['command'] = self.add_answer
        btnAddAns.grid(row=(number_questions + number_answers + 7), column=0, sticky=W)
        btnCancel = Button(self, text="Cancel the question", font=("Calibri", 10))
        btnCancel['command'] = self.cancel_question
        btnCancel.grid(row=(number_questions + number_answers + 7), column=2, sticky=E)
        dynamic_objects.append(btnRemoveAns)
        dynamic_objects.append(btnFinishQ)
        dynamic_objects.append(btnAddAns)
        dynamic_objects.append(btnCancel)

    def cancel_question(self):
        global number_answers
        for i in range(len(dynamic_objects) - 1, -1, -1):
            dynamic_objects[i].destroy()
            dynamic_objects.remove(dynamic_objects[i])
        number_answers = 0
        self.init_questions()

    def add_answer(self):
        global anwsers
        global number_answers
        if number_answers == 6:
            messagebox.showerror("Error", "There can only be up to 6 answers")
        else:
            for i in range(len(dynamic_objects) - 1, len(dynamic_objects) - 5, -1):
                dynamic_objects[i].destroy()
                dynamic_objects.remove(dynamic_objects[i])
            self.answer_obj = []
            self.answer_obj.append(Label(self, text=("Answer " + str(number_answers + 1) + ":"), font=("Calibri", 12, "bold")))
            self.answer_obj[0].grid(row=(number_questions + number_answers + 7), column=0, sticky=W)
            self.answer_obj.append(Entry(self, width=20, font=("Calibri", 12)))
            self.answer_obj[1].grid(row=(number_questions + number_answers + 7), column=1, sticky=W)
            self.answer_obj.append(Radiobutton(self, text="Correct", font=("Calibri", 12), variable=self.answer_correct, value=(number_answers + 1)))
            self.answer_obj[2].grid(row=(number_questions + number_answers + 7), column=2)
            answers.append(self.answer_obj[:])
            number_answers += 1

            for obj in self.answer_obj:
                dynamic_objects.append(obj)
            self.add_question_buttons()

    def finish_question(self):
        global number_questions
        global answers
        if self.txtQues.get("1.0", "end-1c") == '':
            messagebox.showerror("Error", "Please enter a question")
        elif answers == []:
            messagebox.showerror("Error", "Make sure there is at least 1 answer")
        else:
            flag = 0
            for lst in answers:
                if lst[1].get() == '':
                    flag = 1
                    messagebox.showerror("Error", "Make sure that each answer is filled in")
            if flag == 0:
                questions["Question_" + str(number_questions + 1)] = self.txtQues.get("1.0", "end-1c")
                lstAns = []
                for lst in answers:
                    lstAns.append(lst[1].get())
                questions["Answers_" + str(number_questions + 1)] = lstAns
                questions["Correct_Ans_" + str(number_questions + 1)] = self.answer_correct.get()
                lblNew = Label(self, font=("Calibri", 12))
                lblNew.grid(row=(number_questions + 5), column=0, columnspan=4, sticky=W)
                label_text = ""
                if len(questions["Question_" + str(number_questions + 1)]) >= 36:
                    label_text = questions["Question_" + str(number_questions + 1)][:33] + "..."
                else:
                    label_text = questions["Question_" + str(number_questions + 1)]
                lblNew['text'] = ("Question " + str(number_questions + 1) + ": " + label_text)
                number_questions += 1
                answers = []
                self.cancel_question()

    def remove_answer(self):
        global number_answers
        global answers
        if not answers == []:
            for i in range(len(dynamic_objects) - 1, len(dynamic_objects) - 8, -1):
                dynamic_objects[i].destroy()
                dynamic_objects.remove(dynamic_objects[i])
            answers.remove(answers[len(answers) - 1])
            number_answers -= 1
            self.add_question_buttons()

    def submit_test(self):
        global number_questions
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
            for i in range(1, number_questions + 1):
                writer.writerow(["QUESTION_NO", i])
                writer.writerow(["QUESTION", questions["Question_" + str(i)]])
                counter = 1
                for ans in questions["Answers_" + str(i)]:
                    if ans == questions["Answers_" + str(i)][questions["Correct_Ans_" + str(i)] - 1]:
                        writer.writerow(["ANSWER_" + str(counter), ans, 1])
                    else:
                        writer.writerow(["ANSWER_" + str(counter), ans, 0])
                    counter += 1
        self.master.destroy()
        self.previous.deiconify()
