#/bin/bash/python3

from tkinter import *
from PIL import *


calculator = Tk()
calculator.title("Calculator by Simon")

screen = Entry(calculator, width=34, borderwidth=20)
screen.grid(rowspan=1, columnspan=3)

def add_button  (number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))

def add_nr():
    global first_nr
    first_nr = int(screen.get())
    global math
    math = "addition"
    screen.delete(0, END)
    screen.insert(0, str(first_nr) + "+")

def sub_nr():
    global first_nr
    first_nr = int(screen.get())
    global math
    math = "subtraction"
    screen.delete(0, END)
    screen.insert(0, str(first_nr) + "-")

def mult_nr():
    global first_nr
    first_nr = int(screen.get())
    global math
    math = "multiplication"
    screen.delete(0, END)
    screen.insert(0, str(first_nr) + "*")

def div_nr():
    global first_nr
    first_nr = int(screen.get())
    global math
    math = "division"
    screen.delete(0, END)
    screen.insert(0, str(first_nr) + "/")

def solution():
    func = screen.get()
    if math == "addition":
        func_lst = func.split("+")
        solution = first_nr + int(func_lst[-1])
        screen.delete(0, END)
        screen.insert(0, str(solution))
    if math == "subtraction":
        func_lst = func.split("-")
        solution = first_nr - int(func_lst[-1])
        screen.delete(0, END)
        screen.insert(0, str(solution))
    if math == "multiplication":
        func_lst = func.split("*")
        solution = first_nr * int(func_lst[-1])
        screen.delete(0, END)
        screen.insert(0, str(solution))
    if math == "division":
        func_lst = func.split("/")
        solution = float(first_nr) / float(func_lst[-1])
        screen.delete(0, END)
        screen.insert(0, str(solution))

button1 = Button(calculator, text="1", padx= 40, pady= 20, command=lambda: add_button(1)).grid(row=3, column= 2)
button2 = Button(calculator, text="2", padx= 40, pady= 20, command=lambda: add_button(2)).grid(row=3, column= 1)
button3 = Button(calculator, text="3", padx= 40, pady= 20, command=lambda: add_button(3)).grid(row=3, column= 0)

button4 = Button(calculator, text="4", padx= 40, pady= 20, command=lambda: add_button(4)).grid(row=2, column= 2)
button5 = Button(calculator, text="5", padx= 40, pady= 20, command=lambda: add_button(5)).grid(row=2, column= 1)
button6 = Button(calculator, text="6", padx= 40, pady= 20, command=lambda: add_button(6)).grid(row=2, column= 0)

button7 = Button(calculator, text="7", padx= 40, pady= 20, command=lambda: add_button(7)).grid(row=1, column=2)
button8 = Button(calculator, text="8", padx= 40, pady= 20, command=lambda: add_button(8)).grid(row=1, column=1)
button9 = Button(calculator, text="9", padx= 40, pady= 20, command=lambda: add_button(9)).grid(row=1, column=0)

button0 = Button(calculator, text="0", padx= 38, pady= 20, command=lambda: add_button(0)).grid(row=4, column=0)
button_plus = Button(calculator, text="+", padx= 38, pady= 20, command=add_nr).grid(row=5, column=0)
button_sub = Button(calculator, text="-", padx= 38, pady= 20, command=sub_nr).grid(row=6, column=2)
button_mult = Button(calculator, text="*", padx= 38, pady= 20, command=mult_nr).grid(row=6, column=1)
button_div = Button(calculator, text="/", padx= 38, pady= 20, command=div_nr).grid(row=6, column=0)
button_equal = Button(calculator, text="=", padx= 99, pady= 20, command= solution).grid(row=4, column=1, columnspan=2)
button_clear = Button(calculator, text="clear", padx= 88, pady= 20, command= lambda: screen.delete(0, END)).grid(row=5, column=1, columnspan=2)


calculator.mainloop()

