from tkinter import ttk

class PublicKeysFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        self.encryption_keys = ttk.Label(self, text='Public keys for encryption (p, g, y): ', font=('Arial', 16))
        self.encryption_keys.grid(row=0, column=0)

        self.signature_keys = ttk.Label(self, text='Public keys for signature (p, q, a, v): ', font=('Arial', 16))
        self.signature_keys.grid(row=1, column=0)

        for widget in self.winfo_children():
            widget.grid(padx=10, pady=10)
