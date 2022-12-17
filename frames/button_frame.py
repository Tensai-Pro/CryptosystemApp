from tkinter import ttk

class ButtonFrame(ttk.Frame):
    def __init__(self, container, text):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.__create_widgets(text)

    def __create_widgets(self, text):
        # style = ttk.Style()
        # style.configure('btn.TButton', font=('Helvetica', 12))
        for i in range(len(text)):
            for j in range(len(text[i])):
                btn_text, btn_cmd = text[i][j]
                btn = ttk.Button(self, text=btn_text, command=btn_cmd, width=30)    # add (style='btn.TButton')
                btn.grid(row=i, column=j, padx=10, pady=10)