import socket
from view import home

HOST = 'localhost'
PORT = 8000


class Client:

    def __init__(self, host, port):
        print("Client connected!")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        home.create_home_page()


client = Client(HOST, PORT)
