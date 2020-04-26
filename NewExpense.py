from tkinter import *


class NewExpense:
    def __init__(self, root, color, dbconnection):
        self.root = root
        self.color = color
        self.dbconnection = dbconnection
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.width = self.screen_width / 3
        self.height = self.screen_height / 3
        self.gui_init()
        self.frame = None
        self.topFrame = None

    def gui_init(self):
        self.root.title("Add new expense record")
        self.root.resizable(width=False, height=False)

        self.frame = Frame(
            self.root,
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5
        )

        self.frame.pack(side=TOP, expand=True, fill=BOTH)
        self.frame.grid_propagate(0)

        self.topFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 4 / 5,
            width=self.width * 4 / 5,
        )

        self.topFrame.grid_propagate(0)
        self.topFrame.pack(expand=True, fill=BOTH)
        self.topFrame.place(relx=0.5, rely=0.5, anchor='center')
