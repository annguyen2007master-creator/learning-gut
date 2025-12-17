import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        #initial the app
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(300, 300, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 150)

        pixmap = QPixmap("profile.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) //  2,
                          label.width(),
                          label.height())

def main():
    #to run the app
    app = QApplication(sys.argv)
    window = MainWindow()

     #to show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()