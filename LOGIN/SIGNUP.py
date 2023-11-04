from tkinter import *
from PIL import ImageTk
import tkinter


root = Tk()
signup_window = root


#######################

signup_window.title('Sign Up Page')
background = ImageTk.PhotoImage(file='C:/Users/kenneth/Pictures/Saved Pictures/BG3.jpg')
BG1 = Label(root, image=background)
BG1.place(x=0, y=0)

frame = tkinter.Frame()
frame.config(bg="BLACK")
frame.place(x=700, y=300)


############################


def l0g():
    signup_window.destroy()
    import LOGIN




#########################


signup_label = Label(frame, text='CREATE AN ACCOUNT', bg='WHITE', fg='BLUE',  font=('Arial', 10))
signup_label.grid(row=0, column=0, columnspan=2)
email_label = Label(frame, text="ENTER YOUR EMAIL", bg="BLACK", fg="BLUE", font=("Arial", 10))
email_label.grid(row=5, column=0)
username_label = Label(frame, text='ENTER YOUR USERNAME', bg="BLACK", fg="BLUE", font=("Arial", 10))
username_label.grid(row=6, column=0)
password_label = Label(frame, text="ENTER YOUR PASSWORD", bg="BLACK", fg="BLUE", font=("Arial", 10))
password_label.grid(row=7, column=0)
confirm_label = Label(frame, text="CONFIRM PASSWORD", bg='BLACK', fg='BLUE', font=('Arial', 10))
confirm_label.grid(row=8, column=0)
already = Label(frame, text='Already have an account?', bg="BLACK", fg="WHITE", font=('Arial', 8))
already.grid(row=14, column=0)
email_entry = Entry(frame)
email_entry.grid(row=5, column=1, pady=10)
username_entry = Entry(frame)
username_entry.grid(row=6, column=1, pady=10)
password_entry = Entry(frame)
password_entry.grid(row=7, column=1, pady=10)
confirm_entry = Entry(frame)
confirm_entry.grid(row=8, column=1, pady=10)
TaC = Checkbutton(frame, text="I Agree to the Terms and Conditions", bg="BLACK", fg="WHITE", font=('Arial', 7))
TaC.grid(row=10, column=1)
sign1 = Button(frame, text='SIGN UP', font=('Arial', 12), bg='BLACK', fg='BLUE')
sign1.grid(row=12, column=0, columnspan=2, pady=20)
LOG = Button(frame, text='Log in', command=l0g, font=('Arial', 8), bg='BLACK', fg='BLUE', cursor="hand2")
LOG.grid(row=14, column=1)




signup_window.mainloop()
root.mainloop