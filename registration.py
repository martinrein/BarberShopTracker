from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration Form", width=20,font=("bold",20))
label_0.place(relx=0.5, rely=0.1, anchor=CENTER)
entry_name = Entry(root, width=20)
entry_name.place(relx=0.5, rely=0.2, anchor=CENTER)
#entry_name.pack()

def myClick():
    name = entry_name.get()
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
#label_name = Label(root, text="hello").grid(row=1, column=0)
myButton = Button(root, text="Submit", width=20, command = popupConfirm)
myButton.place(relx=0.5, rely=0.9, anchor=CENTER)
#myButton.pack()

root.mainloop()

#e.insert(0, "Enter Your Name: ")