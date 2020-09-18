from tkinter import *
from tkinter import messagebox

# Creating the Window
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

# Creating Label and Entry Widgets
label_header = Label(root, text="Registration Form", width=20,font=("bold",30))
label_header.place(relx=0.5, rely=0.08, anchor=CENTER)

label_1 = Label(root, text="Name", width=20,font=("bold",12))
label_1.place(relx=0.4, rely=0.2, anchor=E)
entry_1 = Entry(root, width=20)
entry_1.place(relx=0.6, rely=0.2, anchor=CENTER)

def myClick():
    name = entry_1.get()
    myLabel = Label(root, text = name, padx=20, pady=20)#.grid(row=0, column=0)
    myLabel.pack()

def popupConfirm():
    response = messagebox.askokcancel("Confirm Registration","Do you want to submit your registration?")
    #Label(root,text=response).pack()

    if response == 1:
        root.quit()
        # open visual aid

# def saveUser():
#     text_file = open("registered_users.txt", 'a')
#     text_file.append(.get())
#     text_file.close()

#frame = LabelFrame(root, text = "Registration",padx=100, pady=100)
#frame.pack(padx=10, pady=10)
myButton = Button(root, text="Submit", width=20, command = popupConfirm)
myButton.place(relx=0.5, rely=0.9, anchor=CENTER)
#myButton.pack()

root.mainloop()
