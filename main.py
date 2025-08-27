import tkinter
from tkinter import *

root = Tk()

root.title("Memorial Page")
root.geometry('1600x900')

c = Canvas(root, bg = "#e8dab2", width=1600, height=900)
person = PhotoImage(file="person.PNG")
image_label = tkinter.Label(root, image=person)
image_label.pack()
c.pack()

















# Execute Tkinter
root.mainloop()