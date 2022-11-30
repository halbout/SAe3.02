from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QComboBox
import socket


class Client(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        exit = QPushButton("Exit")
        lab1 = QLabel("Enter your command")
        self.__cmd = QLineEdit("")
        self.__Send = QPushButton("Send")
        help = QPushButton("Help")
        OS = QComboBox()
        OS.addItem("DOS")
        OS.addItem("Linux")
        OS.addItem("Powershell")
        lab2 = QLabel("Système \nd'exploitation")

        grid.addWidget(exit, 4, 2)
        grid.addWidget(lab1, 0, 1)
        grid.addWidget(self.__cmd, 1, 1)
        grid.addWidget(self.__Send, 2, 1)
        grid.addWidget(help, 4, 0)
        grid.addWidget(OS, 1, 2)
        grid.addWidget(lab2, 0, 2)

        exit.clicked.connect(self.__actionQuit)
        self.__Send.clicked.connect(self.__actionSend)
        help.clicked.connect(self.__actionHelp)
        self.setWindowTitle("Gestion des serveurs")

    def __actionQuit(self):
        QCoreApplication.exit(0)

    def __actionSend(self):
        host = "localhost"
        port = 30000
        client = socket.socket()
        client.connect((host, port))
        client.send(self.__Send.encode())
        res = QMessageBox()
        res.setWindowTitle("Résultats")
        res.setText(client.recv(1024).decode())
        client.close()
        resultat = res.exec()

    def __actionHelp(self):
        self.__message = QMessageBox()
        self.__message.setText("Ces indications peuvent vous aidez à mieux comprendre le fonctionnement de cette interface graphique.\n \nDans un premier temps choisissez votre système d'exploitation via le menu déroulant.\n \nEnsuite tapez une commande dans la zone de texte approprié parmi les suivantes : RAM, CPU, IP, Name."
                               "\n \nVous pouvez également tapez des commandes de création et de suppression sur les serveurs")
        self.__message.setWindowTitle("Guide d'utilisation")
        msg = self.__message.exec()
