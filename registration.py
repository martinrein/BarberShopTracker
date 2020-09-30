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

        self.barber_choice = StringVar()
        self.date_choice = StringVar()

        # Set Variables for Questionnaire Answers
        self.q1_value = StringVar()
        self.q2_value = StringVar()
        self.q3_value = StringVar()
        self.q4_value = StringVar()
        self.q5_value = StringVar()
        self.q6_value = StringVar()
        self.q7_value = StringVar()
        self.q8_value = StringVar()
        self.q9_value = StringVar()
        self.q10_value = StringVar()

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
        
        # Create Button
        nextButton = Button(self.main_frame, text="Next >>", width=10, command = self.confirm_registration)
        nextButton.place(relx=0.5, rely=0.94, anchor=CENTER)

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
        self.entry_1 = Entry(self.frame_register_form, width=30)
        self.entry_2 = Entry(self.frame_register_form, width=30)
        self.entry_3 = Entry(self.frame_register_form, width=30)
        self.entry_4 = Entry(self.frame_register_form, width=30)

        # Get List of Barbers from text file 'barbers.txt' and create Barber Dropdown Menu
        with open('barbers.txt', 'r') as f:
            barbers_list = json.loads(f.read())
        barbers_list.insert(0,"-- Select a Barber --")
        self.barber_choice.set(barbers_list[0])
        barber_dropdown = OptionMenu(self.frame_register_form, self.barber_choice, *barbers_list)

        # Get List of Available Dates from text file 'open_dates.txt' and create Date Dropdown Menu
        with open('open_dates.txt', 'r') as f:
            date_list = json.loads(f.read())
        date_list.insert(0,"-- Select from Available Dates --")
        self.date_choice.set(date_list[0])
        date_dropdown = OptionMenu(self.frame_register_form, self.date_choice, *date_list)

        timeButton = Button(self.frame_register_form, text="-- Select an Appointment --", width=21, command = self.select_time)

        # Place Widgets on the Frame
        self.frame_register_form.pack(fill="both", expand=True,padx=20, pady=80)
        label_1.place(relx=0.05, rely=-0.05)
        label_2.place(relx=0.09, rely=0.05)
        label_3.place(relx=0.05, rely=0.15)
        label_4.place(relx=0.07, rely=0.25)
        label_5.place(relx=0.06, rely=0.35)
        label_6.place(relx=0.05, rely=0.45)
        label_7.place(relx=0.05, rely=0.55)
        self.entry_1.place(relx=0.6, rely=-0.025, anchor=CENTER)
        self.entry_2.place(relx=0.6, rely=0.075, anchor=CENTER)
        self.entry_3.place(relx=0.6, rely=0.175, anchor=CENTER)
        self.entry_4.place(relx=0.6, rely=0.275, anchor=CENTER)
        barber_dropdown.place(relx=0.315, rely=0.345)
        date_dropdown.place(relx=0.315, rely=0.445)
        timeButton.place(relx=0.51, rely=0.58, anchor=CENTER)

    def select_time(self):
        """
        This function asks the user to select a time slot to schedule their appointment.
        """

        if (str(self.barber_choice.get()) != "-- Select a Barber --") & \
            (str(self.date_choice.get()) != "-- Select from Available Dates --"):
            
            self.time_window = Toplevel()
            self.time_window.geometry('250x550')
            self.time_window.title('Select an Appointment')

            # Create Schedule File if the file does not exist yet
            schedule_file_name = self.date_choice.get() + ' - ' + self.barber_choice.get() + '.txt'
            if (os.path.exists('./' + schedule_file_name)) == False:
                schedule_dict = {"10:00 AM - 10:30 AM":"","10:30 AM - 11:00 AM":"",\
                    "11:00 AM - 11:30 AM":"","11:30 AM - 12:00 PM":"","12:00 PM - 12:30 PM":"",\
                        "12:30 PM - 1:00 PM":"","1:00 PM - 1:30 PM":"","1:30 PM - 2:00 PM":"",\
                            "2:00 PM - 2:30 PM":"","2:30 PM - 3:00 PM":"","3:00 PM - 3:30 PM":"",\
                                "3:30 PM - 4:00 PM":"","4:00 PM - 4:30 PM":"","4:30 PM - 5:00 PM":"",\
                                    "5:00 PM - 5:30 PM":"","5:30 PM - 6:00 PM":"","6:00 PM - 6:30 PM":"",\
                                        "6:30 PM - 7:00 PM":""}
                with open(schedule_file_name, 'w') as file:
                    file.write(json.dumps(schedule_dict))
            
            # Read the file and place on a variable
            file_schedule = open(schedule_file_name, 'r')
            sched_contents = file_schedule.read()
            schedule_dict = ast.literal_eval(sched_contents)
            file_schedule.close()

            # Create Buttons for available slots and slots taken
            if schedule_dict['10:00 AM - 10:30 AM'] == "":
                button_1000am = Button(self.time_window, text="10:00 AM - 10:30 AM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_1000am))
                button_1000am.place(relx=0.5, rely=0.1, anchor=CENTER)
            else:
                red_1000am = Button(self.time_window, text="10:00 AM - 10:30 AM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_1000am.place(anchor="c", relx=0.5, rely=0.1)

            if schedule_dict['10:30 AM - 11:00 AM'] == "":
                button_1030am = Button(self.time_window, text="10:30 AM - 11:00 AM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_1030am))
                button_1030am.place(relx=0.5, rely=0.15, anchor=CENTER)
            else:
                red_1030am = Button(self.time_window, text="10:30 AM - 11:00 AM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_1030am.place(anchor="c", relx=0.5, rely=0.15)

            if schedule_dict['11:00 AM - 11:30 AM'] == "":
                button_1100am = Button(self.time_window, text="11:00 AM - 11:30 AM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_1100am))
                button_1100am.place(relx=0.5, rely=0.2, anchor=CENTER)
            else:
                red_1100am = Button(self.time_window, text="11:00 AM - 11:30 AM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_1100am.place(anchor="c", relx=0.5, rely=0.2)
            
            if schedule_dict['11:30 AM - 12:00 PM'] == "":
                button_1130am = Button(self.time_window, text="11:30 AM - 12:00 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_1130am))
                button_1130am.place(relx=0.5, rely=0.25, anchor=CENTER)
            else:
                red_1130am = Button(self.time_window, text="11:30 AM - 12:00 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_1130am.place(anchor="c", relx=0.5, rely=0.25)

            if schedule_dict['12:00 PM - 12:30 PM'] == "":
                button_1200pm = Button(self.time_window, text="12:00 PM - 12:30 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_1200pm))
                button_1200pm.place(relx=0.5, rely=0.3, anchor=CENTER)
            else:
                red_1200pm = Button(self.time_window, text="12:00 PM - 12:30 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_1200pm.place(anchor="c", relx=0.5, rely=0.3)
    
            if schedule_dict['12:30 PM - 1:00 PM'] == "":
                button_1230pm = Button(self.time_window, text="12:30 PM - 1:00 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_1230pm))
                button_1230pm.place(relx=0.5, rely=0.35, anchor=CENTER)
            else:
                red_1230pm = Button(self.time_window, text="12:30 PM - 1:00 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_1230pm.place(anchor="c", relx=0.5, rely=0.35)

            if schedule_dict['1:00 PM - 1:30 PM'] == "":
                button_100pm = Button(self.time_window, text="1:00 PM - 1:30 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_100pm))
                button_100pm.place(relx=0.5, rely=0.4, anchor=CENTER)
            else:
                red_100pm = Button(self.time_window, text="1:00 PM - 1:30 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_100pm.place(anchor="c", relx=0.5, rely=0.4)

            if schedule_dict['1:30 PM - 2:00 PM'] == "":
                button_130pm = Button(self.time_window, text="1:30 PM - 2:00 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_130pm))
                button_130pm.place(relx=0.5, rely=0.45, anchor=CENTER)
            else:
                red_130pm = Button(self.time_window, text="1:30 PM - 2:00 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_130pm.place(anchor="c", relx=0.5, rely=0.45)

            if schedule_dict['2:00 PM - 2:30 PM'] == "":
                button_200pm = Button(self.time_window, text="2:00 PM - 2:30 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_200pm))
                button_200pm.place(relx=0.5, rely=0.5, anchor=CENTER)
            else:
                red_200pm = Button(self.time_window, text="2:00 PM - 2:30 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_200pm.place(anchor="c", relx=0.5, rely=0.5)

            if schedule_dict['2:30 PM - 3:00 PM'] == "":
                button_230pm = Button(self.time_window, text="2:30 PM - 3:00 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_230pm))
                button_230pm.place(relx=0.5, rely=0.55, anchor=CENTER)
            else:
                red_230pm = Button(self.time_window, text="2:30 PM - 3:00 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_230pm.place(anchor="c", relx=0.5, rely=0.55)

            if schedule_dict['3:00 PM - 3:30 PM'] == "":
                button_300pm = Button(self.time_window, text="3:00 PM - 3:30 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_300pm))
                button_300pm.place(relx=0.5, rely=0.6, anchor=CENTER)
            else:
                red_300pm = Button(self.time_window, text="3:00 PM - 3:30 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_300pm.place(anchor="c", relx=0.5, rely=0.6)

            if schedule_dict['3:30 PM - 4:00 PM'] == "":
                button_330pm = Button(self.time_window, text="3:30 PM - 4:00 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_330pm))
                button_330pm.place(relx=0.5, rely=0.65, anchor=CENTER)
            else:
                red_330pm = Button(self.time_window, text="3:30 PM - 4:00 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_330pm.place(anchor="c", relx=0.5, rely=0.65)

            if schedule_dict['4:00 PM - 4:30 PM'] == "":
                button_400pm = Button(self.time_window, text="4:00 PM - 4:30 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_400pm))
                button_400pm.place(relx=0.5, rely=0.7, anchor=CENTER)
            else:
                red_400pm = Button(self.time_window, text="4:00 PM - 4:30 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_400pm.place(anchor="c", relx=0.5, rely=0.7)

            if schedule_dict['4:30 PM - 5:00 PM'] == "":
                button_430pm = Button(self.time_window, text="4:30 PM - 5:00 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_430pm))
                button_430pm.place(relx=0.5, rely=0.75, anchor=CENTER)
            else:
                red_430pm = Button(self.time_window, text="4:30 PM - 5:00 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_430pm.place(anchor="c", relx=0.5, rely=0.75)

            if schedule_dict['5:00 PM - 5:30 PM'] == "":
                button_500pm = Button(self.time_window, text="5:00 PM - 5:30 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_500pm))
                button_500pm.place(relx=0.5, rely=0.8, anchor=CENTER)
            else:
                red_500pm = Button(self.time_window, text="5:00 PM - 5:30 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_500pm.place(anchor="c", relx=0.5, rely=0.8)
            
            if schedule_dict['5:30 PM - 6:00 PM'] == "":
                button_530pm = Button(self.time_window, text="5:30 PM - 6:00 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_530pm))
                button_530pm.place(relx=0.5, rely=0.85, anchor=CENTER)
            else:
                red_530pm = Button(self.time_window, text="5:30 PM - 6:00 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_530pm.place(anchor="c", relx=0.5, rely=0.85)

            if schedule_dict['6:00 PM - 6:30 PM'] == "":
                button_600pm = Button(self.time_window, text="6:00 PM - 6:30 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_600pm))
                button_600pm.place(relx=0.5, rely=0.9, anchor=CENTER)
            else:
                red_600pm = Button(self.time_window, text="6:00 PM - 6:30 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_600pm.place(anchor="c", relx=0.5, rely=0.9)

            if schedule_dict['6:30 PM - 7:00 PM'] == "":
                button_630pm = Button(self.time_window, text="6:30 PM - 7:00 PM",height=1,width=20,\
                    fg="green", command = lambda: self.submit_time(button_630pm))
                button_630pm.place(relx=0.5, rely=0.95, anchor=CENTER)
            else:
                red_630pm = Button(self.time_window, text="6:30 PM - 7:00 PM",height=1,width=20,\
                    fg='red', command = self.time_taken)
                red_630pm.place(anchor="c", relx=0.5, rely=0.95)

        else:
            messagebox.showerror("Invalid","Please select a Barber and Date")

    def submit_time(self, button):
        """
        This function asks the user to confirm their time slot choice.
        """

        self.timeslot_str = button["text"]
        selected_time = messagebox.askokcancel("Confirm Time Slot","You selected "+ \
            self.timeslot_str +".\n\nDo you want to schedule this time slot?")

        # Display the selected time slot on the main window
        if selected_time == 1:
            self.label_time = Label(self.main_frame, text="> Selected Time: " + self.timeslot_str, width=30,font=("bold",12))
            self.label_time.place(relx=0.3, rely=0.6)
            self.time_window.destroy()

    def time_taken(self):
        """
        This function outputs an error message. It would ask the user to select another time slot.
        """

        messagebox.showerror("Slot Taken", "This time slot has been taken. Please select another time slot.")

    def confirm_registration(self):
        """
        This function asks the user to view and confirm their inputs. If the user confirms, the 
        questionnaire form would appear.
        """

        confirmation = messagebox.askokcancel("Confirm Registration","Name: " + self.entry_1.get() + \
            "\nContact No.: " + self.entry_2.get() + "\nEmail: " + self.entry_3.get() + "\nAddress: " + \
                self.entry_4.get() + "\nBarber: " + self.barber_choice.get() + "\nDate: " + \
                    self.date_choice.get() + "\nTime: " + self.timeslot_str)

        if confirmation == 1:   
            self.questionnaire()

    def questionnaire(self):
        """
        This function creates and display a questionnaire form. The form consists 10 questions 
        that will be answered by using radiobuttons of 'Yes' and 'No'.
        """

        # Create Blank Frame
        self.questionnaire_frame.place(in_=self.main_frame, anchor="c", relx=.5, rely=.5)
        #white_frame = Frame(width=440, height=550, background="white")
        
        # Remove unnecessary Widgets
        self.frame_register_form.destroy()
        # barber_dropdown.destroy()
        # date_dropdown.destroy()
        # timeButton.destroy()
        # label_time.destroy()

        # Create Label Widgets
        label_header = Label(self.main_frame, text="Questionnaire", width=20,font=("bold",30))
        label_header.place(relx=0.5, rely=0.05, anchor=CENTER)
        label_yes = Label(self.questionnaire_frame, text="YES", width=3,font=("arial bold",12))
        label_yes.place(relx=0.795, rely=0)
        label_no = Label(self.questionnaire_frame, text="NO", width=3,font=("arial bold",12))
        label_no.place(relx=0.895, rely=0)
        label_ifyes_1 = Label(self.questionnaire_frame, text="If YES please state here: ", width=17,font=("bold",12))
        label_ifyes_1.place(relx=0.055, rely=0.52)
        label_ifyes_2 = Label(self.questionnaire_frame, text="If YES please state here: ", width=17,font=("bold",12))
        label_ifyes_2.place(relx=0.055, rely=0.64)

        # Create Question Label Widgets 
        q1 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="1.   Have you been experiencing any colds lately?")
        q2 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="2.   Have you had a fever lately?")
        q3 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="3.   Have you been experiencing any cough lately?")
        q4 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="4.   Have you been experiencing any shortness of breath\n      lately?")
        q5 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="5.   Have you been experiencing any sore throat lately?")
        q6 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="6.   Do you have any case of asthma or any other\n      disease?")
        q7 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="7.   In the past 30 days have you been to any other\n      country?")
        q8 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="8.   Do you have any senior citizens at home? ")
        q9 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="9.   Do you work in any healthcare organization?")
        q10 = Label(self.questionnaire_frame, width=40, font=("bold",12), anchor=W, justify=LEFT,\
            text="10. Do you agree to follow the rules and regulations\n       regarding COVID-19 safety and precautions?")

        self.q6_entry = Entry(self.questionnaire_frame, width=19)
        self.q7_entry = Entry(self.questionnaire_frame, width=19)

        # Place Questionnaire Widgets
        q1.place(relx=0.01, rely=0.05)
        q2.place(relx=0.01, rely=0.13)
        q3.place(relx=0.01, rely=0.21)
        q4.place(relx=0.01, rely=0.29)
        q5.place(relx=0.01, rely=0.37)
        q6.place(relx=0.01, rely=0.45)
        q7.place(relx=0.01, rely=0.57)
        q8.place(relx=0.01, rely=0.69)
        q9.place(relx=0.01, rely=0.77)
        q10.place(relx=0.01, rely=0.85)

        self.q6_entry.place(relx=0.58, rely=0.541, anchor=CENTER)
        self.q7_entry.place(relx=0.58, rely=0.661, anchor=CENTER)

        # Create Yes or No Radio Buttons
        Radiobutton(self.questionnaire_frame, variable = self.q1_value, value = "YES").place(relx=0.8, rely=0.048)
        Radiobutton(self.questionnaire_frame, variable = self.q1_value, value = "NO").place(relx=0.9, rely=0.048)
        self.q1_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q2_value, value = "YES").place(relx=0.8, rely=0.125)
        Radiobutton(self.questionnaire_frame, variable = self.q2_value, value = "NO").place(relx=0.9, rely=0.125)
        self.q2_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q3_value, value = "YES").place(relx=0.8, rely=0.207)
        Radiobutton(self.questionnaire_frame, variable = self.q3_value, value = "NO").place(relx=0.9, rely=0.207)
        self.q3_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q4_value, value = "YES").place(relx=0.8, rely=0.288)
        Radiobutton(self.questionnaire_frame, variable = self.q4_value, value = "NO").place(relx=0.9, rely=0.288)
        self.q4_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q5_value, value = "YES").place(relx=0.8, rely=0.368)
        Radiobutton(self.questionnaire_frame, variable = self.q5_value, value = "NO").place(relx=0.9, rely=0.368)
        self.q5_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q6_value, value = "YES").place(relx=0.8, rely=0.447)
        Radiobutton(self.questionnaire_frame, variable = self.q6_value, value = "NO").place(relx=0.9, rely=0.447)
        self.q6_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q7_value, value = "YES").place(relx=0.8, rely=0.57)
        Radiobutton(self.questionnaire_frame, variable = self.q7_value, value = "NO").place(relx=0.9, rely=0.57)
        self.q7_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q8_value, value = "YES").place(relx=0.8, rely=0.685)
        Radiobutton(self.questionnaire_frame, variable = self.q8_value, value = "NO").place(relx=0.9, rely=0.685)
        self.q8_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q9_value, value = "YES").place(relx=0.8, rely=0.765)
        Radiobutton(self.questionnaire_frame, variable = self.q9_value, value = "NO").place(relx=0.9, rely=0.765)
        self.q9_value.set(0)
        Radiobutton(self.questionnaire_frame, variable = self.q10_value, value = "YES").place(relx=0.8, rely=0.85)
        Radiobutton(self.questionnaire_frame, variable = self.q10_value, value = "NO").place(relx=0.9, rely=0.85)
        self.q10_value.set(0)

        # Create Submit Button
        submitButton = Button(self.main_frame, text="Submit", width=10, command = self.submit_registration)
        submitButton.place(relx=0.5, rely=0.95, anchor=CENTER)

    def get_customer(self):
        """
        This function gets all inputs from the registration form. Then it calls a function to save 
        these information into a text file.
        """

        customer = 'Name: ' + self.entry_1.get() + '\nContact No.: ' + self.entry_2.get() + '\nEmail: ' + \
            self.entry_3.get() + '\nAddress: ' + self.entry_4.get() + '\nBarber: ' + \
                self.barber_choice.get() + '\nDate: ' + self.date_choice.get() + '\nTime: ' + \
                    self.timeslot_str
        self.save_to_file(customer)

    def get_question(self):
        """
        This function gets the radiobutton answers from the questionnaire form. Then it calls a function 
        to save these information into a text file.
        """

        answers = '\nQuestion 1-5: ' + str(self.q1_value.get()) + ', ' + str(self.q2_value.get()) + ', ' + \
            str(self.q3_value.get()) + ', ' + str(self.q4_value.get()) + ', ' + str(self.q5_value.get()) + \
                '\nQuestion 6-10: ' + str(self.q6_value.get()) + ', ' + str(self.q7_value.get()) + ', ' + \
                    str(self.q8_value.get()) + ', ' + str(self.q9_value.get()) + ', ' + str(self.q10_value.get())
        self.save_to_file(answers)

    def get_question_stated(self):
        """
        This function gets the answer from question 6 and 7 from the questionnaire form. 
        Then it calls a function to save these information into a text file.
        """

        stated = '\nQuestion 6 Stated: ' + self.q6_entry.get() + '\nQuestion 7 Stated: ' + self.q7_entry.get() + '\n\n'
        self.save_to_file(stated)
        
    def save_to_file(self, info):
        """
        This function saves the registered user's information into a text file.
        """

        text_file = open("registered_users.txt", 'a')
        text_file.write(info)
        text_file.close()

    def submit_registration(self):
        """
        This function asks the user to confirm their registration. If the response is 'OK', it saves 
        all inputs of the user into a text file. Then it automatically exits the program.
        """

        response = messagebox.askokcancel("Confirm Registration","Do you want to submit your registration?")

        if response == 1:   
            self.get_customer()
            self.get_question()
            self.get_question_stated()

            # Read the file and place on a variable
            schedule_file_name = self.date_choice.get() + ' - ' + self.barber_choice.get() + '.txt'
            file_schedule = open(schedule_file_name, 'r')
            sched_contents = file_schedule.read()
            schedule_dict = ast.literal_eval(sched_contents)
            file_schedule.close()

            # Places the selected time slot into the file
            schedule_dict[self.timeslot_str] = self.entry_1.get() + ' - ' + self.entry_2.get()
            with open(schedule_file_name, 'w') as file:
                file.write(json.dumps(schedule_dict))

            self.quit()

app = Registration()
app.mainloop()
