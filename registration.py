from tkinter import *
import sqlite3
from tkinter import messagebox
root=Tk()
root.geometry('600x600')
root.title("Registration Form")
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Firstname:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Lastname:",width=20,font=("bold", 10))
label_2.place(x=78,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Username:",width=20,font=("bold", 10))
label_3.place(x=78,y=230)

entry_3=Entry(root)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Email:",width=20,font=("bold", 10))
label_4.place(x=78,y=280)

entry_4=Entry(root)
entry_4.place(x=240,y=280)

label_5 = Label(root, text="Company:",width=20,font=("bold", 10))
label_5.place(x=78,y=330)

entry_5=Entry(root,)
entry_5.place(x=240,y=330)

label_6 = Label(root, text="Password:",width=20,font=("bold", 10))
label_6.place(x=78,y=380)

entry_6=Entry(root,show='*')
entry_6.place(x=240,y=380)


label_7 = Label(root, text="Confirm Password:",width=20,font=("bold", 10))
label_7.place(x=78,y=430)

entry_7=Entry(root,show='*')
entry_7.place(x=240,y=430)


def regsubmit():
       if entry_3.get() == '' or entry_6.get() == '' :
              messagebox.showinfo('enter all credentials')
       else:

              import db
              uname =entry_3.get()
              pwd = entry_6.get()

              conn = sqlite3.connect('C:/Users/anirudh/Desktop/python database/sqlite-tools-win32-x86-3240000/testdb.db')
              cursor = conn.cursor()
              cursor.execute("INSERT INTO entries(username,password)VALUES(?,?)",(uname,pwd))
              conn.commit()
              root.destroy()


def reset():
       entry_1.delete(0,END)
       entry_2.delete(0, END)
       entry_3.delete(0, END)
       entry_4.delete(0, END)
       entry_5.delete(0, END)
       entry_6.delete(0, END)
       entry_7.delete(0, END)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=regsubmit).place(x=78,y=480)
Button(root, text='Reset',width=20,bg='brown',fg='white',command=reset).place(x=400,y=480)



root.mainloop()