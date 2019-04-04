#Author: Jack
from tkinter import *
from tkcalendar import DateEntry
from current_test import current_test
import tkinter.messagebox 
import csv
import datetime


class student_menu(Frame):
	def __init__(self, master, previous):
		Frame.__init__(self, master)
		self.previous = previous
		self.grid()
		self.init_window(master)
		self.init_title()
		self.read_test()
		self.select_type()
		self.init_buttons()
		self.init_radio()
		self.fill_table()

	def init_window(self, master):
		master.title("Select a test")
		master.minsize(506, 0)
		master.resizable(width=False, height=False)

	def init_title(self):
		lblTitle = Label(self, text="Please choose a test:", font=("Calibri", 12, "bold"))
		lblTitle.grid(row=0, column=0, sticky=W)

	def init_radio(self):

		self.varforsum = IntVar()
		self.varforsum.set(1)
		rdoForm = Radiobutton(self, text= "formative", variable=self.varforsum, value=2)
		rdoForm.grid(row=5, column=3, columnspan=1)

		rdoSum = Radiobutton(self, text= "summative", variable=self.varforsum, value=1)
		rdoSum.grid(row=5, column=4, columnspan=1)

	def read_test(self):
		self.test_data = []
		self.titles = list()
		with open('tests\\tests.csv', newline='') as test_file:
			self.test_data = list(csv.reader(test_file))

		for key in self.test_data:
			if key[0] == "TITLE":
				self.titles.append(key[1])

	def fill_table(self):
		self.listProg = Listbox(self,height=3)
		scroll = Scrollbar(self,command=self.listProg.yview)
		self.listProg.configure(yscrollcommand=scroll.set)

		self.listProg.grid(row=0,column=2, columnspan=2, sticky=NE)
		scroll.grid(row=0,column=4,sticky=W)

		if self.varforsum.get() == 1:
			for item in self.summative:
				self.listProg.insert(END, item)
		elif self.varforsum.get() == 2:
			for item in self.formative:
				self.listProg.insert(END, item)


		self.listProg.selection_set(END)


	def init_buttons(self):
		btnOpen = Button(self, text="Open", font=("Calibri", 12,), width=20, command=self.open_test)
		btnOpen.grid(row=4, column=1, columnspan=3)

		btnReload = Button(self, text="Reload", font=("Calibri", 12,), width=20, command=self.fill_table)
		btnReload.grid(row=4, column=4, columnspan=3)

		btnBack = Button(self, text="Back", font=("Calibri", 12), width=10, command=self.go_back)
		btnBack.grid(row=0, column=4, sticky=E, rowspan=2)

	def open_test(self, master=None):
		choice = self.listProg.get(ANCHOR)
		if choice == "":
			tkinter.messagebox.showwarning("Entry Error", "Please select a test")
		else:
			t1 = Toplevel(self)
			current_test(t1, choice, self.varforsum.get())

	def select_type(self):
		self.summative = list()
		self.formative = list()
		count = len(self.test_data)
		titlecount = len(self.titles)
		for i in range(0, count):
			if self.test_data[i][0] == "TYPE":
				for items in range(0, titlecount):
					if self.titles[items] == self.test_data[i - 1][1]:
						if self.test_data[i][1] == "summative":
							self.summative.append(self.titles[items])
						if self.test_data[i][1] == "formative":
							self.formative.append(self.titles[items])

	def go_back(self):
		self.master.destroy()
		self.previous.deiconify()
