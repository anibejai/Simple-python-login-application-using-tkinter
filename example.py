from tkinter import *
from tkinter import ttk
gui = Tk()
gui.geometry("400x400")
def login(us1,pw1,usr,pword):
    if us1 == usr and pw1==pword:
       i=Label(gui,text='Login success').grid(row=6,column=0)
       print("login success")
    else:
       print("wrong password")
       j=Label(gui,text='Login failed').grid(row=6,column=0)
gui.title("First title")
a = Label(gui ,text="username").grid(row=0,column = 0)
b = Label(gui ,text="password").grid(row=1,column=0)
e = Entry(gui).grid(row=0,column=1)
f = Entry(gui,show="*").grid(row=1,column=1)
c = Button(gui, text="Create account").grid(row=2,column=0)
a1 = Label(gui ,text="username").grid(row=3,column = 0)
b1 = Label(gui ,text="password").grid(row=4,column=0)
e1 = Entry(gui).grid(row=3,column=1)
f1 = Entry(gui,show="*").grid(row=4,column=1)
c1 = Button(gui, text="LOGIN",command=lambda :
     login(e,f,e1,f1)).grid(row=5,column=1)
gui.mainloop()