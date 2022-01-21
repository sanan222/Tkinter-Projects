from email.mime import image
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My project')
root.iconbitmap('D:\Python Projects\icons\gear.ico')

my_img1 = ImageTk.PhotoImage(Image.open("D:\Python Projects\images\istanbul1.jfif"))
my_img2 = ImageTk.PhotoImage(Image.open("D:\Python Projects\images\istanbul2.jfif"))
my_img3 = ImageTk.PhotoImage(Image.open("D:\Python Projects\images\istanbul3.jfif"))
my_img4 = ImageTk.PhotoImage(Image.open("D:\Python Projects\images\istanbul4.jfif"))
my_img5 = ImageTk.PhotoImage(Image.open("D:\Python Projects\images\istanbul5.jfif"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)



def forward(row_number):
    global my_label
    global button_forward
    global button_back


    my_label.grid_forget()
    my_label=Label(image = image_list[row_number-1])

    button_back = Button(root, text = "<<", command = lambda: back(row_number-1))
    button_forward = Button(root, text = ">>", command = lambda: forward(row_number+1))

    if row_number == 5:
        button_forward["state"] = "disabled"

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)
    

def back(row_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image = image_list[row_number - 1])

    button_back = Button(root, text = "<<", command = lambda: back(row_number-1))
    button_forward = Button(root, text = ">>", command = lambda: forward(row_number+1))

    
    if row_number == 0:
        button_back["state"] = "disabled"

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

button_back = Button(root, text = "<<", command =back, state=DISABLED)
button_exit = Button(root, text = "Exit Program", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)




root.mainloop()
