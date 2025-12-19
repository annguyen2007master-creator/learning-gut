import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout,)

class MainWindow(QMainWindow):
    def __init__(self):
        #initial the app
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(300, 300, 500, 500)

        self.button1 = QPushButton("NGU 1")
        self.button2 = QPushButton("NGU 2")
        self.button3 = QPushButton("NGU 3")

        self.initUI()


    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Verdana;
                padding: 5px;
                margin: 5px;
                border: 5px solid gray;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: green;
            } 
            QPushButton#button2{
                background-color: blue;
            } 
            QPushButton#button3{
                background-color: purple;
            }
            QPushButton#button1:hover{
                background-color: gray;
            } 
            QPushButton#button2:hover{
                background-color: gray;
            } 
            QPushButton#button3:hover{
                background-color: gray;
            }  
        """)


def main():
    #to run the app
    app = QApplication(sys.argv)
    window = MainWindow()

     #to show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()