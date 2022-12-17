import tkinter as tk
from tkinter import ttk
from frames.public_keys_frame import PublicKeysFrame
from frames.sender_frame import SenderFrame
from frames.receiver_frame import ReceiverFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cryptosystem App')
        self.geometry('1300x700')
        self.resizable(0, 0)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        self.public_keys ={}

        self.__create_widgets()

    def __set_encryption_keys(self):
        p, g, y = self.public_keys['p_encryption'], self.public_keys['g_encryption'], self.public_keys['y_encryption']
        text = self.public_keys_frame.encryption_keys.cget('text')
        text += f"({p}, {g}, {y})"
        self.public_keys_frame.encryption_keys.config(text=text)

    def __set_signature_keys(self):
        p, q, a, v = self.public_keys['p_signature'], self.public_keys['q_signature'], self.public_keys['a_signature'], self.public_keys['v_signature']
        text = self.public_keys_frame.signature_keys.cget('text')
        text += f"({p}, {q}, {a}, {v})"
        self.public_keys_frame.signature_keys.config(text=text)

    def __set_signature(self, C1, C2, e, y):
        self.C1 = C1
        self.C2 = C2
        self.e = e
        self.y = y

    def __send_msg(self):
        self.receiver_frame.receive_msg(self.C1, self.C2, self.e, self.y)

    def __create_widgets(self):
        self.public_keys_frame = PublicKeysFrame(self)
        self.public_keys_frame.grid(row=0, column=0, columnspan=3, pady=30)

        self.sender_frame = SenderFrame(self, self.public_keys, self.__set_signature_keys, self.__set_signature)
        self.sender_frame.grid(row=1, column=0, sticky='N')

        self.send_msg_btn = ttk.Button(self, text='Send message', width=20, command=self.__send_msg)
        self.send_msg_btn.grid(row=1, column=1, padx=10, ipady=20, sticky='N')

        self.receiver_frame = ReceiverFrame(self, self.public_keys, self.__set_encryption_keys)
        self.receiver_frame.grid(row=1, column=2, sticky='N')



if __name__ == '__main__':
    app = App()
    app.mainloop()