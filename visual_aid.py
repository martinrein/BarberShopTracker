from tkinter import *
from tkinter import filedialog
import json
import os
import ast

class VisualAid(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.setup_window()

    def setup_window(self):
        self.resizable(width=False, height=False)
        self.geometry('550x700')
        self.title("Barber's Visual Aid")

        # Create Frame Widget
        self.main_frame = Frame(self)

        # Create Button Widget
        self.open_file_button = Button(self.main_frame, text="Click this to select a Text File", command=self.open_file)
        
        # Display the Widgets
        self.open_file_button.place(relx=0.5, rely=0.03, anchor=CENTER)
        self.main_frame.place(height=700, width=550)

    def open_file(self):
        # Create File dialog to find file
        self.filename = filedialog.askopenfilename(title="Please select a file", filetypes=((".txt files", "*.txt"),("all files", "*.*")))

        # Reads the text file and place the content into a variable
        file_schedule = open(self.filename, 'r')
        sched_contents = file_schedule.read()
        self.schedule_dict = ast.literal_eval(sched_contents)
        file_schedule.close()

        # Removes Button Widget on the window
        self.open_file_button.destroy()

        # Display Label Widgets
        self.label_filename = Label(self.main_frame, text=self.filename,font=("bold",10))
        self.label_header = Label(self.main_frame, text="Barber's Schedule", width=25,font=("bold",20),relief=RIDGE)

        # Display the Widgets
        self.label_header.place(relx=0.5, rely=0.05,anchor=CENTER)
        self.label_filename.pack()

        # Display Time and Schedule
        self.display_time_labels()
        self.display_schedule()

    def display_time_labels(self):
        # Create Label Widgets
        label_10am = Label(self.main_frame, text="10:00 AM - 10:30 AM", width=18,font=("bold",12))
        label_10am.place(relx=0.2, rely=0.1,anchor=CENTER)
        label_1030am = Label(self.main_frame, text="10:30 AM - 11:00 AM", width=18,font=("bold",12))
        label_1030am.place(relx=0.2, rely=0.15,anchor=CENTER)
        label_11am = Label(self.main_frame, text="11:00 AM - 11:30 AM", width=18,font=("bold",12))
        label_11am.place(relx=0.2, rely=0.2,anchor=CENTER)
        label_1130am = Label(self.main_frame, text="11:30 AM - 12:00 PM", width=18,font=("bold",12))
        label_1130am.place(relx=0.2, rely=0.25,anchor=CENTER)
        label_12pm = Label(self.main_frame, text="12:00 PM - 12:30 PM", width=18,font=("bold",12))
        label_12pm.place(relx=0.2, rely=0.3,anchor=CENTER)
        label_1230pm = Label(self.main_frame, text="12:30 PM - 1:00 PM", width=18,font=("bold",12))
        label_1230pm.place(relx=0.2, rely=0.35,anchor=CENTER)
        label_1pm = Label(self.main_frame, text="1:00 PM - 1:30 PM", width=18,font=("bold",12))
        label_1pm.place(relx=0.2, rely=0.4,anchor=CENTER)
        label_130pm = Label(self.main_frame, text="1:30 PM - 2:00 PM", width=18,font=("bold",12))
        label_130pm.place(relx=0.2, rely=0.45,anchor=CENTER)
        label_2pm = Label(self.main_frame, text="2:00 PM - 2:30 PM", width=18,font=("bold",12))
        label_2pm.place(relx=0.2, rely=0.5,anchor=CENTER)
        label_230pm = Label(self.main_frame, text="2:30 PM - 3:00 PM", width=18,font=("bold",12))
        label_230pm.place(relx=0.2, rely=0.55,anchor=CENTER)
        label_3pm = Label(self.main_frame, text="3:00 PM - 3:30 PM", width=18,font=("bold",12))
        label_3pm.place(relx=0.2, rely=0.6,anchor=CENTER)
        label_330pm = Label(self.main_frame, text="3:30 PM - 4:00 PM", width=18,font=("bold",12))
        label_330pm.place(relx=0.2, rely=0.65,anchor=CENTER)
        label_4pm = Label(self.main_frame, text="4:00 PM - 4:30 PM", width=18,font=("bold",12))
        label_4pm.place(relx=0.2, rely=0.7,anchor=CENTER)
        label_430pm = Label(self.main_frame, text="4:30 PM - 5:00 PM", width=18,font=("bold",12))
        label_430pm.place(relx=0.2, rely=0.75,anchor=CENTER)
        label_5pm = Label(self.main_frame, text="5:00 PM - 5:30 PM", width=18,font=("bold",12))
        label_5pm.place(relx=0.2, rely=0.8,anchor=CENTER)
        label_530pm = Label(self.main_frame, text="5:30 PM - 6:00 PM", width=18,font=("bold",12))
        label_530pm.place(relx=0.2, rely=0.85,anchor=CENTER)
        label_6pm = Label(self.main_frame, text="6:00 PM - 6:30 PM", width=18,font=("bold",12))
        label_6pm.place(relx=0.2, rely=0.9,anchor=CENTER)
        label_630pm = Label(self.main_frame, text="6:30 PM - 7:00 PM", width=18,font=("bold",12))
        label_630pm.place(relx=0.2, rely=0.95,anchor=CENTER)

    def display_schedule(self):
        # Display schedule of the barber
        if self.schedule_dict["10:00 AM - 10:30 AM"] == "":
            label_1 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_1.place(relx=0.64, rely=0.1,anchor=CENTER)
        else:
            label_1 = Label(self.main_frame, text=self.schedule_dict["10:00 AM - 10:30 AM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_1.place(relx=0.64, rely=0.1,anchor=CENTER)

        if self.schedule_dict["10:30 AM - 11:00 AM"] == "":
            label_2 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_2.place(relx=0.64, rely=0.15,anchor=CENTER)
        else:
            label_2 = Label(self.main_frame, text=self.schedule_dict["10:30 AM - 11:00 AM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_2.place(relx=0.64, rely=0.15,anchor=CENTER)

        if self.schedule_dict["11:00 AM - 11:30 AM"] == "":
            label_3 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_3.place(relx=0.64, rely=0.2,anchor=CENTER)
        else:
            label_3 = Label(self.main_frame, text=self.schedule_dict["11:00 AM - 11:30 AM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_3.place(relx=0.64, rely=0.2,anchor=CENTER)

        if self.schedule_dict["11:30 AM - 12:00 PM"] == "":
            label_4 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_4.place(relx=0.64, rely=0.25,anchor=CENTER)
        else:
            label_4 = Label(self.main_frame, text=self.schedule_dict["11:30 AM - 12:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_4.place(relx=0.64, rely=0.25,anchor=CENTER)

        if self.schedule_dict["12:00 PM - 12:30 PM"] == "":
            label_5 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_5.place(relx=0.64, rely=0.3,anchor=CENTER)
        else:
            label_5 = Label(self.main_frame, text=self.schedule_dict["12:00 PM - 12:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_5.place(relx=0.64, rely=0.3,anchor=CENTER)

        if self.schedule_dict["12:30 PM - 1:00 PM"] == "":
            label_6 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_6.place(relx=0.64, rely=0.35,anchor=CENTER)
        else:
            label_6 = Label(self.main_frame, text=self.schedule_dict["12:30 PM - 1:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_6.place(relx=0.64, rely=0.35,anchor=CENTER)

        if self.schedule_dict["1:00 PM - 1:30 PM"] == "":
            label_7 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_7.place(relx=0.64, rely=0.4,anchor=CENTER)
        else:
            label_7 = Label(self.main_frame, text=self.schedule_dict["1:00 PM - 1:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_7.place(relx=0.64, rely=0.4,anchor=CENTER)

        if self.schedule_dict["1:30 PM - 2:00 PM"] == "":
            label_8 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_8.place(relx=0.64, rely=0.45,anchor=CENTER)
        else:
            label_8 = Label(self.main_frame, text=self.schedule_dict["1:30 PM - 2:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_8.place(relx=0.64, rely=0.45,anchor=CENTER)

        if self.schedule_dict["2:00 PM - 2:30 PM"] == "":
            label_9 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_9.place(relx=0.64, rely=0.5,anchor=CENTER)
        else:
            label_9 = Label(self.main_frame, text=self.schedule_dict["2:00 PM - 2:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_9.place(relx=0.64, rely=0.5,anchor=CENTER)

        if self.schedule_dict["2:30 PM - 3:00 PM"] == "":
            label_10 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_10.place(relx=0.64, rely=0.55,anchor=CENTER)
        else:
            label_10 = Label(self.main_frame, text=self.schedule_dict["2:30 PM - 3:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_10.place(relx=0.64, rely=0.55,anchor=CENTER)

        if self.schedule_dict["3:00 PM - 3:30 PM"] == "":
            label_11 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_11.place(relx=0.64, rely=0.6,anchor=CENTER)
        else:
            label_11 = Label(self.main_frame, text=self.schedule_dict["3:00 PM - 3:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_11.place(relx=0.64, rely=0.6,anchor=CENTER)

        if self.schedule_dict["3:30 PM - 4:00 PM"] == "":
            label_12 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_12.place(relx=0.64, rely=0.65,anchor=CENTER)
        else:
            label_12 = Label(self.main_frame, text=self.schedule_dict["3:30 PM - 4:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_12.place(relx=0.64, rely=0.65,anchor=CENTER)

        if self.schedule_dict["4:00 PM - 4:30 PM"] == "":
            label_13 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_13.place(relx=0.64, rely=0.7,anchor=CENTER)
        else:
            label_13 = Label(self.main_frame, text=self.schedule_dict["4:00 PM - 4:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_13.place(relx=0.64, rely=0.7,anchor=CENTER)

        if self.schedule_dict["4:30 PM - 5:00 PM"] == "":
            label_14 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_14.place(relx=0.64, rely=0.75,anchor=CENTER)
        else:
            label_14 = Label(self.main_frame, text=self.schedule_dict["4:30 PM - 5:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_14.place(relx=0.64, rely=0.75,anchor=CENTER)

        if self.schedule_dict["5:00 PM - 5:30 PM"] == "":
            label_15 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_15.place(relx=0.64, rely=0.8,anchor=CENTER)
        else:
            label_15 = Label(self.main_frame, text=self.schedule_dict["5:00 PM - 5:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_15.place(relx=0.64, rely=0.8,anchor=CENTER)

        if self.schedule_dict["5:30 PM - 6:00 PM"] == "":
            label_16 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_16.place(relx=0.64, rely=0.85,anchor=CENTER)
        else:
            label_16 = Label(self.main_frame, text=self.schedule_dict["5:30 PM - 6:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_16.place(relx=0.64, rely=0.85,anchor=CENTER)

        if self.schedule_dict["6:00 PM - 6:30 PM"] == "":
            label_17 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_17.place(relx=0.64, rely=0.9,anchor=CENTER)
        else:
            label_17 = Label(self.main_frame, text=self.schedule_dict["6:00 PM - 6:30 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_17.place(relx=0.64, rely=0.9,anchor=CENTER)

        if self.schedule_dict["6:30 PM - 7:00 PM"] == "":
            label_18 = Label(self.main_frame, text="n/a", width=40,font=("bold",12),bg= "white",relief=RIDGE)
            label_18.place(relx=0.64, rely=0.95,anchor=CENTER)
        else:
            label_18 = Label(self.main_frame, text=self.schedule_dict["6:30 PM - 7:00 PM"], width=40,font=("bold",12),bg= "lime",relief=RIDGE)
            label_18.place(relx=0.64, rely=0.95,anchor=CENTER)

app = VisualAid()
app.mainloop()
