import tkinter as tk
from tkinter import *
import sqlite3
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

        for F in (StartPage, PageOne):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, SeaofBTCapp, controller):
        Frame.__init__(self, SeaofBTCapp)

        label = Label(self, text="login page", font=LARGE_FONT)
        label_1 = Label(self, text="username")
        label_2 = Label(self, text="Password")
        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")
        label_1.grid(row=0, sticky=E)
        label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        # self.label.pack(pady=10, padx=10)
        # label_1.pack()
        # label_2.pack()

        SeaofBTCapp.show_frame(PageOne)
       # button = Button(self, text="Visit Page 1",command=self.loginbut)
        #button.grid(row=2,column=1)

       # self.button2 = Button(self, text="Visit Page 2",
                              #command=lambda: controller.show_frame(PageTwo))
        # button2.pack()
        self.pack()

    def loginbut(self,parent,controller):
        # print("Clicked")
        Frame.__init__(self, parent)

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

        else:
            #tm.showerror("Login error", "Incorrect username")
            controller.show_frame(PageOne)
        conn.commit()
        conn.close()


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(StartPage))
        button1.pack()




app = SeaofBTCapp()
app.mainloop()
