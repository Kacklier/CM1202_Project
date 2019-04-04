#Author: Jamie
from tkinter import *
from tkinter import ttk
from resultworker import *

root = Tk()

studentnames = []
studentresults = {}

def generate_data(test_type):
    tests = GetTests(test_type)

    students = []
    for test in tests:
        x = get_students_results(test[0], test[1])
        if len(x) > 0:
            students.append(get_students_results(test[0], test[1]))
        else:
            continue

    global studentnames, studentresults
    for student in students:
        for x in student:
            if len(x[0]) > 0:
                studentnames.append(x[0])
                studentresults[x[0]] = x[1]

generate_data("summative")

sortType = { 'summative':'Summative Tests'}

sortby = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()

def showData(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        student_name = studentnames[idx]
        student_result = studentresults[student_name]
        statusmsg.set(f"The result of student {student_name} is {student_result}%")
    sentmsg.set('')

c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)


lbox = Listbox(c)
lbox.insert("end", *studentnames)

def displayRes(*args):
    studentnames = []
    studentresults = {}
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        to_check = sortType[sortby.get()].replace(" ", "").lower()

        sentmsg.set("Displayed students for %s" % (sortType[sortby.get()]))


lbl = ttk.Label(c, text="Display students by assessment type:")
g2 = ttk.Radiobutton(c, text=sortType['summative'], variable=sortby, value='summative')
send = ttk.Button(c, text='Display Results', command=displayRes, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# Grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbl.grid(column=1, row=0, padx=10, pady=5)
g2.grid(column=1, row=2, sticky=W, padx=20)
send.grid(column=2, row=4, sticky=E)
sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
status.grid(column=0, row=6, columnspan=2, sticky=(W,E))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

lbox.bind('<<ListboxSelect>>', showData)
lbox.bind('<Double-1>', displayRes)
root.bind('<Return>', displayRes)

# Colorize alternating lines of the listbox
for i in range(0,len(studentnames),2):
    lbox.itemconfigure(i, background='#f0f0ff')

sortby.set('summative')
sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0)
showData()

root.mainloop()