import os.path
from tkinter import *
import tkinter.messagebox
import linecache

path = 'C:/Users/user2022/Desktop/project'
items = os.listdir(path)


def validate():
    name = entry_1.get()
    password = entry_3.get()
    name += ".txt"

    if name in items:
        with open(name, 'r') as fp:
            line_numbers = [2]
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
        if lines[0] == password:
            tkinter.messagebox.showinfo('Success', 'WELCOME!')
            os.system('C:/Users/user2022/Desktop/project/client.py')


        else:
            tkinter.messagebox.showinfo('Invalid Password')
    else:
        tkinter.messagebox.showinfo('Invalid Username')


root = Tk()
root.geometry('500x500')
bg = PhotoImage(file='source/bg.png')
root.title("LogIn Form")
root.iconbitmap("source/icone.ico")

label2 = Label(root, image=bg)
label2.place(x=0, y=0)

label_0 = Label(root, text="Login Form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_3 = Label(root, text="Password", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
entry_3 = Entry(root)
entry_3.place(x=240, y=230)

Button(root, text='login', width=20, bg='green', fg='white', command=validate).place(x=180, y=380)

root.mainloop()
exit()
