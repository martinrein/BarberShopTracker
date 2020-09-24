from tkinter import *
from tkinter import messagebox
import json
import os
import ast

# Create the Window
root = Tk()
root.geometry('500x750')
root.title("CEE Barber Shop")

def select_time():
    if (str(barber_choice.get()) != "-- Select a Barber --") & (str(date_choice.get()) != "-- Select from Available Dates --"):
        time_window = Toplevel()
        time_window.geometry('500x500')
        time_window.title('Select an Appointment')

        # Create Schedule File if the file does not exist yet
        schedule_file_name = date_choice.get() + '_' + barber_choice.get() + '.txt'
        if (os.path.exists('./' + schedule_file_name)) == False:
            schedule_dict = {"10:00 AM":"","10:30 AM":"","11:00 AM":"","11:30 AM":"","12:00 PM":"","12:30 PM":"","1:00 PM":"","1:30 PM":"","2:00 PM":"","2:30 PM":"","3:00 PM":"","3:30 PM":"","4:00 PM":"","4:30 PM":"","5:00 PM":"","5:30 PM":"","6:00 PM":"","6:30 PM":"",}
            with open(schedule_file_name, 'w') as file:
                file.write(json.dumps(schedule_dict))
        
        # Read the file and place on a variable
        file_schedule = open(schedule_file_name, 'r')
        sched_contents = file_schedule.read()
        schedule_dict = ast.literal_eval(sched_contents)
        file_schedule.close()

        # Create Buttons for available slots and slots taken
        if schedule_dict['10:00 AM'] != "":
            button_10am = Button(time_window, text="10:00 AM - 10:30 AM", width=10)#, command = questionnaire)
            button_10am.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            red_10am = Button(time_window, text="10:00 AM - 10:30 AM", width=20,fg='red')#, command = questionnaire)
            red_10am.place(anchor="c", relx=.5, rely=.5)

    else:
        messagebox.showerror("Invalid","Please select a Barber and Date")

def get_customer():
    customer = 'Name: ' + entry_1.get() + '\nContact No.: ' + entry_2.get() + '\nEmail: ' + entry_3.get() + '\nAddress: ' + entry_4.get() + '\nBarber: ' + barber_choice.get() + '\nDate: ' + date_choice.get() + '\nTime: '
    save_to_file(customer)

def get_question():
    answers = '\nQuestion 1-5: ' + str(q1_value.get()) + ', ' + str(q2_value.get()) + ', ' + str(q3_value.get()) + ', ' + str(q4_value.get()) + ', ' + str(q5_value.get()) + '\nQuestion 6-10: ' + str(q6_value.get()) + ', ' + str(q7_value.get()) + ', ' + str(q8_value.get()) + ', ' + str(q9_value.get()) + ', ' + str(q10_value.get())
    save_to_file(answers)

def get_question_stated():
    stated = '\nQuestion 6 Stated: ' + q6_entry.get() + '\nQuestion 7 Stated: ' + q7_entry.get() + '\n\n'
    save_to_file(stated)
    
# Saves the registered user's information to a text file.
def save_to_file(info):
    text_file = open("registered_users.txt", 'a')
    text_file.write(info)
    text_file.close()

