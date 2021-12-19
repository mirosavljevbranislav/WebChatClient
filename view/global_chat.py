import json
import tkinter
import tkinter.scrolledtext
from tkinter import *

import requests


class GlobalPage(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("Global chat")
        self.resizable(False, False)

        Label(self, text="Chat: ")
        self.text_area = tkinter.scrolledtext.ScrolledText(self)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        self.input_area = Text(self, height=5)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = Button(self, text="Send", command=self.send_message)
        self.send_button.pack(padx=20, pady=6)
        self.mainloop()

    def send_message(self):
        written_message = self.input_area.get("1.0", 'end-1c')
        message_data = {"data": written_message,
                        "username": "Test username"}
        self.text_area.insert('end', written_message)
        # r = requests.post("http://127.0.0.1:8000/ws", data=json.dumps(message_data))
        # print(r.text)
