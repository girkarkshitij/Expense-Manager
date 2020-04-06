# Dashboard

from tkinter import *


class AdminPage:
    def __init__(self, root, color, font, dbconnection):
        for child in root.winfo_children():
            child.destroy()

        self.root = root
        self.dbconnection = dbconnection
        self.color = color
        self.font = font
        self.screen_width = self.root.winfo_screenwidth() * 3 / 4
        self.screen_height = self.root.winfo_screenheight() * 3 / 4

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
            bg='#90FF20',
            height=self.screen_height * 7 / 8,
            width=self.screen_width)
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        income_amount = self.print_income()
        expenses_amount = self.print_expenes()
        self.income = Label(self.up_frame, height=5, width=35, text=income_amount, font=44).place(x=100, y=20)
        self.expense = Label(self.up_frame, height=5, width=35, text=expenses_amount, font=44).place(x=550, y=20)
        self.balance = Label(self.up_frame, height=5, width=35, text=income_amount - expenses_amount, font=44).place(x=1000, y=20)

    def print_income(self):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select sum(amount) from income")
        total = mycursor.fetchone()
        return total[0]

    def print_expenes(self):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select sum(amount) from expense")
        total = mycursor.fetchone()
        return total[0]
