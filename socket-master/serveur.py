import socket

try:
    KILL = "kill"
    RESET = "reset"
    DISCONNECT = "disconnect"
    res = ""
    cmd = ""
    while res != KILL and cmd != KILL:
        server = socket.socket()
        server.bind(('127.0.0.1', 10000))
        while res != KILL and cmd != KILL and res != RESET and cmd != RESET:
            server.listen(1)
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
