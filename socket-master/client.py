import socket
import threading


def reception(client_socket):
    data = ""
    while data != BYE and data != ARRET:
        data = client_socket.recv(1024).decode()
        print(data)

try:
    BYE = "bye"
    ARRET = "arret"
    message = ""
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 10000))

    t1 = threading.Thread(target=reception, args=[client_socket])
    t1.start()

    while message != BYE and message != ARRET and data != BYE and data != ARRET:
        message = input("")
        client_socket.send(message.encode())

    t1.join()
    client_socket.close()

except KeyboardInterrupt:
    print("La connexion au serveur a été interrompue")

except ConnectionResetError:
    print("La connexion au serveur a été interrompue")