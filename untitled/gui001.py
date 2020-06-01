import sqlite3
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm

LARGE_FONT = ("Verdana", 12)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (login, PageOne,PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

       # button1 = Button(self, text="Back to Home",
                         #command=lambda: controller.show_frame(StartPage))
       # button1.pack()

        #button2 = Button(self, text="Page Two",
         #                command=lambda: controller.show_frame(PageTwo))
        #button2.pack()

class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

       # button1 = Button(self, text="Back to Home",
                         #command=lambda: controller.show_frame(StartPage))
       # button1.pack()

       # button2 = Button(self, text="Page One",
                         #command=lambda: controller.show_frame(PageOne))
       # button2.pack()

class login(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.logbtn = Button(self, text="LOGIN", command=self.loginbut)
        self.logbtn.grid(row=3, column=1)
        self.logbtn = Button(self, text="SIGNUP", command=self.signbut)
        self.logbtn.grid(row=3, column=0)

        self.pack()



    def loginbut(self):
        # print("Clicked")


        username = self.entry_1.get()
        password = self.entry_2.get()
        # print(username, password)
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute("SELECT count(*)  FROM login WHERE user=? AND pass=?", (username, password))
        # state= len(c.fetchall());
        state = c.fetchone()
        print(state[0])

        if (state[0] == 1):
            tm.showinfo("Login info", "Welcome ")
            #controller.show_frame(PageOne())

        else:
            tm.showerror("Login error", "Incorrect username")


        conn.commit()
        conn.close()

    def signbut(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute("SELECT count(*)  FROM login WHERE user=? AND pass=?", (username, password))
        state = c.fetchone()
        if (state[0] == 0):
            c.execute("INSERT INTO login (user,pass)VALUES (?,?)", (username, password))

        else:
            tm.showinfo("Login info", "The user already exist in database")
        conn.commit()
        conn.close()



app = SeaofBTCapp()
app.mainloop()
