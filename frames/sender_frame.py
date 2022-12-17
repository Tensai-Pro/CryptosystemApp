import tkinter as tk
from tkinter import ttk
from frames.button_frame import ButtonFrame
from frames.info_frame import InfoFrame
from number_theory.sender import Sender

class SenderFrame(ttk.Frame):
    def __init__(self, container, public_keys, set_signature_keys, set_signature):
        super().__init__(container)

        self.public_keys = public_keys
        self.set_signature_keys = set_signature_keys
        self.set_signature = set_signature
        self.__sender = Sender()

        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __gen_session_key(self):
        k = self.__sender.gen_session_key(self.public_keys['p_encryption'])

        text = self.info_frame.label.cget('text')
        text += f'Session key k: {k}'
        self.info_frame.label.config(text=text)

    def __encrypt_msg(self):
        msg = self.message.get('1.0', 'end').strip()
        if msg:
            p, g, y = self.public_keys['p_encryption'], self.public_keys['g_encryption'], self.public_keys['y_encryption']
            C1, C2 = self.__sender.encrypt(msg, p, g, y)
            self.message.delete('1.0', 'end')
            self.message.insert('1.0', (str(C1) + ' ' + str(C2)))
            self.message.config(state='disabled')

    def __gen_signature_keys(self):
        p, q, a, v, s = self.__sender.gen_signature_keys()

        text = self.info_frame.label.cget('text')
        text += f'\nPrivate key x: {s}'
        self.info_frame.label.config(text=text)

        self.public_keys['p_signature'] = p
        self.public_keys['q_signature'] = q
        self.public_keys['a_signature'] = a
        self.public_keys['v_signature'] = v
        self.set_signature_keys()
        print('sender: ', self.public_keys)

    def __sign_up(self):
        C1, C2, e, y = self.__sender.sign_up()

        text = self.info_frame.label.cget('text')
        text += f'\nSuccessfully signed up.'
        self.info_frame.label.config(text=text)

        self.set_signature(C1, C2, e, y)

    def __create_widgets(self):
        text = [
            [('Generate session key', self.__gen_session_key), ('Generate keys for signature', self.__gen_signature_keys)],
            [('Encrypt', self.__encrypt_msg), ('Sign up', self.__sign_up)]
        ]
        button_frame = ButtonFrame(self, text)
        button_frame.grid(row=0, column=0)

        self.message = tk.Text(self, height=10, width=50)
        self.message.grid(row=1, column=0, pady=20)

        self.info_frame = InfoFrame(self)
        self.info_frame.grid(row=2, column=0)