from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        quit = QPushButton("Exit")
        lab = QLabel("Enter your command")
        command = QLineEdit("")
        send = QPushButton("Send")
        help = QPushButton("?")

        grid.addWidget(quit, 3, 0)
        grid.addWidget(lab, 0, 1)
        grid.addWidget(command, 1, 1)
        grid.addWidget(send, 2, 1)
        grid.addWidget(help, 3, 2)

        quit.clicked.connect(self.__actionQuit)
        #send.clicked.connect(self.__actionSend)
        help.clicked.connect(self.__actionHelp)
        self.setWindowTitle("Gestion des serveurs")

    def __actionQuit(self):
        QCoreApplication.exit(0)

    def __actionHelp(self):
        self.__message = QMessageBox
