import json
import tkinter
from tkinter import *

import requests

from view import home


class LoginWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x250')
        self.title('Login')
        self.resizable(False, False)

        Label(self, text="Name").pack()
        self.username_text = Text(self, bg="gray", height=1, width=20)
        self.username_text.pack()

        Label(self, text="Password").pack()
        self.password_text = Entry(self,)
        self.password_text.configure(bg="gray", show="*")
        self.password_text.place(height=1)
        self.password_text.pack()

        Button(self, text="Login", command=self.send_login_info).pack()

        home.destroy_home_window()
        self.mainloop()

    def send_login_info(self):
        username = self.username_text.get("1.0", "end-1c")
        password = self.password_text.get()

        data = {"username": username, "password": password}

        requests.post("http://127.0.0.1:8000/login", data=json.dumps(data))
