import socket
import threading

try:
    BYE = "bye"
    ARRET = "arret"
    reply = ""
    data = ""
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 10000))
    server_socket.listen(1)
    while reply != ARRET and data != ARRET:
        conn, address = server_socket.accept()
        reply = data = ""

        while reply != BYE and data != BYE and reply != ARRET and data != ARRET:
            data = conn.recv(1024).decode()
            print(data)
            if data == BYE:
                reply = BYE
                conn.send(reply.encode())
            elif data == ARRET:
                reply = ARRET
                conn.send(reply.encode())
            else:
                start = reply = input("")

                t1 = threading.Thread()
                t1.start()
                t1.join()

                end = conn.send(reply.encode())

        conn.close()
    server_socket.close()

except ConnectionAbortedError:
    print("Le connexion au client a été interrompue")
