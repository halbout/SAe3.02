import sys
from PyQt5.QtWidgets import QApplication
from GUI import Client

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Client()
    window.show()

    app.exec()
