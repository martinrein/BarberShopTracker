from tkinter import *
from tkinter import messagebox

# Create the Window
root = Tk()
root.geometry('500x750')
root.title("CEE Barber Shop")

# Create Main Frame
frame_register_form = LabelFrame(root, text = " CEE Barber Shop ", pady=50,labelanchor=N, bd=5,font=("bold",20), relief=RIDGE)
frame_register_form.pack(fill="both", expand=True,padx=20, pady=80)

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
# label_5 = Label(frame_register_form, text="Barber", width=10,font=("bold",12))
# label_5.place(relx=0.06, rely=0.35)
# label_6 = Label(frame_register_form, text="Date", width=10,font=("bold",12))
# label_6.place(relx=0.05, rely=0.45)

# Create Registration Entry Widgets
entry_1 = Entry(frame_register_form, width=30)
entry_1.place(relx=0.6, rely=-0.025, anchor=CENTER)
entry_2 = Entry(frame_register_form, width=30)
entry_2.place(relx=0.6, rely=0.075, anchor=CENTER)
entry_3 = Entry(frame_register_form, width=30)
entry_3.place(relx=0.6, rely=0.175, anchor=CENTER)
entry_4 = Entry(frame_register_form, width=30)
entry_4.place(relx=0.6, rely=0.275, anchor=CENTER)

def get_customer():
    customer = 'Name: ' + entry_1.get() + '\nContact No.: ' + entry_2.get() + '\nEmail: ' + entry_3.get() + '\nAddress: ' + entry_4.get() + '\n\n'
    save_to_file(customer)

# Saves the registered user's information to a text file.
def save_to_file(customer):
    text_file = open("registered_users.txt", 'a')
    text_file.write(customer)
    text_file.close()

def submit_registration():
    response = messagebox.askokcancel("Confirm Registration","Do you want to submit your registration?")
    
    if response == 1:   # If response is 'OK'
        get_customer()
        root.quit()

def questionnaire():
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

    # Create Blank Frame
    white_frame = Frame(width=440, height=550, background="white")
    white_frame.place(in_=frame_register_form, anchor="c", relx=.5, rely=.5)
    
    # Create Label Widgets
    label_header = Label(root, text="Questionnaire", width=20,font=("bold",30))
    label_header.place(relx=0.5, rely=0.05, anchor=CENTER)
    label_yes = Label(white_frame, text="YES", width=3,font=("arial bold",12))
    label_yes.place(relx=0.795, rely=0)
    label_no = Label(white_frame, text="NO", width=3,font=("arial bold",12))
    label_no.place(relx=0.895, rely=0)

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
    # q7 = Label(white_frame, text="7.   In the past 30 days have you been to any other\n      country?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    # q7.place(relx=0.01, rely=0.53)
    # q8 = Label(white_frame, text="8.   Do you have any senior citizens at home? ", width=40,font=("bold",12), anchor=W,justify=LEFT)
    # q8.place(relx=0.01, rely=0.61)
    # q9 = Label(white_frame, text="9.   Do you work in any healthcare organization?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    # q9.place(relx=0.01, rely=0.69)
    # q10 = Label(white_frame, text="10. Do you agree to follow the rules and regulations\n       regarding COVID-19 safety and precautions?", width=40,font=("bold",12), anchor=W,justify=LEFT)
    # q10.place(relx=0.01, rely=0.77)

    # Create Yes or No Radio Buttons
    Radiobutton(white_frame, variable = q1_value, value = "YES").place(relx=0.8, rely=0.048)
    Radiobutton(white_frame, variable = q1_value, value = "NO").place(relx=0.9, rely=0.048)
    Radiobutton(white_frame, variable = q2_value, value = "YES").place(relx=0.8, rely=0.125)
    Radiobutton(white_frame, variable = q2_value, value = "NO").place(relx=0.9, rely=0.125)
    Radiobutton(white_frame, variable = q3_value, value = "YES").place(relx=0.8, rely=0.207)
    Radiobutton(white_frame, variable = q3_value, value = "NO").place(relx=0.9, rely=0.207)
    Radiobutton(white_frame, variable = q4_value, value = "YES").place(relx=0.8, rely=0.288)
    Radiobutton(white_frame, variable = q4_value, value = "NO").place(relx=0.9, rely=0.288)
    Radiobutton(white_frame, variable = q5_value, value = "YES").place(relx=0.8, rely=0.368)
    Radiobutton(white_frame, variable = q5_value, value = "NO").place(relx=0.9, rely=0.368)
    Radiobutton(white_frame, variable = q6_value, value = "YES").place(relx=0.8, rely=0.447)
    Radiobutton(white_frame, variable = q6_value, value = "NO").place(relx=0.9, rely=0.447)
    # Radiobutton(white_frame, variable = q7_value, value = "YES").place(relx=0.8, rely=0.51)
    # Radiobutton(white_frame, variable = q7_value, value = "NO").place(relx=0.9, rely=0.51)
    # Radiobutton(white_frame, variable = q8_value, value = "YES").place(relx=0.8, rely=0.587)
    # Radiobutton(white_frame, variable = q8_value, value = "NO").place(relx=0.9, rely=0.587)
    # Radiobutton(white_frame, variable = q9_value, value = "YES").place(relx=0.8, rely=0.664)
    # Radiobutton(white_frame, variable = q9_value, value = "NO").place(relx=0.9, rely=0.664)
    # Radiobutton(white_frame, variable = q10_value, value = "YES").place(relx=0.8, rely=0.741)
    # Radiobutton(white_frame, variable = q10_value, value = "NO").place(relx=0.9, rely=0.741)

myButton = Button(root, text="Next >>", width=10, command = questionnaire)
myButton.place(relx=0.5, rely=0.95, anchor=CENTER)

root.mainloop()
