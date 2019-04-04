from tkinter import *
import csv
from collections import OrderedDict

class modify_menu(Frame):
        def __init__(self, master, previous):
                Frame.__init__(self, master)
                self.previous = previous
                self.grid()
                self.test_fetch()
                self.init_window()
                self.init_title()
                self.fill_table()
                self.init_buttons()

        def init_window(self):
                self.master.title("Modify Menu")
                self.master.minsize(500, 200)
        

        def test_fetch(self):
                #updates test_data and titles
                self.test_data = [] #list of list of each line ie [['TITILE', '1'], ['TEST', 'MATHS1']]
                self.titles = list() #list of test titles
                with open('tests\\tests.csv', newline='') as test_file:
                        self.test_data = list(csv.reader(test_file))
                for key in self.test_data:
                        if key[0] == "TITLE":
                                self.titles.append(key[1])

        def init_title(self):
                test_choice_title = Label(self, text="Please choose a test:", font=("Calibri", 12, "bold"))
                test_choice_title.grid(row=0, column=0, sticky=W)

        def fill_table(self):
                #fills listbox from self.titles list
                self.test_fetch()
                self.test_title_list = Listbox(self,height=3, exportselection=0)
                scroll = Scrollbar(self,command=self.test_title_list.yview)
                self.test_title_list.configure(yscrollcommand=scroll.set)

                self.test_title_list.grid(row=0,column=2, columnspan=2, sticky=NE)
                scroll.grid(row=0,column=4,sticky=W)

                for test_title in self.titles:
                        self.test_title_list.insert(END, test_title)

                self.test_title_list.selection_set(END)

                self.question_select = Listbox(self, height = 3, exportselection=0)
                scroll2 = Scrollbar(self, command=self.question_select.yview)
                self.question_select.configure(yscrollcommand=scroll2.set)

                self.question_select.grid(row=0,column=5, columnspan=2, sticky=NE)
                scroll2.grid(row=0,column=7,sticky=W)

                for i in range(10):
                        self.question_select.insert(END, i+1)

                #choice = Button(self, text="Select question")
                self.question_entry = Entry(self, width=35, font=("Calibri", 12))
                self.question_entry.grid(row=6, column=3, columnspan=2)

                #entry boxes for answers
                self.ans1_entry = Entry(self, width=35, font=("Calibri", 12))
                self.ans1_entry.grid(row=7, column=3, columnspan=2)
                self.ans2_entry = Entry(self, width=35, font=("Calibri", 12))
                self.ans2_entry.grid(row=8, column=3, columnspan=2)
                self.ans3_entry = Entry(self, width=35, font=("Calibri", 12))
                self.ans3_entry.grid(row=9, column=3, columnspan=2)
                self.ans4_entry = Entry(self, width=35, font=("Calibri", 12))
                self.ans4_entry.grid(row=10, column=3, columnspan=2)
                self.ans5_entry = Entry(self, width=35, font=("Calibri", 12))
                self.ans5_entry.grid(row=10, column=3, columnspan=2)

        def fill_second_table(self):
                self.to_edit = self.test_title_list.get(ANCHOR)
                self.question_to_edit = self.question_select.get(ANCHOR)
                self.test_fetch()

                ordered_titles = OrderedDict({str(index): x for index, x in enumerate(self.titles, start=1)})
                for line in self.test_data:
                        if line[1] == self.to_edit:
                                for key, value in ordered_titles.items():
                                        if value == self.to_edit:
                                                num_to_change = key
                #num_to_change is the test number
                found = False
                q1pos = -1
                q2pos = -1
                q3pos = -1
                q4pos = -1
                q5pos = -1
                ques = -1
                #iterate through test_data again, if entry is not empty then replace for respective question
                for value, line in enumerate(self.test_data):
                        print(value, line)
                        if found != True:
                        #check for the correct test
                                if line[0] == 'TEST' and line[1] == num_to_change:
                                        
                                        found = True
                        if found == True:
                                if line[0] ==  'QUESTION_NO' and line[1] == '1':
                                        if len(self.question_entry.get()) > 0:
                                                #save the position of all of the questions 
                                                ques = value + 1
                                                found = False
                                if line[0] ==  'QUESTION' and line[1] == '1':
                                        if len(self.ans1_entry.get()) > 0:
                                                q1pos = value + 1
                                                found = False

                                if line[0] ==  'ANSWER_1':
                                        if len(self.ans2_entry.get()) > 0:       
                                                q2pos = value + 1
                                                found = False          
                                if line[0] ==  'ANSWER_2':
                                        if len(self.ans3_entry.get()) > 0:
                                                q3pos = value + 1
                                                found = False   
                                if line[0] ==  'ANSWER_3':
                                        if len(self.ans4_entry.get()) > 0:
                                                q4pos = value + 1
                                                found = False               
                                if line[0] ==  'ANSWER_4':                                       
                                        if len(self.ans5_entry.get()) > 0:
                                                q5pos = value + 1
                                                found = False

                                

                if q1pos != -1:
                        self.test_data[q1pos][1] = self.ans1_entry.get()
                if q2pos != -1:
                        self.test_data[q2pos][1] = self.ans2_entry.get()
                if q3pos != -1:
                        self.test_data[q3pos][1] = self.ans3_entry.get()
                if q4pos != -1:
                        self.test_data[q4pos][1] = self.ans4_entry.get()
                if q5pos != -1:
                        self.test_data[q5pos][1] = self.ans5_entry.get()
                print(self.test_data)





        def init_buttons(self):
                btnDel = Button(self, text="Delete Assessment", font=("Calibri", 12,), width=20, command=self.del_ass)
                btnDel.grid(row=4, column=1, columnspan=2)

                btnEdit = Button(self, text="Edit Assessment", font=("Calibri", 12,), width=20, command=self.fill_second_table)
                btnEdit.grid(row=4, column=3, columnspan=2)

                btnRel = Button(self, text="Reload", font=("Calibri", 12,), width=20, command=self.fill_table)
                btnRel.grid(row=4, column=5, columnspan=2)

        

        def del_ass(self):
                
                self.to_delete = self.test_title_list.get(ANCHOR)
                #finds the test number to be deleted
                new_data = []
                to_keep = False
                ordered_titles = OrderedDict({str(index): x for index, x in enumerate(self.titles, start=1)})
                #needlessly complicated nesting
                for line in self.test_data:
                        if line[1] == self.to_delete:
                                for key, value in ordered_titles.items():
                                        if value == self.to_delete:
                                                num_to_change = key
                #creates a new list of lines (new_data) to add to csv file minus test to be deleted (num_to_change)
                stop_adding = False
                for line in self.test_data:
                        if stop_adding == False:

                                if line[0] == 'TEST':
                                        if line[1] == str(num_to_change):
                                                count = str(num_to_change)
                                                stop_adding = True
                                        else:
                                                new_data.append(line)
                                else:
                                        new_data.append(line)
                        else:
                                if line[0] == 'TEST':
                                        new_data.append(line)
                                        stop_adding = False

                                else:
                                        pass

                #recalculates test number and writes to csv file (otherwise new tests are labelled wrong)
                with open('tests\\tests.csv', 'w', newline='') as csvFile:
                        count = 0
                        for i in new_data:
                                print("Count", count)
                                if i[0] == 'TEST':
                                        count += 1
                                        print("BEFORE", i)
                                        i[1] = str(count)
                                        print("AFTER",i)
                                else:
                                        pass
                                
                        writer = csv.writer(csvFile)
                        writer.writerows(new_data)


