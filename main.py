from tkinter import *
from create_test import create_test
from student_menu import student_menu
from current_test import current_test
root = Tk()


class DisplayRoot(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Test creator")
        root.geometry("{}x{}".format("400", "200"))

        Label(root, text="Log in as:", font=("Cambria", 22)).grid(row=0, column=0, columnspan=2, padx=130)

        btnLecturer = Button(root, text="Lecturer", font=("Cambria", 18), width=10, height=2)
        btnLecturer['command'] = self.open_lecturer_menu
        btnLecturer.grid(row=1, column=0)

        btnStudent = Button(root, text="Student", font=("Cambria", 18), width=10, height=2)
        btnStudent['command'] = self.open_student_menu
        btnStudent.grid(row=1, column=1)

    def open_lecturer_menu(self):
        t1 = Toplevel(root)
        root.withdraw()
# TODO:
# create_test will need to be changed to lecturer_menu (or similar), which in turn can lead to create_test
        create_test(t1)
        t1.wm_protocol("WM_DELETE_WINDOW", root.destroy)

    def open_student_menu(self):
        t1 = Toplevel(root)
        root.withdraw()
        student_menu(t1)
        t1.wm_protocol("WM_DELETE_WINDOW", root.destroy)

root.resizable(width=False, height=False)
DisplayRoot(root)

root.mainloop()
