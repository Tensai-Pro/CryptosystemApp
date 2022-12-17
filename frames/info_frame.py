from tkinter import ttk

class InfoFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        self.label = ttk.Label(self, text='', font=("Arial", 14))
        self.label.grid(row=0, column=0)