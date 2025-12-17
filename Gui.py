import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QLabel)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        #initial the app
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(300, 300, 500, 500)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Hit me", self)
        self.button.setGeometry(150, 150, 200, 200)
        self.button.setStyleSheet("font-size:30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 50, 200, 200)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet("font-size:30px;")

    def on_click(self):
        self.label.setText("You're GAY")


def main():
    #to run the app
    app = QApplication(sys.argv)
    window = MainWindow()

     #to show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()