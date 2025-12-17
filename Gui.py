import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        #initial the app
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(300, 300, 500, 500)
        self.checkBox = QCheckBox("Do you like me?", self)
        self.initUI()

    def initUI(self):
        self.checkBox.setGeometry(0, 0, 300, 300)
        self.checkBox.setStyleSheet("font-size:20px;"
                                    "font-family:Verdana;")
        self.checkBox.setCheckState(False)
        self.checkBox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if Qt.CheckState(state):
            print("you gay")
        else:
            print("get outta here")
def main():
    #to run the app
    app = QApplication(sys.argv)
    window = MainWindow()

     #to show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()