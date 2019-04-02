from tkinter import *
from test_db_template import Test
from tkcalendar import DateEntry
import csv
import datetime

class current_test(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.init_window(master)


	def init_window(self, master):
		master.title("Create a new test")
		master.minsize(506, 0)