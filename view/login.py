import json
import tkinter
from tkinter import *

import requests


from view import home_page
from view.global_chat import GlobalPage


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

        home_page.destroy_home_window()
        self.mainloop()

    def send_login_info(self):
        username = self.username_text.get("1.0", "end-1c")
        password = self.password_text.get()

        data = {"username": username, "password": password}

        request = requests.post("http://127.0.0.1:8000/login", data=json.dumps(data))
        if request:
            self.destroy()
            global_page = GlobalPage()
            global_page.update()
            global_page.update_idletasks()
        else:
            self.wrong_info_popup()

    def wrong_info_popup(self):
        popup = Toplevel(self)
        popup.geometry("400x70")
        popup.title("Wrong info")
        Label(popup, text="Incorrect username or password", font='Mistral 12 bold').pack()
        Button(popup, text="Okay", command=popup.destroy).pack()
        self.mainloop()
