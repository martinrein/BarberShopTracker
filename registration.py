from tkinter import *
from tkinter import messagebox
import json
import os
import ast

class Registration(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.initial_values()
        self.setup_window()

    def initial_values(self):
        """

        """

        # Set Variables for Questionnaire Answers
        q1_value = StringVar()
        q2_value = StringVar()
        q3_value = StringVar()
        q4_value = StringVar()
        q5_value = StringVar()
        q6_value = StringVar()
        q7_value = StringVar()
        q8_value = StringVar()
        q9_value = StringVar()
        q10_value = StringVar()

    def setup_window(self):
        """
        This function creates the initial widgets for the program.
        """

        # Create Window
        self.resizable(width=False, height=False)
        self.geometry('550x650')
        self.title("CEE Barber Shop")

        # Create Frames
        self.main_frame = Frame(self)
        
        label_header = Label(self.main_frame, text="Registration Form", width=20,font=("bold",30))

        self.registration_setup()

        # Place Frame
        self.main_frame.place(height=650, width=550)
        label_header.place(relx=0.5, rely=0.05, anchor=CENTER)
        

        #white_frame = Frame(width=440, height=550, background="white")

        # Create Buttons
        # timeButton = Button(root, text="-- Select an Appointment --", width=21, command = select_time)
        # nextButton = Button(root, text="Next >>", width=10, command = confirm_registration)
        # timeButton.place(relx=0.5, rely=0.559, anchor=CENTER)
        # nextButton.place(relx=0.5, rely=0.95, anchor=CENTER)

    def registration_setup(self):

        # Create Frame for Registration Form
        self.frame_register_form = LabelFrame(self.main_frame, text = " CEE Barber Shop ", \
            pady=50,labelanchor=N,bd=5,font=("bold",20), relief=RIDGE)

        # Create Registration Label Widgets
        label_1 = Label(self.frame_register_form, text="Name", width=10,font=("bold",12))
        label_2 = Label(self.frame_register_form, text="Contact No.", width=10,font=("bold",12))
        label_3 = Label(self.frame_register_form, text="Email", width=10,font=("bold",12))
        label_4 = Label(self.frame_register_form, text="Address", width=10,font=("bold",12))
        label_5 = Label(self.frame_register_form, text="Barber", width=10,font=("bold",12))
        label_6 = Label(self.frame_register_form, text="Date", width=10,font=("bold",12))
        label_7 = Label(self.frame_register_form, text="Time", width=10,font=("bold",12))

        # Create Registration Entry Widgets
        entry_1 = Entry(self.frame_register_form, width=30)
        entry_2 = Entry(self.frame_register_form, width=30)
        entry_3 = Entry(self.frame_register_form, width=30)
        entry_4 = Entry(self.frame_register_form, width=30)

        # Get List of Barbers from text file 'barbers.txt' and create Barber Dropdown Menu
        with open('barbers.txt', 'r') as f:
            barbers_list = json.loads(f.read())
        barbers_list.insert(0,"-- Select a Barber --")
        barber_choice = StringVar()
        barber_choice.set(barbers_list[0])
        barber_dropdown = OptionMenu(self.frame_register_form, barber_choice, *barbers_list)

        # Get List of Available Dates from text file 'open_dates.txt' and create Date Dropdown Menu
        with open('open_dates.txt', 'r') as f:
            date_list = json.loads(f.read())
        date_list.insert(0,"-- Select from Available Dates --")
        date_choice = StringVar()
        date_choice.set(date_list[0])
        date_dropdown = OptionMenu(self.frame_register_form, date_choice, *date_list)

        # Place Widgets on the Frame
        self.frame_register_form.pack(fill="both", expand=True,padx=20, pady=80)
        label_1.place(relx=0.05, rely=-0.05)
        label_2.place(relx=0.09, rely=0.05)
        label_3.place(relx=0.05, rely=0.15)
        label_4.place(relx=0.07, rely=0.25)
        label_5.place(relx=0.06, rely=0.35)
        label_6.place(relx=0.05, rely=0.45)
        label_7.place(relx=0.05, rely=0.55)
        entry_1.place(relx=0.6, rely=-0.025, anchor=CENTER)
        entry_2.place(relx=0.6, rely=0.075, anchor=CENTER)
        entry_3.place(relx=0.6, rely=0.175, anchor=CENTER)
        entry_4.place(relx=0.6, rely=0.275, anchor=CENTER)
        barber_dropdown.place(relx=0.315, rely=0.345)
        date_dropdown.place(relx=0.315, rely=0.445)

app = Registration()
app.mainloop()
