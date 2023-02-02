from tkinter import *
from random import randint

def move_button():
    no_btn.place(x=randint(0, 100), y=randint(0, 100))

def replace_text():
    global text
    lbl.config(text="Knew it")
    yes_btn.destroy()
    no_btn.destroy()

    lbl.grid(ipadx=100, ipady=75)

root = Tk()

root.title("The Test")

root.minsize(200,150)

lbl = Label(text="Are you dumb?")
lbl.grid(ipadx=100, ipady=10)

yes_btn = Button(text="Yes", command=replace_text)
yes_btn.grid()

no_btn = Button(text="No", command=move_button)
no_btn.grid()

root.mainloop()
