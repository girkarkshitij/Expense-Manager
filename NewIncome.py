from tkinter import *
import time
import Message


class NewIncome:
    def __init__(self, root, color, dbconnection, current_login):
        self.root = root
        self.color = color
        self.dbconnection = dbconnection
        self.current_login = current_login
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.width = self.screen_width / 3
        self.height = self.screen_height / 3
        self.gui_init()
        self.frame = None
        self.topFrame = None

    def gui_init(self):
        self.root.title("Add new income record")
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

        self.categoryLabel = Label(
            self.topFrame, text="Category", bg=self.color)
        self.categoryLabel.grid(row=1, column=0, sticky=W, padx=2, pady=2)

        self.amountLabel = Label(
            self.topFrame, text="Amount", bg=self.color)
        self.amountLabel.grid(row=3, column=0, sticky=W, padx=2, pady=2)

        self.commentLabel = Label(
            self.topFrame,
            text="Comments",
            bg=self.color)
        self.commentLabel.grid(row=5, column=0, sticky=W, padx=2, pady=2)

        self.category_options = ["Salary", "Prize", "Rental", "Other"]
        self.variable = StringVar(self.topFrame)
        self.categoryEntry = OptionMenu(self.topFrame, self.variable, *self.category_options)
        self.categoryEntry.grid(row=1, column=1, sticky=W, padx=2, pady=2)

        self.amountEntry = Entry(self.topFrame)
        self.amountEntry.grid(row=3, column=1, sticky=W, padx=2, pady=2)

        self.commentEntry = Text(self.topFrame, width=20, height=5)
        self.commentEntry.grid(row=5, column=1)

        self.submit_button = Button(
            self.topFrame, text="Submit")
        self.submit_button.bind("<Button-1>", self.addincome)
        self.submit_button.grid(row=9, column=1, columnspan=3, padx=2, pady=2)

    def addincome(self, event):
        mycursor = self.dbconnection.cursor()
        options = ["Salary", "Prize", "Rental", "Other"]
        temp = self.variable.get()
        category = options.index(temp) + 1
        amount = self.amountEntry.get()
        comments = self.commentEntry.get("1.0", 'end-1c')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO income (member_id, income_category_id, income_date, amount, comments) VALUES (%s, %s, " \
                "%s, %s, %s) "
        values = (self.current_login, category, current_time, amount, comments)
        mycursor.execute(query, values)
        self.dbconnection.commit()
        self.message("Record updated successfully")

        for child in self.root.winfo_children():
            child.destroy()

        self.root.destroy()

    def message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window, self.color, message)
        new_window.wait_window()
