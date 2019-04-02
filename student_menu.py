from tkinter import *
from tkcalendar import DateEntry
from current_test import current_test
import tkinter.messagebox 
import csv
import datetime

class student_menu(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.init_window(master)
		self.init_title()
		self.read_test()

	def init_window(self, master):
		master.title("Select a test")
		master.minsize(506, 0)

	def init_title(self):
		lblTitle = Label(self, text="Please choose a test:", font=("Calibri", 12, "bold"))
		lblTitle.grid(row=0, column=0, sticky=W)


	def read_test(self):
		test_data = []
		titles = list()
		with open('tests\\tests.csv', newline='') as test_file:
			test_data = list(csv.reader(test_file))

		for key in test_data:
			print(key)
			if key[0] == "TITLE":
				titles.append(key[1])


		#these can be removed soon
		print(test_data)
		print(titles)
		print(test_data[1][0])

		self.listProg = Listbox(self,height=3)
		scroll = Scrollbar(self,command=self.listProg.yview)
		self.listProg.configure(yscrollcommand=scroll.set)

		self.listProg.grid(row=0,column=2, columnspan=2, sticky=NE)
		scroll.grid(row=0,column=4,sticky=W)

		for item in titles:
			self.listProg.insert(END, item)

		self.listProg.selection_set(END)
		
		btnSubmit = Button(self, text="Submit", font=("Calibri", 12,), width=20, command=self.open_test)
		btnSubmit.grid(row=4, column=3, columnspan=3)



	def open_test(self, master=None):
		choice = self.listProg.get(ANCHOR)
		print(choice)
		if choice == "":
			tkinter.messagebox.showwarning("Entry Error, please select a test")
		else:
			t1 = Toplevel(self)
			current_test(t1, choice)