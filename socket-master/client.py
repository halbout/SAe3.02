import socket

try:

    def sendCmd(client_socket):

        BYE = "bye"
        ARRET = "arret"
        message = ""
        client = socket.socket()
        client.connect(('127.0.0.1', 10000))

        while message != BYE and message != ARRET and data != BYE and data != ARRET:
            message = input("")
            client.send(message.encode())

        client.close()

except KeyboardInterrupt:
    print("La connexion au serveur a été interrompue")

except ConnectionResetError:
    print("La connexion au serveur a été interrompue")