from tkinter import *


class Message(object):
    def __init__(self, root, color, message):
        self.root = root
        self.font = ('Times',12 , 'roman')
        self.color = color
        self.message = message
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = self.screen_height / 4
        self.width = self.screen_width / 4
        self.frame = None
        self.gui_init()

    def gui_init(self):
        self.root.title("Message")
        self.root.resizable(width=False, height=False)
        self.frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5)

        self.frame.grid_propagate(0)
        self.frame.pack(expand=True, side=TOP, fill=BOTH)
        # creating labels
        top_frame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 8 / 10,
            width=self.width)
        top_frame.grid_propagate(0)
        top_frame.pack(expand=True, fill=BOTH, side=TOP)

        down_frame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 2 / 10,
            width=self.width)
        down_frame.grid_propagate(0)
        down_frame.pack(expand=True, fill=BOTH, side=TOP)

        message_label = Label(
            top_frame, text=self.message, font=self.font, bg=self.color)
        message_label.place(relx=0.5, rely=0.5, anchor='center')

        # creating login button
        ok_button = Button(down_frame, text="OK", font=('Times', 8, 'roman'))
        ok_button.bind("<Button-1>", self.__ok)
        ok_button.place(relx=0.5, rely=0.5, anchor='center')

    def __ok(self, event):
        for child in self.root.winfo_children():
            child.destroy()
        self.root.destroy()