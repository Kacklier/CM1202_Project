from tkinter import *
from test_db_template import Test
from tkcalendar import DateEntry
import student_menu
import csv
import datetime

class current_test(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.init_window(master)
		self.read_test()

	def read_test(self):
		test_data = []
		titles = list()
		with open('tests\\tests.csv', newline='') as test_file:
			test_data = list(csv.reader(test_file))

		for key in test_data:
			break

	def init_window(self, master):
		master.title(choice)
		master.minsize(506, 0)
