from tkinter import *
from random import *

root = Tk()

root.geometry('1000x600')


def wrap():
    onClick()

def onClick():
    x = randint(50, 950)
    y = randint(50, 550)
    button1.place(x=x, y=y)

def accept():
    endWindow = Toplevel(root)
    endWindow.title(":)")
    endWindow.geometry("500x300")
    Label(endWindow, text = "You finally accept the reality of things!").pack()


#create label
main_label = Label(root, text = "Are you a dumbass?")

#put label on screen
main_label.pack()

#first button
rand1 = randrange(1, 5)
#randpix = random.randrange(10, 50, 5)
button1 = Button(root, text = "No", padx =20, pady =20 , command = wrap)
button1.place(x = 400, y = 100)

button2 = Button(root, text = "Yes", padx =20, pady =20, command = accept)
button2.place(x = 600, y = 100)


root.mainloop()