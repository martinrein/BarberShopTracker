from tkinter import *

root = Tk()
root.title("Registration")

e = Entry(root, width=50)
e.pack()

def myClick():
    name = e.get()
    myLabel = Label(root, text = name).grid(row=1, column=0)
    myLabel.pack()

#label_name = Label(root, text="hello").grid(row=1, column=0)
myButton = Button(root, text="Submit", command = myClick)
myButton.pack()

root.mainloop()

#e.insert(0, "Enter Your Name: ")