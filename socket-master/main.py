import sys
import client

if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) < 3:
        client = Client("0.0.0.0", 10000)
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        client = Client(host, port)

    client.start()
    client.join()

    client.connect()
    client.echange()