def questionnaire():
    # Create Blank Frame
    white_frame.place(in_=frame_register_form, anchor="c", relx=.5, rely=.5)
    
    # Remove unnecessary Widgets
    barber_dropdown.destroy()
    date_dropdown.destroy()
    timeButton.destroy()

    # Create Label Widgets
    label_header = Label(root, text="Questionnaire", width=20,font=("bold",30))
    label_header.place(relx=0.5, rely=0.05, anchor=CENTER)
    label_yes = Label(white_frame, text="YES", width=3,font=("arial bold",12))
    label_yes.place(relx=0.795, rely=0)
    label_no = Label(white_frame, text="NO", width=3,font=("arial bold",12))
    label_no.place(relx=0.895, rely=0)
    label_ifyes_1 = Label(white_frame, text="If YES please state here: ", width=17,font=("bold",12))
    label_ifyes_1.place(relx=0.055, rely=0.52)
    label_ifyes_2 = Label(white_frame, text="If YES please state here: ", width=17,font=("bold",12))
    label_ifyes_2.place(relx=0.055, rely=0.64)

    # Create Question Label Widgets 
    q1 = Label(white_frame, text="1.   Have you been experiencing any colds lately?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q1.place(relx=0.01, rely=0.05)
    q2 = Label(white_frame, text="2.   Have you had a fever lately?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q2.place(relx=0.01, rely=0.13)
    q3 = Label(white_frame, text="3.   Have you been experiencing any cough lately?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q3.place(relx=0.01, rely=0.21)
    q4 = Label(white_frame, text="4.   Have you been experiencing any shortness of breath\n      lately?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q4.place(relx=0.01, rely=0.29)
    q5 = Label(white_frame, text="5.   Have you been experiencing any sore throat lately?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q5.place(relx=0.01, rely=0.37)
    q6 = Label(white_frame, text="6.   Do you have any case of asthma or any other\n      disease?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q6.place(relx=0.01, rely=0.45)
    q7 = Label(white_frame, text="7.   In the past 30 days have you been to any other\n      country?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q7.place(relx=0.01, rely=0.57)
    q8 = Label(white_frame, text="8.   Do you have any senior citizens at home? ", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q8.place(relx=0.01, rely=0.69)
    q9 = Label(white_frame, text="9.   Do you work in any healthcare organization?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q9.place(relx=0.01, rely=0.77)
    q10 = Label(white_frame, text="10. Do you agree to follow the rules and regulations\n       regarding COVID-19 safety and precautions?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    q10.place(relx=0.01, rely=0.85)

    # Place Questionnaire Entry Widgets
    q6_entry.place(relx=0.58, rely=0.541, anchor=CENTER)
    q7_entry.place(relx=0.58, rely=0.661, anchor=CENTER)

    # Create Yes or No Radio Buttons
    Radiobutton(white_frame, variable = q1_value, value = "YES").place(relx=0.8, rely=0.048)
    Radiobutton(white_frame, variable = q1_value, value = "NO").place(relx=0.9, rely=0.048)
    q1_value.set(0)
    Radiobutton(white_frame, variable = q2_value, value = "YES").place(relx=0.8, rely=0.125)
    Radiobutton(white_frame, variable = q2_value, value = "NO").place(relx=0.9, rely=0.125)
    q2_value.set(0)
    Radiobutton(white_frame, variable = q3_value, value = "YES").place(relx=0.8, rely=0.207)
    Radiobutton(white_frame, variable = q3_value, value = "NO").place(relx=0.9, rely=0.207)
    q3_value.set(0)
    Radiobutton(white_frame, variable = q4_value, value = "YES").place(relx=0.8, rely=0.288)
    Radiobutton(white_frame, variable = q4_value, value = "NO").place(relx=0.9, rely=0.288)
    q4_value.set(0)
    Radiobutton(white_frame, variable = q5_value, value = "YES").place(relx=0.8, rely=0.368)
    Radiobutton(white_frame, variable = q5_value, value = "NO").place(relx=0.9, rely=0.368)
    q5_value.set(0)
    Radiobutton(white_frame, variable = q6_value, value = "YES").place(relx=0.8, rely=0.447)
    Radiobutton(white_frame, variable = q6_value, value = "NO").place(relx=0.9, rely=0.447)
    q6_value.set(0)
    Radiobutton(white_frame, variable = q7_value, value = "YES").place(relx=0.8, rely=0.57)
    Radiobutton(white_frame, variable = q7_value, value = "NO").place(relx=0.9, rely=0.57)
    q7_value.set(0)
    Radiobutton(white_frame, variable = q8_value, value = "YES").place(relx=0.8, rely=0.685)
    Radiobutton(white_frame, variable = q8_value, value = "NO").place(relx=0.9, rely=0.685)
    q8_value.set(0)
    Radiobutton(white_frame, variable = q9_value, value = "YES").place(relx=0.8, rely=0.765)
    Radiobutton(white_frame, variable = q9_value, value = "NO").place(relx=0.9, rely=0.765)
    q9_value.set(0)
    Radiobutton(white_frame, variable = q10_value, value = "YES").place(relx=0.8, rely=0.85)
    Radiobutton(white_frame, variable = q10_value, value = "NO").place(relx=0.9, rely=0.85)
    q10_value.set(0)

    submitButton = Button(root, text="Submit", width=10, command = submit_registration)
    submitButton.place(relx=0.5, rely=0.95, anchor=CENTER)

def submit_registration():
    response = messagebox.askokcancel("Confirm Registration","Do you want to submit your registration?")
    
    if response == 1:   # If response is 'OK'
        get_customer()
        get_question()
        get_question_stated()
        root.quit()

# Create Main Frame
frame_register_form = LabelFrame(root, text = " CEE Barber Shop ", pady=50,labelanchor=N, bd=5,font=("bold",20), relief=RIDGE)
frame_register_form.pack(fill="both", expand=True,padx=20, pady=80)
white_frame = Frame(width=440, height=550, background="white")

# Create Registration Label Widgets
label_header = Label(root, text="Registration Form", width=20,font=("bold",30))
label_header.place(relx=0.5, rely=0.05, anchor=CENTER)
label_1 = Label(frame_register_form, text="Name", width=10,font=("bold",12))
label_1.place(relx=0.05, rely=-0.05)
label_2 = Label(frame_register_form, text="Contact No.", width=10,font=("bold",12))
label_2.place(relx=0.09, rely=0.05)
label_3 = Label(frame_register_form, text="Email", width=10,font=("bold",12))
label_3.place(relx=0.05, rely=0.15)
label_4 = Label(frame_register_form, text="Address", width=10,font=("bold",12))
label_4.place(relx=0.07, rely=0.25)
label_5 = Label(frame_register_form, text="Barber", width=10,font=("bold",12))
label_5.place(relx=0.06, rely=0.35)
label_6 = Label(frame_register_form, text="Date", width=10,font=("bold",12))
label_6.place(relx=0.05, rely=0.45)
label_7 = Label(frame_register_form, text="Time", width=10,font=("bold",12))
label_7.place(relx=0.05, rely=0.55)

# Create Registration Entry Widgets
entry_1 = Entry(frame_register_form, width=30)
entry_1.place(relx=0.6, rely=-0.025, anchor=CENTER)
entry_2 = Entry(frame_register_form, width=30)
entry_2.place(relx=0.6, rely=0.075, anchor=CENTER)
entry_3 = Entry(frame_register_form, width=30)
entry_3.place(relx=0.6, rely=0.175, anchor=CENTER)
entry_4 = Entry(frame_register_form, width=30)
entry_4.place(relx=0.6, rely=0.275, anchor=CENTER)
q6_entry = Entry(white_frame, width=19)
q7_entry = Entry(white_frame, width=19)

# Get List of Barbers from text file 'barbers.txt' and create Barber Dropdown Menu
with open('barbers.txt', 'r') as f:
    barbers_list = json.loads(f.read())
barbers_list.insert(0,"-- Select a Barber --")
barber_choice = StringVar()
barber_choice.set(barbers_list[0])
barber_dropdown = OptionMenu(root, barber_choice, *barbers_list)
barber_dropdown.place(relx=0.302, rely=0.42)

# Get List of Available Dates from text file 'open_dates.txt' and create Date Dropdown Menu
with open('open_dates.txt', 'r') as f:
    date_list = json.loads(f.read())
date_list.insert(0,"-- Select from Available Dates --")
date_choice = StringVar()
date_choice.set(date_list[0])
date_dropdown = OptionMenu(root, date_choice, *date_list)
date_dropdown.place(relx=0.302, rely=0.48)

# Set Variables of Questionnaire Answers
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

# Create Buttons
timeButton = Button(root, text="-- Select an Appointment --", width=21, command = select_time)
timeButton.place(relx=0.5, rely=0.559, anchor=CENTER)
nextButton = Button(root, text="Next >>", width=10, command = questionnaire)
nextButton.place(relx=0.5, rely=0.95, anchor=CENTER)

root.mainloop()
