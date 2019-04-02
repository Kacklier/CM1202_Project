from tkinter import *
from test_db_template import Test
from tkcalendar import DateEntry
import csv
import datetime


class current_test(Frame):
	
	def __init__(self, master, choice):
		Frame.__init__(self, master)
		self.choice = choice
		self.grid()
		self.init_window(master)
		self.read_test()
		self.show_test()

	def read_test(self):
		test_data = []
		titles = list()
		cont = True
		counter = 0
		startpoint = 0
		endpoint = 0
		with open('tests\\tests.csv', newline='') as test_file:
			test_data = list(csv.reader(test_file))

		for key in test_data:
			counter += 1
			if key[0] == "TITLE":
				if key[1] == self.choice:
					startpoint = counter-2
				elif key[1] != self.choice and startpoint != 0:
					endpoint = counter-3
		if endpoint ==0:
			endpoint = counter -1
		print(startpoint)
		print(endpoint)
		questionstart = startpoint + 7

		lblTitle = Label(self, text="Title: ", font=("Calibri", 12, "bold"))
		lblTitle.grid(row=0, column=0, sticky=W)
		varTitle = Label(self, text=test_data[startpoint + 1][1], font=("Calibri", 12))
		varTitle.grid(row=0, column=1, sticky=W)

		lblType = Label(self, text="Test type: ", font=("Calibri", 12, "bold"))
		lblType.grid(row=1, column=0, sticky=W)
		varType = Label(self, text=test_data[startpoint + 2][1], font=("Calibri", 12))
		varType.grid(row=1, column=1, sticky=W)

		lblTime = Label(self, text="Time:  ", font=("Calibri", 12, "bold"))
		lblTime.grid(row=2, column=0, sticky=W)
		varTime = Label(self, text=test_data[startpoint + 3][1], font=("Calibri", 12))
		varTime.grid(row=2, column=1, sticky=W)
		print(questionstart - startpoint)
		print(questionstart)
		print(test_data[questionstart][1])

		self.varA1 = IntVar()
		self.varA2 = IntVar()
		if questionstart - startpoint == 7:
			self.txtQ1 = Label(self,text = test_data[questionstart][1], font=("Calibri", 12), height=4, width=35)
			self.txtQ1.grid(row=5, column=0, columnspan=2)

			rdoA11 = Radiobutton(self, text=test_data[questionstart + 1][1], variable=self.varA1, value=1)
			rdoA11.grid(row=5, column=1, columnspan=1)

			rdoA12 = Radiobutton(self, text=test_data[questionstart + 2][1], variable=self.varA1, value=2)
			rdoA12.grid(row=5, column=2, columnspan=1)
			
			rdoA13 = Radiobutton(self, text=test_data[questionstart + 3][1], variable=self.varA1, value=3)
			rdoA13.grid(row=5, column=3, columnspan=1)

			rdoA14 = Radiobutton(self, text=test_data[questionstart + 4][1], variable=self.varA1, value=4)
			rdoA14.grid(row=5, column=4, columnspan=1)

			questionstart += 6
			self.txtQ2 = Label(self,text = test_data[questionstart][1], font=("Calibri", 12), height=4, width=35)
			self.txtQ2.grid(row=6, column=0, columnspan=2)

			rdoA21 = Radiobutton(self, text=test_data[questionstart + 1][1], variable=self.varA2, value=1)
			rdoA21.grid(row=6, column=1, columnspan=1)

			rdoA22 = Radiobutton(self, text=test_data[questionstart + 2][1], variable=self.varA2, value=2)
			rdoA22.grid(row=6, column=2, columnspan=1)
			
			rdoA23 = Radiobutton(self, text=test_data[questionstart + 3][1], variable=self.varA2, value=3)
			rdoA23.grid(row=6, column=3, columnspan=1)

			rdoA24 = Radiobutton(self, text=test_data[questionstart + 4][1], variable=self.varA2, value=4)
			rdoA24.grid(row=6, column=4, columnspan=1)







	def init_window(self, master):
		master.title(self.choice)
		master.minsize(506, 0)

	def show_test(self):
		pass

