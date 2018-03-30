import socket


class Server:
    socket = None

    def __init__(self):
        port = 60000  # Reserve a port for your service.
        self.socket = self.startLocal(port)
        self.listen()
        while True:
            self.connectToClient()

    def startLocal(self, port):
        sock = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        sock.bind((host, port))  # Bind to the port
        return sock

    def listen(self):
        self.socket.listen(5)  # Now wait for client connection.

    def getDataToSend(self, filename, size):
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        return data

    def connectToClient(self):
        conn, addr = self.socket.accept()  # Establish connection with client.
        conn.send(self.getDataToSend('TestData.txt', 1024))
        conn.close()
        print('connection closed')


server = Server()
