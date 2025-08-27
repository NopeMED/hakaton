import tkinter
from tkinter import *

root = Tk()

root.title("Memorial Page")
root.geometry('1600x900')

c = Canvas(root, bg = "#e8dab2", width=1600, height=900)
person = PhotoImage(file="person.PNG")
new_image = person.subsample(2, 2)
image_label = tkinter.Label(root, image=new_image)

c.pack()

text_var = tkinter.StringVar()
text_var.set("Name\nLastname")
label = tkinter.Label(c,
                 textvariable=text_var,
                 anchor=tkinter.W,
                 bg="#e8dab2",
                 height=3,
                 width=30,
                 bd=3,
                 font=("Arial", 16, "bold"),
                 cursor="hand2",
                 fg="black",
                 padx=15,
                 pady=15,
                 wraplength=250
                )


label.pack()
image_label.pack()



















# Execute Tkinter
root.mainloop()