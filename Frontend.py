from ast import Str
from tkinter import *
import tkinter
from turtle import back

from click import command
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def add_command():
        backend.add(weight.get(),backend.date.today())
        list1.delete(0,END)
        list1.insert(END,weight.get(),backend.date.today())

def delete_command():
    backend.delete_last_entry()




window=Tk()

window.wm_title("Weight Tracker")

canvas=tkinter.Canvas(window, height=150, width=150)
canvas.grid(columnspan=3, rowspan=4)

l1=Label(window, text="Enter Weight (Kg)", height=5)
l1.grid(row=0, column=0)


weight=StringVar()
e1=Entry(window, textvariable=weight)
e1.grid(row=0, column=1)


list1=Listbox(window, height=10, width=45)
list1.grid(row=1, column=0, columnspan=2, rowspan=2)

sb1=Scrollbar(window)
sb1.grid(row=1, column=2, columnspan=1)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=3, column=1, rowspan=1)

b2=Button(window, text="Add Entry", width=12, command=add_command)
b2.grid(row=3, column=0)

b3=Button(window, text="Close", width=12, command=window.destroy)
b3.grid(row=4, column=1)

b4=Button(window, text="Delete Last Entry", width=12, command=delete_command)
b4.grid(row=3, column=2)



window.mainloop()



