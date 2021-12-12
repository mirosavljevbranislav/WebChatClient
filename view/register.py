import json
import tkinter
from tkinter import *
import requests


class RegisterWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x250')
        self.title('Register')
        self.resizable(False, False)

        Label(self, text="Username").pack()
        self.username_entry = Text(self, bg="gray", height=1, width=20)
        self.username_entry.pack()

        Label(self, text="Password").pack()
        self.password_entry = Entry(self,)
        self.password_entry.configure(bg="gray", show="*")
        self.password_entry.place(height=1)
        self.password_entry.pack()

        Label(self, text="Name").pack()
        self.fullname_entry = Text(self, bg="gray", height=1, width=20)
        self.fullname_entry.pack()

        Label(self, text="Last name").pack()
        self.lastname_entry = Text(self, bg="gray", height=1, width=20)
        self.lastname_entry.pack()

        Button(self, text="Register", command=self.store_user_request).pack()
        self.mainloop()

    def store_user_request(self):
        """
        Takes text from text-fields and adds them to dictionary and then passes it to request
        :return: None
        """
        username = self.username_entry.get("1.0", "end-1c")
        password = self.password_entry.get()
        fullname = self.fullname_entry.get("1.0", "end-1c")
        lastname = self.lastname_entry.get("1.0", "end-1c")

        data = {"username": username,
                "password": password,
                "full_name": fullname,
                "last_name": lastname}
        print(data)
        requests.post("http://127.0.0.1:8000/register", data=json.dumps(data))
