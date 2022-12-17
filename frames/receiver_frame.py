import tkinter as tk
from tkinter import ttk, messagebox
from frames.button_frame import ButtonFrame
from frames.info_frame import InfoFrame
from number_theory.receiver import Receiver

class ReceiverFrame(ttk.Frame):
    def __init__(self, container, public_keys, set_encryption_keys):
        super().__init__(container)

        self.public_keys = public_keys
        self.set_encryption_keys = set_encryption_keys
        self.__receiver = Receiver()

        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __gen_encryption_keys(self):
        p, g, y, x = self.__receiver.gen_encryption_keys()

        text = self.info_frame.label.cget('text')
        text += f'Private key x: {x}'
        self.info_frame.label.config(text=text)

        self.public_keys['p_encryption'] = p
        self.public_keys['g_encryption'] = g
        self.public_keys['y_encryption'] = y
        self.set_encryption_keys()
        print('receiver: ', self.public_keys)

    def __check_signature(self):
        p, a, v = self.public_keys['p_signature'], self.public_keys['a_signature'], self.public_keys['v_signature']
        self.is_correct = self.__receiver.check_signature(p, a, v)

        if self.is_correct:
            messagebox.showinfo(title='Correct', message='Signature is correct!')
        else:
            messagebox.showinfo(title='Error', message='Signature is wrong!')

    def __decrypt(self):
        if self.is_correct:
            decrypted_msg = self.__receiver.decrypt_msg()
            
            self.message.config(state='normal')
            self.message.delete('1.0', 'end')
            self.message.insert('1.0', decrypted_msg)
            self.message.config(state='disabled')

    def __create_widgets(self):
        text = [
            [('Generate keys for encryption', self.__gen_encryption_keys), ('Check signature', self.__check_signature)],
            [('Decrypt', self.__decrypt)]
        ]
        button_frame = ButtonFrame(self, text)
        button_frame.grid(row=0, column=0)

        self.message = tk.Text(self, height=10, width=50, state='disabled')
        self.message.grid(row=1, column=0, pady=20)

        self.info_frame = InfoFrame(self)
        self.info_frame.grid(row=2, column=0)

    def receive_msg(self, C1, C2, e, y):
        self.__receiver.receive_msg(C1, C2, e, y)

        self.message.config(state='normal')
        self.message.insert('1.0', (str(C1) + ' ' + str(C2)))
        self.message.config(state='disabled')