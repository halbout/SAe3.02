from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QComboBox


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        quit = QPushButton("Exit")
        lab1 = QLabel("Enter your command")
        command = QLineEdit("")
        send = QPushButton("Send")
        help = QPushButton("Help")
        OS = QComboBox()
        OS.addItem("DOS")
        OS.addItem("Linux")
        OS.addItem("Powershell")
        lab2 = QLabel("Système \nd'exploitation")

        grid.addWidget(quit, 4, 2)
        grid.addWidget(lab1, 0, 1)
        grid.addWidget(command, 1, 1)
        grid.addWidget(send, 2, 1)
        grid.addWidget(help, 4, 0)
        grid.addWidget(OS, 1, 2)
        grid.addWidget(lab2, 0, 2)

        quit.clicked.connect(self.__actionQuit)
        #send.clicked.connect(self.__actionSend)
        help.clicked.connect(self.__actionHelp)
        self.setWindowTitle("Gestion des serveurs")

    def __actionQuit(self):
        QCoreApplication.exit(0)

    def __actionHelp(self):
        self.__message = QMessageBox()
        self.__message.setText("test")
        self.__message.setInformativeText("a")
        self.__message.setWindowTitle("Information")
        msg = self.__message.exec()
