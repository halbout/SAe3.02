import socket

try:
    KILL = "kill"
    RESET = "reset"
    DISCONNECT = "disconnect"
    data = ""
    message = ""
    client = socket.socket()
    client.connect(('127.0.0.1', 10000))

    while message != KILL and message != RESET and message != DISCONNECT and data != KILL and data != RESET and data != DISCONNECT:
        message = input("")
        client.send(message.encode())
        data = client.recv(1024).decode()
        print(data)

    client.close()

except KeyboardInterrupt:
    print("La connexion au serveur a été interrompue")

except ConnectionResetError:
    print("La connexion au serveur a été interrompue")