from tkinter import messagebox

from AdminPage import *


class LoginFrame:
    def __init__(self, parent, root, height, width, side, color, dbconnection, admincredentials):
        self.parent = parent
        self.root = root
        self.height = height
        self.width = width
        self.side = side
        self.font = ('Times', 12, 'roman')
        self.color = color
        self.dbConnection = dbconnection
        self.adminCredentials = admincredentials
        self.frame = None
        self.userNameEntry = None
        self.userNameLabel = None
        self.passwordEntry = None
        self.passwordLabel = None
        self.loginButton = None
        self.gui_init()

    def gui_init(self):
        self.frame = Frame(
            self.root,
            cursor='arrow',
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5)
        self.frame.grid_propagate(0)
        self.frame.pack(expand=True, side=self.side, fill=BOTH)

        frame1 = Frame(
            self.frame,
            cursor='arrow',
            bg=self.color,
            height=self.height / 3,
            width=self.width * 2 / 3)
        frame1.grid_propagate(0)
        frame1.pack(expand=True, fill=BOTH)
        frame1.place(relx=0.5, rely=0.5, anchor='center')

        # Labels
        self.userNameLabel = Label(
            frame1, text="UserName", font=self.font, bg=self.color)
        self.userNameLabel.grid(row=0, column=0, sticky=E, padx=2, pady=2)

        self.passwordLabel = Label(
            frame1, text="Password", font=self.font, bg=self.color)
        self.passwordLabel.grid(row=1, column=0, sticky=E, padx=2, pady=2)

        # Entries
        self.userNameEntry = Entry(frame1, width=25, font=self.font)
        self.userNameEntry.grid(row=0, column=1, sticky=W, padx=2, pady=2)

        self.passwordEntry = Entry(frame1, width=25, show='*', font=self.font)
        self.passwordEntry.grid(row=1, column=1, sticky=W, padx=2, pady=2)

        # creating login button
        self.loginButton = Button(frame1, text="Login", font=self.font)
        self.loginButton.bind("<Button-1>", self.__loginAction)
        self.loginButton.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

    def __loginAction(self, event):
        """
        This method is called when the "Login" button is pressed
        It checks the administrator credentials
        """

        username = self.userNameEntry.get()
        password = self.passwordEntry.get()

        if username == self.adminCredentials[0] and password == self.adminCredentials[1]:
            AdminPage(self.parent, self.color, self.font, self.dbConnection)
        else:
            """
            Pop a message stating that the Username/Password is incorrect.
            """
            messagebox.showerror("Error", "The username and password that you entered did not match our records. "
                                          "Please double-check and try again.")
