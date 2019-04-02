from tkinter import *
from test_db_template import Test
from tkcalendar import DateEntry
import csv
import datetime

class student_menu(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.init_window(master)
		self.init_title()
		self.init_test_select()
		self.read_test()

	def init_window(self, master):
		master.title("Create a new test")
		master.minsize(506, 0)

	def init_title(self):
		lblTitle = Label(self, text="Please choose a test:", font=("Calibri", 12, "bold"))
		lblTitle.grid(row=0, column=0, sticky=W)

	def init_test_select(self):
		self.listProg = Listbox(self,height=3)
		scroll = Scrollbar(self,command=self.listProg.yview)
		self.listProg.configure(yscrollcommand=scroll.set)

		self.listProg.grid(row=0,column=2, columnspan=2, sticky=NE)
		scroll.grid(row=0,column=4,sticky=W)

		for item in ["CS", "CS with", "BIS", "SE", "Joints", ""]:
			self.listProg.insert(END, item)

		self.listProg.selection_set(END)

	def read_test(self):
		#with open('test\\test.csv', 'rb') as test_file:
		#	reader = csv.reader(test_file)
		#	counter = 0
			#for row in reader:
			#	if row[0] == "TITLE":
		pass






