import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QRadioButton, QButtonGroup)

class MainWindow(QMainWindow):
    def __init__(self):
        #initial the app
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(300, 300, 500, 500)
        self.radio1 = QRadioButton("Pokemon", self)
        self.radio2 = QRadioButton("Pikachu", self)
        self.radio3 = QRadioButton("toi ngu", self)
        self.buttonGroup1 = QButtonGroup(self)
        self.buttonGroup2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(100, 100, 500, 50)
        self.radio2.setGeometry(100, 150, 500, 50)
        self.radio3.setGeometry(100, 200, 500, 50)


        self.setStyleSheet("QRadioButton{"
                           "font-size:14px;"
                           "font-family: arial;"
                           "padding: 10px;"
                           "}")

        self.buttonGroup1.addButton(self.radio1)
        self.buttonGroup1.addButton(self.radio2)
        self.buttonGroup2.addButton(self.radio3)

        self.radio1.toggled.connect(self.radio_button_clicked)
        self.radio2.toggled.connect(self.radio_button_clicked)
        self.radio3.toggled.connect(self.radio_button_clicked)

    def radio_button_clicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

def main():
    #to run the app
    app = QApplication(sys.argv)
    window = MainWindow()

     #to show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()