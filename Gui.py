import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QLabel, QPushButton,)

class MainWindow(QMainWindow):
    def __init__(self):
        #initial the app
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(300, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.label = QLabel("toi bi dien co nao: ", self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.label.setGeometry(10,0,300,50)
        self.line_edit.setGeometry(10, 50, 300, 50)
        self.button.setGeometry(310, 50, 125, 50)
        self.label.setStyleSheet("font-size:25px;"
                                     "font-family:Verdana;")
        self.line_edit.setStyleSheet("font-size:25px;"
                                     "font-family:Verdana;")
        self.button.setStyleSheet("font-size:25px;"
                                     "font-family:Verdana;")
        self.line_edit.setPlaceholderText("how you stupid")
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"ban ngu co {text}")


def main():
    #to run the app
    app = QApplication(sys.argv)
    window = MainWindow()

     #to show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()