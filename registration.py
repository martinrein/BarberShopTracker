from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()

def myClick():
    name = e.get()
    myLabel = Label(root, text = name)
    myLabel.pack()

myButton = Button(root, text="Submit", command = myClick)
myButton.pack()

root.mainloop()

#e.insert(0, "Enter Your Name: ")