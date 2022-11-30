import socket

try:
    KILL = "kill"
    RESET = "reset"
    DISCONNECT = "disconnect"
    res = ""
    cmd = ""
    host = "localhost"
    port = 30000
    server = socket.socket()
    while res != KILL and cmd != KILL:
        server.bind((host, port))
        server.listen(1)

        while res != KILL and cmd != KILL and res != RESET and cmd != RESET:
            conn, address = server.accept()
            res = cmd = ""

            while res != KILL and cmd != KILL and res != RESET and cmd != RESET and res != DISCONNECT and cmd != DISCONNECT:
                cmd = conn.recv(1024).decode()
                print(cmd)
                if cmd == DISCONNECT:
                    res = DISCONNECT
                    conn.send(res.encode())
                elif cmd == RESET:
                    res = RESET
                    conn.send(res.encode())
                elif cmd == KILL:
                    res = KILL
                    conn.send(res.encode())
                else:
                    res = input("")

            conn.close()
    server.close()

except ConnectionAbortedError:
    print("Le connexion au client a été interrompue")
except ConnectionResetError:
    print("Le connexion au client a été interrompue")
except KeyboardInterrupt:
    print("Le connexion au client a été interrompue")
