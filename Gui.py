import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        #initial the app
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(300, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Pokemon1", self)
        label2 = QLabel("Pokemon2", self)
        label3 = QLabel("Pokemon3", self)
        label4 = QLabel("Pokemon4", self)
        label5 = QLabel("Pokemon5", self)
        label1.setStyleSheet("background-color:purple")
        label2.setStyleSheet("background-color:red")
        label3.setStyleSheet("background-color:yellow")
        label4.setStyleSheet("background-color:green")
        label5.setStyleSheet("background-color:blue")

        vbox = QHBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)


def main():
    #to run the app
    app = QApplication(sys.argv)
    window = MainWindow()

     #to show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()