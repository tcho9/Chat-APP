import os.path
import sqlite3
from tkinter import *
import tkinter.messagebox

import os

users = list()

pwd = "C:/Users/user2022/Desktop/project"


def database():
    name = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    room = c.get()
    gender = var.get()

    conn = sqlite3.connect('user.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS User (name TEXT,email TEXT,password TEXT,room TEXT,Gender TEXT)')
    cursor.execute('INSERT INTO reg (name,email,password,room,Gender) VALUES(?,?,?,?,?)',
                   (name, email, password, room, gender,))
    conn.commit()

    if (name == "" or email == "" or password == "" or room == 'Room' or gender == 0):
        tkinter.messagebox.showinfo('Invalid Message Alert', "Fields cannot be left empty!")

    else:
        os.chdir(pwd)
        tkinter.messagebox.showinfo('Success Message', "Successfully registered!")

        exit()


items = os.listdir('C:/Users/user2022/Desktop/project')

root = Tk()
root.geometry('500x500')
bg = PhotoImage(file='source/bg.png')
root.iconbitmap("source/icone.ico")
root.title("Registration Form")


label6 = Label(root, image=bg)
label6.place(x=0, y=0)

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=70, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=60, y=180)

entry_2 = Entry(root)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Password", width=20, font=("bold", 10))
label_3.place(x=60, y=230)
entry_3 = Entry(root)
entry_3.place(x=240, y=230)

label_4 = Label(root, text="Gender", width=20, font=("bold", 10))
label_4.place(x=60, y=280)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=280)
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=280)

label_5 = Label(root, text="Room", width=20, font=("bold", 10))
label_5.place(x=60, y=320)

list1 = ['Room-1-', 'Room-2-', 'Room-3-'];
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width=15)
c.set('Select your Room')
droplist.place(x=240, y=320)

Button(root, text='Submit', width=20, bg='green', fg='white', command=database).place(x=180, y=380)


root.wm_attributes("-transparentcolor", 'grey')

root.mainloop()
