import os.path
from tkinter import *
import tkinter.messagebox
import os
import tkinter.font as font
import subprocess

root = Tk()
root.geometry('500x500')
root.title("Chat-UP!")

Fullname = StringVar()
Email = StringVar()
var = IntVar()
p = StringVar()
var1 = IntVar()



def register1():
    os.system('C:/Users/user2022/Desktop/project/reg.py')
def login1():
    os.system('C:/Users/user2022/Desktop/project/login.py')


bg = PhotoImage(file='source/bg.png')
root.iconbitmap("source/icone.ico")


label1 = Label(root, image=bg)
label1.place(x=0, y=0)

label_0 = Label(root, text="WELCOME TO CHAT-UP!", bg='black', fg='red',height=5, width=30,anchor='center', font=("bold", 20))
label_0.place(x=10, y=30)

Button(root, text='Register',height=2,font=('Helvetica', '20'), width=20,bg='green',activeforeground='blue', fg='white',command=register1).place(x=90, y=300)
Button(root, text='Login', height=2,font=('Helvetica', '20'),width=20, bg='green',activeforeground='blue', fg='white',command=login1).place(x=90, y=200)
Button(root, text='EXIT',bg='red',fg='white',command=exit).place(x=90,y=400)
root.mainloop()