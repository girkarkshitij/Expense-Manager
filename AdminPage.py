# Dashboard

from tkinter import *
from tkinter import ttk


class AdminPage:
    def __init__(self, root, color, font, dbconnection, width):
        for child in root.winfo_children():
            child.destroy()

        self.root = root
        self.dbconnection = dbconnection
        self.color = color
        self.font = font
        self.screen_width = self.root.winfo_screenwidth() * 3 / 4
        self.screen_height = self.root.winfo_screenheight() * 3 / 4
        self.width = width
        self.gui_init()
        self.up_frame = None
        self.down_frame = None
        self.dashBoard = None
        self.logoutFrame = None
        self.income = None
        self.expense = None
        self.balance = None

    def gui_init(self):
        self.up_frame = Frame(
            self.root,
            cursor='hand1',
            bg='#C8FF1B',
            height=self.screen_height / 8,
            width=self.screen_width)
        self.up_frame.grid_propagate(0)
        self.up_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.down_frame = Frame(
            self.root,
            cursor='hand1',
            bg='#FFFFFF',
            height=self.screen_height * 7 / 8,
            relief=RAISED,
            bd=5,
            width=self.screen_width)
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        income_amount = self.print_total_income()
        expenses_amount = self.print_total_expenes()
        self.income = Label(self.up_frame, height=5, width=35, text=income_amount, font=44).place(x=100, y=20)
        self.expense = Label(self.up_frame, height=5, width=35, text=expenses_amount, font=44).place(x=550, y=20)
        self.balance = Label(self.up_frame, height=5, width=35, text=income_amount - expenses_amount, font=44)
        self.balance.place(x=1000, y=20)
        self.print_expenses(self.down_frame)
        self.print_income(self.down_frame)

    def print_total_income(self):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select sum(amount) from income")
        total = mycursor.fetchone()
        return total[0]

    def print_total_expenes(self):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select sum(amount) from expense")
        total = mycursor.fetchone()
        return total[0]

    def print_expenses(self, frame):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select * from mydatabase.expense")
        expenses_list = mycursor.fetchall()

        # label = Label(frame, font=("Arial", 30), text="Expenses").place(x=100, y=40)
        cols = ("Number", "Expense-id", "Member-id", "Category", "Date", "Amount", "Comments")
        list_box = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            list_box.heading(col, text=col)
        list_box.grid(row=3, column=1, columnspan=3)
        # close_button = Button(frame, text="Close", width=15, command=exit).grid(row=4, column=1)
        for i, (id1, id2, cat, date, am, comm) in enumerate(expenses_list, start=1):
            list_box.insert("", "end", values=(i, id1, id2, cat, date, am, comm))

    def print_income(self, frame):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select * from mydatabase.income")
        income_list = mycursor.fetchall()

        # label = Label(frame, font=("Arial", 30), text="Income").place(x=100, y=200)
        cols = ("Number", "Expense-id", "Member-id", "Category", "Date", "Amount", "Comments")
        list_box2 = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            list_box2.heading(col, text=col)
        list_box2.grid(row=15, column=1, columnspan=3)
        # close_button = Button(frame, text="Close", width=15, command=exit).grid(row=4, column=1)
        for i, (id1, id2, cat, date, am, comm) in enumerate(income_list, start=1):
            list_box2.insert("", "end", values=(i, id1, id2, cat, date, am, comm))
