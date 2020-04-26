# Dashboard

from tkinter import *
from tkinter import ttk

from NewExpense import *
from NewIncome import *


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
        self.addNewExpenseButton = None
        self.addNewIncomeButton = None

    def gui_init(self):
        self.up_frame = Frame(
            self.root,
            cursor='hand1',
            bg='#3BFF1D',
            height=self.screen_height * 1 / 8,
            width=self.screen_width)
        self.up_frame.grid_propagate(0)
        self.up_frame.pack(side=TOP, fill=BOTH)
        self.down_frame = Frame(
            self.root,
            cursor='hand1',
            bg='#E5FF26',
            height=self.screen_height * 6 / 8,
            relief=RAISED,
            bd=5,
            width=self.screen_width)
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        income_amount = self.print_total_income()
        expenses_amount = self.print_total_expenes()
        self.income = Label(self.up_frame, height=2, width=35, text=income_amount, font=44).place(x=100, y=5)
        self.expense = Label(self.up_frame, height=2, width=35, text=expenses_amount, font=44).place(x=550, y=5)
        self.balance = Label(self.up_frame, height=2, width=35, text=income_amount - expenses_amount, font=44)
        self.balance.place(x=1000, y=5)
        self.print_expenses(self.down_frame)
        self.print_income(self.down_frame)
        self.addNewExpenseButton = Button(self.down_frame, text="Add new expense", font=self.font)
        self.addNewExpenseButton.place(x=400, y=570, anchor='center')
        self.addNewExpenseButton.bind("<Button-1>", self.addNewExpense)
        self.addNewIncomeButton = Button(self.down_frame, text="Add new income", font=self.font)
        self.addNewIncomeButton.place(x=800, y=570, anchor='center')
        self.addNewIncomeButton.bind("<Button-2>", self.addNewIncome)

    def addNewExpense(self, event):
        new_window = Toplevel(self.root)
        NewExpense(new_window, self.color, self.dbconnection)
        new_window.wait_window()

    def addNewIncome(self, event):
        new_window = Toplevel(self.root)
        NewIncome(new_window, self.color, self.dbconnection)
        new_window.wait_window()

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
        mycursor.execute("select * from mydatabase.expense order by expense_id desc")
        expenses_list = mycursor.fetchall()

        label = Label(frame, font=("Arial", 15), text=" Expenses ").place(x=700, y=10)
        cols = ("Number", "Expense-id", "Member-id", "Category", "Date", "Amount", "Comments")
        list_box = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            list_box.heading(col, text=col)
        list_box.place(x=55, y=40)
        verscrlbar = ttk.Scrollbar(frame,
                                   orient="vertical",
                                   command=list_box.yview)
        verscrlbar.place(x=1400, y=50)
        list_box.configure(xscrollcommand=verscrlbar.set)
        # close_button = Button(frame, text="Close", width=15, command=exit).grid(row=4, column=1)
        for i, (id1, id2, cat, date, am, comm) in reversed(list(enumerate(expenses_list, start=1))):
            list_box.insert("", "end", values=(i, id1, id2, cat, date, am, comm))

    def print_income(self, frame):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select * from mydatabase.income order by income_id desc")
        income_list = mycursor.fetchall()
        label = Label(frame, font=("Arial", 15), text="  Income  ").place(x=700, y=270)
        cols = ("Number", "Income-id", "Member-id", "Category", "Date", "Amount", "Comments")
        list_box2 = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            list_box2.heading(col, text=col)
        list_box2.place(x=55, y=300)
        verscrlbar = ttk.Scrollbar(frame,
                                   orient="vertical",
                                   command=list_box2.yview)
        verscrlbar.place(x=1400, y=300)
        list_box2.configure(xscrollcommand=verscrlbar.set)
        for i, (id1, id2, cat, date, am, comm) in reversed(list(enumerate(income_list, start=1))):
            list_box2.insert("", "end", values=(i, id1, id2, cat, date, am, comm))

