from tkinter import *
from tkinter import filedialog
import json
import os
import ast

class VisualAid(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

    def initial_values(self):
        pass

    def setup_window(self):
        self.resizable(width=False, height=False)
        self.geometry('550x700')
        self.title("Barber's Visual Aid")

        # Create Frame Widget
        self.main_frame = Frame(self)

        # Create Button Widget to find file
        self.filename = filedialog.askopenfilename(title="Please select a file", filetypes=((".txt files", "*.txt"),("all files", "*.*")))
    
        # Create Label Widgets
        self.label_filename = Label(self.main_frame, text=self.filename,font=("bold",10))
        self.label_filename.pack()
        self.label_header = Label(self.main_frame, text="Barber's Schedule", width=25,font=("bold",20),relief=RIDGE)
        self.label_header.place(relx=0.5, rely=0.05,anchor=CENTER)

    def open_file(self):
        pass


app = VisualAid()
app.mainloop()

