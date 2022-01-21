from tkinter import *

root = Tk()
root.title("Simple Calculator")

equation = StringVar()
e = Entry (root, textvariable=equation, width = 50, borderwidth = 5)
e.grid(row = 0, column = 0,columnspan=4, padx=10, pady = 10)


expression = ""

def button_click(number):
    global expression
    expression += str(number)
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set(expression)


button_1 = Button(root, text = "1", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF",command=lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(3))
button_mul = Button(root, text = "X", padx=29, pady = 8, borderwidth=3, bg = "#FFFFFF", command = lambda: button_click("*"))
button_4 = Button(root, text = "4", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click(0))
button_add = Button(root, text = "+", padx = 28, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click("+"))
button_equal = Button(root, text = "=", padx = 70, pady = 8, borderwidth=3, bg = "#FFFFFF", command=equal)
button_clear = Button(root, text = "Clear", padx = 60, pady =8, borderwidth=3, bg = "#FFFFFF", command = clear)

button_subt = Button(root, text = "-", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click("-"))
button_divide = Button(root, text = "/", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF", command = lambda: button_click("/"))
button_negate = Button(root, text = "Neg", padx = 22, pady = 8, borderwidth=3, bg = "#FFFFFF", command=lambda: button_click("*(-1)"))
button_dot = Button (root, text = ".", padx = 30, pady = 8, borderwidth=3, bg = "#FFFFFF")



button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_mul.grid(row = 3, column = 3)

button_4.grid(row = 4, column = 0)
button_5.grid(row = 4, column = 1)
button_6.grid(row = 4, column = 2)
button_subt.grid(row = 4, column = 3)

button_7.grid(row = 5, column = 0)
button_8.grid(row = 5, column = 1)
button_9.grid(row = 5, column = 2)
button_add.grid(row = 5, column = 3)

button_0.grid(row = 6, column = 1)
button_negate.grid(row = 6, column = 0)
button_dot.grid(row = 6, column = 2)
button_divide.grid(row = 6, column = 3)

button_clear.grid(row = 7, column = 0, columnspan=2)
button_equal.grid(row = 7, column = 2, columnspan=2)

root.mainloop()