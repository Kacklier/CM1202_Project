from tkinter import *
from tkcalendar import DateEntry
import csv
import datetime

class student_menu(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.init_window(master)
		self.init_title()
		self.read_test()
		self.open_test()

	def init_window(self, master):
		master.title("Create a new test")
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
		

		#how can I close the current window and open the current_test window
		btnSubmit = Button(self, text="Submit", font=("Calibri", 12,), width=20, command=self.#idek what to put here)
		btnSubmit.grid(row=23, column=0, columnspan=3)