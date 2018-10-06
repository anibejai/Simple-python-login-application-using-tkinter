from tkinter import*
import sqlite3
from tkinter import messagebox
root=Tk()
logo=PhotoImage(file="pylogo.gif")
Label(root, image=logo).pack(side="left")
#Label.grid(pady=30,row=0,column=0)
root.title("Python Application project")    #for setting title of project
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 700
height =380
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

'''                   #database connectivity#
def Database():
    global conn, cursor
    conn = sqlite3.connect('C:/Users/anirudh/Desktop/python database/sqlite-tools-win32-x86-3240000/testdb.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'entries' (id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT,Firstname TEXT,Lastname TEXT)")
'''


def login():
    if username.get() == '' or password.get() == '':
        lbl_text.config(text="Please complete the required field!", fg="red")

    else:
        conn = sqlite3.connect('C:/Users/anirudh/Desktop/python database/sqlite-tools-win32-x86-3240000/testdb.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM entries WHERE username = ? AND password =?", (username.get(),password.get()))

        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            messagebox.showerror("error","username and password is incorrect!")
            USERNAME.set("")
            PASSWORD.set("")




def Back():
        Home.destroy()
        root.deiconify()


def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Login successful!", font=('times new roman', 40)).pack()
    lbl_home = Label(Home, text="welcome anirudh!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)


def cancel():
    if messagebox.askyesno('Verify', 'Really quit?'):
        messagebox.showwarning('Yes', 'login cancelled')


def reset():
    username.delete(0, END)
    password.delete(0, END)




def register():
    import registration






USERNAME = StringVar()
PASSWORD = StringVar()


                       #FRAME#
Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)

Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)


                      #LABELS#

lbl_title = Label(Top, text="Python Login", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

                   #ENTRY WIDGETS#

username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)








                     #BUTTON WIDGETS#

btn_login = Button(Form,text="SUBMIT", width=10, command=login)
btn_login.grid(pady=30, row=2, column=0)
btn_login.bind('<Return>', login)

btn_login = Button(Form, text="CANCEL", width=10, command=cancel)
btn_login.grid(pady=30, row=2, column=1)
btn_login.bind('<Return>', cancel)


btn_login = Button(Form, text="RESET", width=10, command=reset)
btn_login.grid(pady=30, row=2, column=3)
btn_login.bind('<Return>', reset)


btn_login = Button(Form, text="REGISTER", width=10, command=register)
btn_login.grid(pady=30, row=3, column=1)
btn_login.bind('<Return>', register)





if __name__ == '__main__':
    root.mainloop()