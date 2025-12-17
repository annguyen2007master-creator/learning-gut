import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        #initial the app
        super().__init__()
        self.setWindowTitle("MyApp")

        #set up the outlook
        self.setGeometry(0, 0, 300, 300)
        self.setWindowIcon(QIcon("profile.jpg"))

        #font
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 50))
        label.setGeometry(0, 0, 300, 80)
        label.setStyleSheet("color: red;"
                            "background-color: black;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)


def main():
    #to run the app
    app = QApplication(sys.argv)
    window = MainWindow()

     #to show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()