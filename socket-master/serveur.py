import socket

KILL = "kill"
RESET = "reset"
DISCONNECT = "disconnect"

def serveur():
    data = ""
    conn = None
    server = None
    while data != KILL:
        data = ""
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        server.bind(("0.0.0.0", 10000))
        server.listen(1)
        print('Le serveur est en attente de connexion')
        while data != KILL and data != RESET:
            data = ""
            try:
                conn, addr = server.accept()
                print(addr)
            except ConnectionError:
                print("erreur de connection")
                break
            else:
                while data != KILL and data != RESET and data != DISCONNECT:
                    data = conn.recv(1024).decode()
                    print("Commande du client: ", data)
                    # data = input('Enter a message to send: ')
                    conn.send(data.encode())
                conn.close()
        print("Connection closed")
        server.close()
        print("Server closed")
