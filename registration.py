from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Registration")

e = Entry(root, width=100)
e.pack()

def myClick():
    name = e.get()
    myLabel = Label(root, text = name, padx=20, pady=20)#.grid(row=0, column=0)
    myLabel.pack()

def popupConfirm():
    response = messagebox.askokcancel("Confirm Registration","Do you want to submit your registration?")
    Label(root,text=response).pack()

    if response == 1:
        root.quit()

#frame = LabelFrame(root, text = "Registration",padx=100, pady=100)
#frame.pack(padx=10, pady=10)
#label_name = Label(root, text="hello").grid(row=1, column=0)
myButton = Button(root, text="Submit", command = popupConfirm)
myButton.pack()

root.mainloop()

#e.insert(0, "Enter Your Name: ")