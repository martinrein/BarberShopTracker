from tkinter import *
from tkinter import messagebox

# Creating the Window
root = Tk()
root.geometry('500x750')
root.title("CEE Barber Shop")

# Creating Label and Entry Widgets
label_header = Label(root, text="Registration Form", width=20,font=("bold",30))
label_header.place(relx=0.5, rely=0.05, anchor=CENTER)

frame_register_form = LabelFrame(root, text = " CEE Barber Shop ", pady=50,labelanchor=N, bd=5,font=("bold",20), relief=RIDGE)
#frame_register_form.place(relx=0.5, rely=0.2, anchor=CENTER,width=400)
frame_register_form.pack(fill="both", expand=True,padx=20, pady=80)

label_1 = Label(frame_register_form, text="Name", width=10,font=("bold",12))
label_1.place(relx=0.05, rely=-0.05)

# label_2 = Label(frame_register_form, text="Date", width=20,font=("bold",12))
# label_2.

# label_3 = Label(frame_register_form, text="Contact No.", width=20,font=("bold",12))
# label_3.

# label_4 = Label(frame_register_form, text="Email", width=20,font=("bold",12))
# label_4.

# label_5 = Label(frame_register_form, text="Address", width=20,font=("bold",12))
# label_5.

#entry_1 = Entry(frame_register_form, width=10)
#entry_1.place(relx=0.8, rely=0.2, anchor=CENTER)
#entry_1.pack()


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

myButton = Button(root, text="Submit", width=20, command = popupConfirm)
myButton.place(relx=0.5, rely=0.95, anchor=CENTER)
#myButton.pack()

root.mainloop()
