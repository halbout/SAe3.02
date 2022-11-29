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

        quit = QPushButton("Exit")
        lab1 = QLabel("Enter your command")
        self.__cmd = QLineEdit("")
        send = QPushButton("Send")
        help = QPushButton("Help")
        OS = QComboBox()
        OS.addItem("DOS")
        OS.addItem("Linux")
        OS.addItem("Powershell")
        lab2 = QLabel("Système \nd'exploitation")
        self.__res = QLabel("")

        grid.addWidget(quit, 4, 2)
        grid.addWidget(lab1, 0, 1)
        grid.addWidget(self.__cmd, 1, 1)
        grid.addWidget(send, 2, 1)
        grid.addWidget(help, 4, 0)
        grid.addWidget(OS, 1, 2)
        grid.addWidget(lab2, 0, 2)
        grid.addWidget(self.__res, 3, 1)

        quit.clicked.connect(self.__actionQuit)
        send.clicked.connect(self.__actionSend)
        help.clicked.connect(self.__actionHelp)
        self.setWindowTitle("Gestion des serveurs")


    def __actionQuit(self):
        QCoreApplication.exit(0)

    def __actionRes(self):
        client = socket.socket()
        client.connect(('127.0.0.1', 30000))
        self.__res = client.recv(1024).decode()
        client.close()

    def __actionSend(self):
        client = socket.socket()
        client.connect(('127.0.0.1', 30000))
        client.send(self.__cmd.encode())
        client.close()

    def __actionHelp(self):
        self.__message = QMessageBox()
        self.__message.setText("test")
        self.__message.setInformativeText("a")
        self.__message.setWindowTitle("Information")
        msg = self.__message.exec()

