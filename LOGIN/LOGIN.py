from tkinter import messagebox
import tkinter
import colorsys
from tkinter import *
import sys
import random
import time
from datetime import datetime
from turtle import * 
from PIL import Image, ImageTk


root = Tk()

# lists

accounts = []

# start

window = root
window.title("Login Form")
winBG = ImageTk.PhotoImage(file='C:/Users/kenneth/Pictures/Saved Pictures/BG3.jpg')
winBg = Label(window, image=winBG)
winBg.place(x=0, y=0)


frame = tkinter.Frame()
frame.config(bg="BLACK")
frame.place(x=700, y=300)


def login():
    username = ""
    password = ""
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="LOGIN SUCCESSFUL!", message="YOU HAVE LOGGED IN!")
    else:
        messagebox.showinfo(title='INVALID LOGIN', message="PLEASE TRY AGAIN.")



def sign():
    window.destroy()
    import SIGNUP


def hide():
    password_entry.config(show="*")
    show_button.config(command=show)
    


def show():
    password_entry.config(show="")
    show_button.config(command=hide)
    

# widgets 

login_label = Label(frame, text='LOGIN', bg="BLACK", fg="BLUE", font=("Arial", 15))
username_label = Label(frame, text='USERNAME', bg="BLACK", fg="BLUE", font=("Arial", 10))
password_label = Label(frame, text="PASSWORD", bg="BLACK", fg="BLUE", font=("Arial", 10)) 


# button
login_button = Button(frame, command=login, text="LOGIN", bg="GRAY", fg="BLACK", font=("Arial", 10))
sign_up_button = Button(frame, text="SIGN UP", command=sign, bg="GRAY", fg="BLACK", font=("Arial", 10))
show_button = Button(frame, command=hide)


# entry
username_entry = Entry(frame)
password_entry = Entry(frame)


# position
login_label.grid(row=5, column=0, columnspan=2, sticky="news", pady=10)
username_label.grid(row=6, column=0)
password_label.grid(row=7, column=0)
username_entry.grid(row=6, column=1, pady=10)
password_entry.grid(row=7, column=1, pady=10)
login_button.grid(row=8, column=0, padx=10, pady=20)
sign_up_button.grid(row=8, column=1, padx=10, pady=20)
show_button.grid(row=7, column=2, pady=10)



root.mainloop()