import socket


class Client:

    socket = None

    def __init__(self):
        self.connectToLocal(6000)
        self.receiveAndSaveData()
        self.socket.close()

    def connectToLocal(self, port):
        self.socket = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = 60000  # Reserve a port for your service.
        self.socket.connect((host, port))

    def receiveAndSaveData(self):
        with open('received_file.txt', 'wb') as f:
            while True:
                data = self.socket.recv(1024)
                if not data:
                    break
                f.write(data)
        f.close()


client = Client()
