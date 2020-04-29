# Dashboard

from tkinter import ttk

from NewExpense import *
from NewIncome import *


class AdminPage:
    def __init__(self, root, color, font, dbconnection, width, current_login):

        for child in root.winfo_children():
            child.destroy()

        self.root = root
        self.dbconnection = dbconnection
        self.current_login = current_login
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
        self.family_expenses = None
        self.family_income = None

    def gui_init(self):
        self.up_frame = Frame(
            self.root,
            cursor='hand1',
            bg='#3368FF',
            height=self.screen_height * 1 / 8,
            width=self.screen_width)
        self.up_frame.grid_propagate(0)
        self.up_frame.pack(side=TOP, fill=BOTH)
        self.down_frame = Frame(
            self.root,
            cursor='hand1',
            bg='#120C2C',
            height=self.screen_height * 6 / 8,
            relief=RAISED,
            bd=5,
            width=self.screen_width)
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        income_amount = self.print_total_income()
        expenses_amount = self.print_total_expenes()
        income_string = "Income " + str(income_amount)
        expenses_string = "Expenses " + str(expenses_amount)
        balance_string = "Balance " + str(income_amount - expenses_amount)
        self.income = Label(self.up_frame, height=2, width=35, text=income_string, font=44).place(x=100, y=5)
        self.expense = Label(self.up_frame, height=2, width=35, text=expenses_string, font=44).place(x=550, y=5)
        self.balance = Label(self.up_frame, height=2, width=35, text=balance_string, font=44)
        self.balance.place(x=1000, y=5)
        self.print_expenses(self.down_frame)
        self.print_income(self.down_frame)
        self.addNewExpenseButton = Button(self.down_frame, text="Add new expense", font=self.font,  bg='#938DF6')
        self.addNewExpenseButton.place(x=500, y=570, anchor='center')
        self.addNewExpenseButton.bind("<Button-1>", self.addNewExpense)
        self.addNewIncomeButton = Button(self.down_frame, text="Add new income", font=self.font,  bg='#938DF6')
        self.addNewIncomeButton.place(x=1000, y=570, anchor='center')
        self.addNewIncomeButton.bind("<Button-1>", self.addNewIncome)
        self.family_income = Button(self.down_frame, text="Total Family Income", font=self.font,  bg='#938DF6')
        self.family_income.place(x=1000, y=650, anchor='center')
        self.family_income.bind("<Button-1>", self.display_family_income)
        self.family_expenses = Button(self.down_frame, text="Total Family Expenses", font=self.font, bg='#938DF6')
        self.family_expenses.place(x=500, y=650, anchor='center')
        self.family_expenses.bind("<Button-1>", self.display_family_expenses)

    def message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window, self.color, message)
        new_window.wait_window()

    def display_family_income(self, event):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select sum(amount) from income")
        total = mycursor.fetchone()
        self.message("Total Family Income\n{0}".format(total[0]))

    def display_family_expenses(self, event):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select sum(amount) from expense")
        total = mycursor.fetchone()
        self.message("Total Family Expenses\n{0}".format(total[0]))

    def addNewExpense(self, event):
        new_window = Toplevel(self.root)
        NewExpense(new_window, self.color, self.dbconnection, self.current_login)
        new_window.wait_window()

    def addNewIncome(self, event):
        new_window = Toplevel(self.root)
        NewIncome(new_window, self.color, self.dbconnection, self.current_login)
        new_window.wait_window()

    def print_total_income(self):
        mycursor = self.dbconnection.cursor()
        member_variable = (self.current_login,)
        query = "select sum(amount) from income where member_id = %s"
        mycursor.execute(query, member_variable)
        total = mycursor.fetchone()
        return total[0]

    def print_total_expenes(self):
        mycursor = self.dbconnection.cursor()
        member_variable = (self.current_login,)
        query = "select sum(amount) from expense where member_id = %s"
        mycursor.execute(query, member_variable)
        total = mycursor.fetchone()
        return total[0]

    def print_expenses(self, frame):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select e.expense_id,f.first_name,  ec.name, e.expense_date, e.amount, e.comments from "
                         "expense e inner join family f on e.member_id = f.member_id inner join e_category ec on "
                         "e.expense_category_id = ec.expense_category_id")
        expenses_list = mycursor.fetchall()
        label = Label(frame, font=("Arial", 15), text=" Expenses ").place(x=700, y=10)
        cols = ("Number", "Member", "Expense - Category", "Date", "Amount", "Comments")
        list_box = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            list_box.heading(col, text=col)
        list_box.place(x=55, y=40)
        verscrlbar = ttk.Scrollbar(frame,
                                   orient="vertical",
                                   command=list_box.yview)
        verscrlbar.place(x=1400, y=50)
        list_box.configure(xscrollcommand=verscrlbar.set)
        for i, (id1, id2, cat, date, am, comm) in reversed(list(enumerate(expenses_list, start=1))):
            list_box.insert("", "end", values=(id1, id2, cat, date, am, comm))

    def print_income(self, frame):

        mycursor = self.dbconnection.cursor()
        mycursor.execute("select i.income_id,f.first_name,  ic.name, i.income_date, i.amount, i.comments from income "
                         "i inner join family f on i.member_id = f.member_id inner join i_category ic on "
                         "i.income_category_id = ic.income_category_id")
        income_list = mycursor.fetchall()
        label = Label(frame, font=("Arial", 15), text="  Income  ").place(x=700, y=270)
        cols = ("Number", "Member", "Income - Category", "Date", "Amount", "Comments")
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
            list_box2.insert("", "end", values=(id1, id2, cat, date, am, comm))
