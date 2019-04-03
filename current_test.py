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
		self.question_load()

	def read_test(self):
		self.test_data = []
		self.titles = list()
		counter = 0
		self.startpoint = 0
		self.endpoint = 0
		with open('tests\\tests.csv', newline='') as test_file:
			self.test_data = list(csv.reader(test_file))

		for key in self.test_data:
			counter += 1
			if key[0] == "TITLE":
				if key[1] == self.choice:
					self.startpoint = counter-2
				elif key[1] != self.choice and self.startpoint != 0:
					self.endpoint = counter-3
		if self.endpoint ==0:
			self.endpoint = counter -1

		lblTitle = Label(self, text="Title: ", font=("Calibri", 12, "bold"))
		lblTitle.grid(row=0, column=0, sticky=W)
		varTitle = Label(self, text= self.test_data[self.startpoint + 1][1], font=("Calibri", 12))
		varTitle.grid(row=0, column=1, sticky=W)

		lblType = Label(self, text="Test type: ", font=("Calibri", 12, "bold"))
		lblType.grid(row=1, column=0, sticky=W)
		varType = Label(self, text= self.test_data[self.startpoint + 2][1], font=("Calibri", 12))
		varType.grid(row=1, column=1, sticky=W)

		lblTime = Label(self, text="Time:  ", font=("Calibri", 12, "bold"))
		lblTime.grid(row=2, column=0, sticky=W)
		varTime = Label(self, text= self.test_data[self.startpoint + 3][1], font=("Calibri", 12))
		varTime.grid(row=2, column=1, sticky=W)
		self.questionstart = self.startpoint + 7

	def question_load(self):
		self.varA1 = IntVar()
		self.varA2 = IntVar()
		self.varA3 = IntVar()
		self.varA4 = IntVar()
		self.varA5 = IntVar()
		self.varA6 = IntVar()
		self.varA7 = IntVar()
		self.varA8 = IntVar()
		self.varA9 = IntVar()
		self.varA10 = IntVar()

		if self.questionstart - self.startpoint == 7:
			txtQ1 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ1.grid(row=5, column=0, columnspan=2)

			rdoA11 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA1, value=1)
			rdoA11.grid(row=5, column=1, columnspan=1)

			rdoA12 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA1, value=2)
			rdoA12.grid(row=5, column=2, columnspan=1)
			
			rdoA13 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA1, value=3)
			rdoA13.grid(row=5, column=3, columnspan=1)

			rdoA14 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA1, value=4)
			rdoA14.grid(row=5, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6


		if self.questionstart - self.startpoint == 13:
			txtQ2 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ2.grid(row=6, column=0, columnspan=2)

			rdoA21 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA2, value=1)
			rdoA21.grid(row=6, column=1, columnspan=1)

			rdoA22 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA2, value=2)
			rdoA22.grid(row=6, column=2, columnspan=1)
			
			rdoA23 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA2, value=3)
			rdoA23.grid(row=6, column=3, columnspan=1)

			rdoA24 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA2, value=4)
			rdoA24.grid(row=6, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6


		if self.questionstart - self.startpoint == 19:
			self.txtQ3 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			self.txtQ3.grid(row=7, column=0, columnspan=2)

			rdoA31 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA3, value=1)
			rdoA31.grid(row=7, column=1, columnspan=1)

			rdoA32 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA3, value=2)
			rdoA32.grid(row=7, column=2, columnspan=1)
			
			rdoA33 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA3, value=3)
			rdoA33.grid(row=7, column=3, columnspan=1)

			rdoA34 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA3, value=4)
			rdoA34.grid(row=7, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 25:
			txtQ4 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ4.grid(row=8, column=0, columnspan=2)

			rdoA41 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA4, value=1)
			rdoA41.grid(row=8, column=1, columnspan=1)

			rdoA42 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA4, value=2)
			rdoA42.grid(row=8, column=2, columnspan=1)
			
			rdoA43 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA4, value=3)
			rdoA43.grid(row=8, column=3, columnspan=1)

			rdoA44 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA4, value=4)
			rdoA44.grid(row=8, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 31:
			txtQ5 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ5.grid(row=9, column=0, columnspan=2)

			rdoA51 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA5, value=1)
			rdoA51.grid(row=9, column=1, columnspan=1)

			rdoA52 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA5, value=2)
			rdoA52.grid(row=9, column=2, columnspan=1)
			
			rdoA53 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA5, value=3)
			rdoA53.grid(row=9, column=3, columnspan=1)

			rdoA54 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA5, value=4)
			rdoA54.grid(row=9, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6


		if self.questionstart - self.startpoint == 37:
			txtQ6 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ6.grid(row=10, column=0, columnspan=2)

			rdoA61 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA6, value=1)
			rdoA61.grid(row=10, column=1, columnspan=1)

			rdoA62 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA6, value=2)
			rdoA62.grid(row=10, column=2, columnspan=1)
			
			rdoA63 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA6, value=3)
			rdoA63.grid(row=10, column=3, columnspan=1)

			rdoA64 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA6, value=4)
			rdoA64.grid(row=10, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 43:
			txtQ7 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ7.grid(row=11, column=0, columnspan=2)

			rdoA71 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA7, value=1)
			rdoA71.grid(row=11, column=1, columnspan=1)

			rdoA72 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA7, value=2)
			rdoA72.grid(row=11, column=2, columnspan=1)
			
			rdoA73 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA7, value=3)
			rdoA73.grid(row=11, column=3, columnspan=1)

			rdoA74 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA7, value=4)
			rdoA74.grid(row=11, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 49:
			txtQ8 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ8.grid(row=12, column=0, columnspan=2)

			rdoA81 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA8, value=1)
			rdoA81.grid(row=12, column=1, columnspan=1)

			rdoA82 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA8, value=2)
			rdoA82.grid(row=12, column=2, columnspan=1)
			
			rdoA83 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA8, value=3)
			rdoA83.grid(row=12, column=3, columnspan=1)

			rdoA84 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA8, value=4)
			rdoA84.grid(row=12, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 55:
			txtQ9 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ9.grid(row=13, column=0, columnspan=2)

			rdoA91 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA9, value=1)
			rdoA91.grid(row=13, column=1, columnspan=1)

			rdoA92 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA9, value=2)
			rdoA92.grid(row=13, column=2, columnspan=1)
			
			rdoA93 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA9, value=3)
			rdoA93.grid(row=13, column=3, columnspan=1)

			rdoA94 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA9, value=4)
			rdoA94.grid(row=13, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 61:
			txtQ10 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=4, width=35)
			txtQ10.grid(row=13, column=0, columnspan=2)

			rdoA101 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA10, value=1)
			rdoA101.grid(row=13, column=1, columnspan=1)

			rdoA102 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA10, value=2)
			rdoA102.grid(row=13, column=2, columnspan=1)
			
			rdoA103 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA10, value=3)
			rdoA103.grid(row=13, column=3, columnspan=1)

			rdoA104 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA10, value=4)
			rdoA104.grid(row=13, column=4, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6






	def init_window(self, master):
		master.title(self.choice)
		master.minsize(506, 0)

