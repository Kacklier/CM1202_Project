#Author: Jack
from tkinter import *
from tkcalendar import DateEntry
import csv
import tkinter.messagebox
import time
from datetime import datetime, timedelta

class current_test(Frame):
	
	def __init__(self, master, choice, FormSum):
		Frame.__init__(self, master)
		self.choice = choice
		self.FormSum = FormSum
		self.grid()
		self.init_window(master)
		self.read_test()
		self.question_load()
		self.init_button()
		self.create_timer()


	def create_timer(self):
		self.now = IntVar()
		self.completed = False
		
		self.time = Label(self, font=('Helvetica', 24))
		self.time.grid(row=2, column=5)
		self.time["textvariable"] = self.now
		
		self.time_start = int(self.test_data[self.startpoint + 3][1])*60
		
		self.auto_update()


	def auto_update(self):
		self.time_start -= 1
		self.displaytime = timedelta(seconds=self.time_start)
		self.now.set(self.displaytime)
		self.after(1000, self.auto_update)
	

	def init_window(self, master):
		master.title(self.choice)
		master.minsize(506, 0)

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

		if self.endpoint ==0 and self.startpoint != 0:
			self.endpoint = counter -1
		elif self.endpoint ==0 and self.startpoint == 0:
			counter = 0
			for key in self.test_data:
				counter += 1
				if key[0] == "TITLE":
					if key[1] != self.choice:
						self.endpoint = counter - 3
						break
		print(self.startpoint)
		print(self.endpoint)

		lblTitle = Label(self, text="Title: ", font=("Calibri", 12, "bold"))
		lblTitle.grid(row=0, column=0, sticky=W)
		txtTitle = Label(self, text= self.test_data[self.startpoint + 1][1], font=("Calibri", 12))
		txtTitle.grid(row=0, column=1, sticky=W)

		lblType = Label(self, text="Test type: ", font=("Calibri", 12, "bold"))
		lblType.grid(row=1, column=0, sticky=W)
		txtType = Label(self, text= self.test_data[self.startpoint + 2][1], font=("Calibri", 12))
		txtType.grid(row=1, column=1, sticky=W)

		lblTime = Label(self, text="Time:  ", font=("Calibri", 12, "bold"))
		lblTime.grid(row=2, column=0, sticky=W)
		txtTime = Label(self, text= self.test_data[self.startpoint + 3][1], font=("Calibri", 12))
		txtTime.grid(row=2, column=1, sticky=W)


		lblName = Label(self, text="Enter Name:  ", font=("Calibri", 12, "bold"))
		lblName.grid(row=3, column=0, sticky=W)
		self.inpName = Entry(self, width=35, font=("Calibri", 12))
		self.inpName.grid(row=3, column=1, sticky=W)
		self.questionstart = self.startpoint + 7

		self.varCB1 = IntVar()
		CB1 = Checkbutton(self,text="Final Attempt", variable=self.varCB1)
		CB1.grid(row=14,column=0,columnspan=4,sticky=W)

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
		self.varA1.set(1)
		self.varA2.set(1)
		self.varA3.set(1)
		self.varA4.set(1)
		self.varA5.set(1)
		self.varA6.set(1)
		self.varA7.set(1)
		self.varA8.set(1)
		self.varA9.set(1)
		self.varA10.set(1)
		self.question_count = 0

		if self.questionstart - self.startpoint == 7:
			self.question_count += 1
			txtQ1 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ1.grid(row=5, column=0, columnspan=2, sticky=W)

			rdoA11 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA1, value=1)
			rdoA11.grid(row=5, column=3, columnspan=1)

			rdoA12 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA1, value=2)
			rdoA12.grid(row=5, column=4, columnspan=1)
			
			rdoA13 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA1, value=3)
			rdoA13.grid(row=5, column=5, columnspan=1)

			rdoA14 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA1, value=4)
			rdoA14.grid(row=5, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6


		if self.questionstart - self.startpoint == 13:
			self.question_count += 1
			txtQ2 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ2.grid(row=6, column=0, columnspan=2, sticky=W)

			rdoA21 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA2, value=1)
			rdoA21.grid(row=6, column=3, columnspan=1)

			rdoA22 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA2, value=2)
			rdoA22.grid(row=6, column=4, columnspan=1)
			
			rdoA23 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA2, value=3)
			rdoA23.grid(row=6, column=5, columnspan=1)

			rdoA24 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA2, value=4)
			rdoA24.grid(row=6, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6


		if self.questionstart - self.startpoint == 19:
			self.question_count += 1
			self.txtQ3 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			self.txtQ3.grid(row=7, column=0, columnspan=2, sticky=W)

			rdoA31 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA3, value=1)
			rdoA31.grid(row=7, column=3, columnspan=1)

			rdoA32 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA3, value=2)
			rdoA32.grid(row=7, column=4, columnspan=1)
			
			rdoA33 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA3, value=3)
			rdoA33.grid(row=7, column=5, columnspan=1)

			rdoA34 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA3, value=4)
			rdoA34.grid(row=7, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 25:
			self.question_count += 1
			txtQ4 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ4.grid(row=8, column=0, columnspan=2, sticky=W)

			rdoA41 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA4, value=1)
			rdoA41.grid(row=8, column=3, columnspan=1)

			rdoA42 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA4, value=2)
			rdoA42.grid(row=8, column=4, columnspan=1)
			
			rdoA43 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA4, value=3)
			rdoA43.grid(row=8, column=5, columnspan=1)

			rdoA44 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA4, value=4)
			rdoA44.grid(row=8, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 31:
			self.question_count += 1
			txtQ5 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ5.grid(row=9, column=0, columnspan=2, sticky=W)

			rdoA51 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA5, value=1)
			rdoA51.grid(row=9, column=3, columnspan=1)

			rdoA52 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA5, value=2)
			rdoA52.grid(row=9, column=4, columnspan=1)
			
			rdoA53 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA5, value=3)
			rdoA53.grid(row=9, column=5, columnspan=1)

			rdoA54 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA5, value=4)
			rdoA54.grid(row=9, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6


		if self.questionstart - self.startpoint == 37:
			self.question_count += 1
			txtQ6 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ6.grid(row=10, column=0, columnspan=2, sticky=W)

			rdoA61 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA6, value=1)
			rdoA61.grid(row=10, column=3, columnspan=1)

			rdoA62 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA6, value=2)
			rdoA62.grid(row=10, column=4, columnspan=1)
			
			rdoA63 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA6, value=3)
			rdoA63.grid(row=10, column=5, columnspan=1)

			rdoA64 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA6, value=4)
			rdoA64.grid(row=10, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 43:
			self.question_count += 1
			txtQ7 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ7.grid(row=11, column=0, columnspan=2, sticky=W)

			rdoA71 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA7, value=1)
			rdoA71.grid(row=11, column=3, columnspan=1)

			rdoA72 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA7, value=2)
			rdoA72.grid(row=11, column=4, columnspan=1)
			
			rdoA73 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA7, value=3)
			rdoA73.grid(row=11, column=5, columnspan=1)

			rdoA74 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA7, value=4)
			rdoA74.grid(row=11, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 49:
			self.question_count += 1
			txtQ8 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ8.grid(row=12, column=0, columnspan=2, sticky=W)

			rdoA81 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA8, value=1)
			rdoA81.grid(row=12, column=3, columnspan=1)

			rdoA82 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA8, value=2)
			rdoA82.grid(row=12, column=4, columnspan=1)
			
			rdoA83 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA8, value=3)
			rdoA83.grid(row=12, column=5, columnspan=1)

			rdoA84 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA8, value=4)
			rdoA84.grid(row=12, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 55:
			self.question_count += 1
			txtQ9 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ9.grid(row=13, column=0, columnspan=2, sticky=W)

			rdoA91 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA9, value=1)
			rdoA91.grid(row=13, column=3, columnspan=1)

			rdoA92 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA9, value=2)
			rdoA92.grid(row=13, column=4, columnspan=1)
			
			rdoA93 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA9, value=3)
			rdoA93.grid(row=13, column=5, columnspan=1)

			rdoA94 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA9, value=4)
			rdoA94.grid(row=13, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6

		if self.questionstart - self.startpoint == 61:
			self.question_count += 1
			txtQ10 = Label(self,text = self.test_data[self.questionstart][1], font=("Calibri", 12), height=2)
			txtQ10.grid(row=13, column=0, columnspan=2, sticky=W)

			rdoA101 = Radiobutton(self, text= self.test_data[self.questionstart + 1][1], variable=self.varA10, value=1)
			rdoA101.grid(row=13, column=3, columnspan=1)

			rdoA102 = Radiobutton(self, text= self.test_data[self.questionstart + 2][1], variable=self.varA10, value=2)
			rdoA102.grid(row=13, column=4, columnspan=1)
			
			rdoA103 = Radiobutton(self, text= self.test_data[self.questionstart + 3][1], variable=self.varA10, value=3)
			rdoA103.grid(row=13, column=5, columnspan=1)

			rdoA104 = Radiobutton(self, text= self.test_data[self.questionstart + 4][1], variable=self.varA10, value=4)
			rdoA104.grid(row=13, column=6, columnspan=1)

			if self.questionstart + 6 < self.endpoint:
				self.questionstart +=6


	def init_button(self):
		if self.FormSum == 1:
			btnSubmitSum = Button(self, text="Summative Submit", font=("Calibri", 12,), width=20, command=self.sum_check)
			btnSubmitSum.grid(row=15, column=3, columnspan=3)
		elif self.FormSum == 2:
			btnSubmitForm = Button(self, text="Formative Submit", font=("Calibri", 12,), width=20, command=self.form_check)
			btnSubmitForm.grid(row=15, column=3, columnspan=3)


	def sum_check(self):
		if self.time_start > 0:
			if self.completed == False:
				self.save_results()
			else:
				tkinter.messagebox.showwarning("Cannot submit twice!")
		else:
			tkinter.messagebox.showwarning("Time has run out!")


	def form_check(self):
		if self.time_start > 0:
			self.final_attempt()
		else:
			tkinter.messagebox.showwarning("Time has run out!")
		


	def save_results(self):
		if self.inpName == "":
			tkinter.messagebox.showwarning("Please input Name")
		else:
			with open('tests\\results.csv', 'r+', newline='') as results_file:
				writer = csv.writer(results_file)
				reader = csv.reader(results_file)
				counter = 1
				for line in reader:
					if line[0] == "TEST":
						counter += 1
				writer.writerow(["TEST", counter])
				writer.writerow(["TITLE", self.test_data[self.startpoint + 1][1]])
				writer.writerow(["NAME", self.inpName.get()])
				writer.writerow(["TYPE", self.test_data[self.startpoint + 2][1]])
				
				questions = [1,2,3,4,5,6,7,8,9,10]
				answers = [self.varA1.get(), self.varA2.get(), self.varA3.get(), self.varA4.get(), self.varA5.get(), self.varA6.get(), self.varA7.get(), self.varA8.get(), self.varA9.get(), self.varA10.get()]

				for i in range(0,self.question_count):
					writer.writerow(["QUESTION_NO", questions[i]])
					writer.writerow(["ANSWER", answers[i]])
			tkinter.messagebox.showwarning("Saved")
			if self.FormSum == 1:
				self.completed = True
		
 

	def final_attempt(self):
		print(self.varCB1.get())
		if self.varCB1.get() == 1:
			self.save_results()
		else:
			tkinter.messagebox.showwarning("Results Not Saved")
