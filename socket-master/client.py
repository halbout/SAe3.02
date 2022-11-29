import socket

try:

    BYE = "bye"
    ARRET = "arret"
    data = ""
    while data != BYE and data != ARRET:
        message = ""
        client_socket = socket.socket()
        client_socket.connect(('127.0.0.1', 10000))

        while message != BYE and message != ARRET and data != BYE and data != ARRET:
            message = input("")
            client_socket.send(message.encode())

        client_socket.close()

except KeyboardInterrupt:
    print("La connexion au serveur a été interrompue")

except ConnectionResetError:
    print("La connexion au serveur a été interrompue")