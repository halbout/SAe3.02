import socket
import threading

KILL = "kill"
RESET = "reset"
DISCONNECT = "disconnect"

class Client():
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__client = socket.socket()
        self.__thread = None

    def connect(self) -> int:
        try:
            self.__client.connect((self.__host, self.__port))
        except ConnectionRefusedError:
            print("serveur non disponible ou mauvaise saisie")
            return -1
        except ConnectionError:
            print("erreur de connection")
            return -1
        else:
            print("connexion réussie")
            return 0

    def echange(self):
        cmd = ""
        self.__thread = threading.Thread(target=self.__recue, args=[self.__client, ])
        self.__thread.start()
        while cmd != KILL and cmd != DISCONNECT and cmd != RESET:
            cmd = self.__envoi()
        self.__thread.join()
        self.__client.close()

    def __envoi(self):
        cmd = input("Commande :")
        try:
            self.__client.send(cmd.encode())
        except BrokenPipeError:
            print("connection fermé")
        return cmd

    def __recue(self, conn):
        res = ""
        while res != KILL and res != DISCONNECT and res != RESET:
            res = conn.recv(1024).decode()
            print(res)
