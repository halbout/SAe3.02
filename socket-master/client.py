import socket

try:
    KILL = "kill"
    RESET = "reset"
    DISCONNECT = "disconnect"
    data = ""
    message = ""
    host = "localhost"
    port = 30000
    client = socket.socket()
    client.connect((host, port))

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
except ConnectionRefusedError:
    print("La connexion au serveur a été interrompue")
