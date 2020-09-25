from tkinter import *
from tkinter import filedialog
import json
import os
import ast

# Create the Window
root = Tk()
root.geometry('550x700')
root.title("Barber's Visual Aid")

def open_file():
    """
    This function loads the selected file and display the barber's scheduled appointments.
    """

    root.filename = filedialog.askopenfilename(title="Please select a file", filetypes=((".txt files", "*.txt"),("all files", "*.*")))
    label_filename = Label(root, text=root.filename,font=("bold",10))
    label_filename.pack()

    label_header = Label(root, text="Barber's Schedule", width=25,font=("bold",20),relief=RIDGE)
    label_header.place(relx=0.5, rely=0.05,anchor=CENTER)

    file_schedule = open(root.filename, 'r')
    sched_contents = file_schedule.read()
    schedule_dict = ast.literal_eval(sched_contents)
    file_schedule.close()

    # Removes Button
    open_file_button.destroy()

    if schedule_dict["10:00 AM - 10:30 AM"] == "":
        label_1 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_1.place(relx=0.64, rely=0.1,anchor=CENTER)
    else:
        label_1 = Label(root, text=schedule_dict["10:00 AM - 10:30 AM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_1.place(relx=0.64, rely=0.1,anchor=CENTER)

    if schedule_dict["10:30 AM - 11:00 AM"] == "":
        label_2 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_2.place(relx=0.64, rely=0.15,anchor=CENTER)
    else:
        label_2 = Label(root, text=schedule_dict["10:30 AM - 11:00 AM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_2.place(relx=0.64, rely=0.15,anchor=CENTER)

    if schedule_dict["11:00 AM - 11:30 AM"] == "":
        label_3 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_3.place(relx=0.64, rely=0.2,anchor=CENTER)
    else:
        label_3 = Label(root, text=schedule_dict["11:00 AM - 11:30 AM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_3.place(relx=0.64, rely=0.2,anchor=CENTER)

    if schedule_dict["11:30 AM - 12:00 PM"] == "":
        label_4 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_4.place(relx=0.64, rely=0.25,anchor=CENTER)
    else:
        label_4 = Label(root, text=schedule_dict["11:30 AM - 12:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_4.place(relx=0.64, rely=0.25,anchor=CENTER)

    if schedule_dict["12:00 PM - 12:30 PM"] == "":
        label_5 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_5.place(relx=0.64, rely=0.3,anchor=CENTER)
    else:
        label_5 = Label(root, text=schedule_dict["12:00 PM - 12:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_5.place(relx=0.64, rely=0.3,anchor=CENTER)

    if schedule_dict["12:30 PM - 1:00 PM"] == "":
        label_6 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_6.place(relx=0.64, rely=0.35,anchor=CENTER)
    else:
        label_6 = Label(root, text=schedule_dict["12:30 PM - 1:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_6.place(relx=0.64, rely=0.35,anchor=CENTER)

    if schedule_dict["1:00 PM - 1:30 PM"] == "":
        label_7 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_7.place(relx=0.64, rely=0.4,anchor=CENTER)
    else:
        label_7 = Label(root, text=schedule_dict["1:00 PM - 1:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_7.place(relx=0.64, rely=0.4,anchor=CENTER)

    if schedule_dict["1:30 PM - 2:00 PM"] == "":
        label_8 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_8.place(relx=0.64, rely=0.45,anchor=CENTER)
    else:
        label_8 = Label(root, text=schedule_dict["1:30 PM - 2:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_8.place(relx=0.64, rely=0.45,anchor=CENTER)

    if schedule_dict["2:00 PM - 2:30 PM"] == "":
        label_9 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_9.place(relx=0.64, rely=0.5,anchor=CENTER)
    else:
        label_9 = Label(root, text=schedule_dict["2:00 PM - 2:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_9.place(relx=0.64, rely=0.5,anchor=CENTER)

    if schedule_dict["2:30 PM - 3:00 PM"] == "":
        label_10 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_10.place(relx=0.64, rely=0.55,anchor=CENTER)
    else:
        label_10 = Label(root, text=schedule_dict["2:30 PM - 3:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_10.place(relx=0.64, rely=0.55,anchor=CENTER)

    if schedule_dict["3:00 PM - 3:30 PM"] == "":
        label_11 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_11.place(relx=0.64, rely=0.6,anchor=CENTER)
    else:
        label_11 = Label(root, text=schedule_dict["3:00 PM - 3:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_11.place(relx=0.64, rely=0.6,anchor=CENTER)

    if schedule_dict["3:30 PM - 4:00 PM"] == "":
        label_12 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_12.place(relx=0.64, rely=0.65,anchor=CENTER)
    else:
        label_12 = Label(root, text=schedule_dict["3:30 PM - 4:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_12.place(relx=0.64, rely=0.65,anchor=CENTER)

    if schedule_dict["4:00 PM - 4:30 PM"] == "":
        label_13 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_13.place(relx=0.64, rely=0.7,anchor=CENTER)
    else:
        label_13 = Label(root, text=schedule_dict["4:00 PM - 4:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_13.place(relx=0.64, rely=0.7,anchor=CENTER)

    if schedule_dict["4:30 PM - 5:00 PM"] == "":
        label_14 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_14.place(relx=0.64, rely=0.75,anchor=CENTER)
    else:
        label_14 = Label(root, text=schedule_dict["4:30 PM - 5:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_14.place(relx=0.64, rely=0.75,anchor=CENTER)

    if schedule_dict["5:00 PM - 5:30 PM"] == "":
        label_15 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_15.place(relx=0.64, rely=0.8,anchor=CENTER)
    else:
        label_15 = Label(root, text=schedule_dict["5:00 PM - 5:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_15.place(relx=0.64, rely=0.8,anchor=CENTER)

    if schedule_dict["5:30 PM - 6:00 PM"] == "":
        label_16 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_16.place(relx=0.64, rely=0.85,anchor=CENTER)
    else:
        label_16 = Label(root, text=schedule_dict["5:30 PM - 6:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_16.place(relx=0.64, rely=0.85,anchor=CENTER)

    if schedule_dict["6:00 PM - 6:30 PM"] == "":
        label_17 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_17.place(relx=0.64, rely=0.9,anchor=CENTER)
    else:
        label_17 = Label(root, text=schedule_dict["6:00 PM - 6:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_17.place(relx=0.64, rely=0.9,anchor=CENTER)

    if schedule_dict["6:30 PM - 7:00 PM"] == "":
        label_18 = Label(root, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
        label_18.place(relx=0.64, rely=0.95,anchor=CENTER)
    else:
        label_18 = Label(root, text=schedule_dict["6:30 PM - 7:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
        label_18.place(relx=0.64, rely=0.95,anchor=CENTER)

    label_10am = Label(root, text="10:00 AM - 10:30 AM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.1,anchor=CENTER)
    label_10am = Label(root, text="10:30 AM - 11:00 AM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.15,anchor=CENTER)
    label_10am = Label(root, text="11:00 AM - 11:30 AM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.2,anchor=CENTER)
    label_10am = Label(root, text="11:30 AM - 12:00 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.25,anchor=CENTER)
    label_10am = Label(root, text="12:00 PM - 12:30 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.3,anchor=CENTER)
    label_10am = Label(root, text="12:30 PM - 1:00 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.35,anchor=CENTER)
    label_10am = Label(root, text="1:00 PM - 1:30 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.4,anchor=CENTER)
    label_10am = Label(root, text="1:30 PM - 2:00 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.45,anchor=CENTER)
    label_10am = Label(root, text="2:00 PM - 2:30 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.5,anchor=CENTER)
    label_10am = Label(root, text="2:30 PM - 3:00 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.55,anchor=CENTER)
    label_10am = Label(root, text="3:00 PM - 3:30 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.6,anchor=CENTER)
    label_10am = Label(root, text="3:30 PM - 4:00 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.65,anchor=CENTER)
    label_10am = Label(root, text="4:00 PM - 4:30 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.7,anchor=CENTER)
    label_10am = Label(root, text="4:30 PM - 5:00 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.75,anchor=CENTER)
    label_10am = Label(root, text="5:00 PM - 5:30 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.8,anchor=CENTER)
    label_10am = Label(root, text="5:30 PM - 6:00 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.85,anchor=CENTER)
    label_10am = Label(root, text="6:00 PM - 6:30 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.9,anchor=CENTER)
    label_10am = Label(root, text="6:30 PM - 7:00 PM", width=18,font=("bold",12))
    label_10am.place(relx=0.2, rely=0.95,anchor=CENTER)
        

open_file_button = Button(root, text="Click this to select a Text File", command=open_file)
open_file_button.place(relx=0.5, rely=0.03, anchor=CENTER)

root.mainloop()
