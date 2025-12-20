#Weather App
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel( self)
        self.emoji_label = QLabel( self)
        self.description_label = QLabel( self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(600, 600, 300, 300)
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.city_input.setFixedSize(300, 45)

        self.setStyleSheet("""
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
                height: 30px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
                border-radius: 5px;
                border: 1px solid gray;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 80px;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "dcfe492797437eda14cd5bbffd5f5b7e"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_info(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden\nAccess is denied")
                case 404:
                    self.display_error("Not found\nCity not found")
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway\nInvalid response from server")
                case 503:
                    self.display_error("Service Unavailable\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout\nServer is down")
                case _:
                   self.display_error("Something went wrong\nPlease try again later")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\nPlease check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nCheck the url")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error\n{req_error}")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_info(self, data):
        self.temperature_label.setStyleSheet("font-size:75px;")
        temperature_f = data["main"]["temp"] * 9/5.0 - 459.67
        print(temperature_f)
        self.temperature_label.setText(f"{temperature_f:.2f}°F")

        weather_description = data["weather"][0]["description"]
        self.description_label.setText(f"{weather_description}")

        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
        match weather_id:
            case x if 200 <= x <= 232:
                return "🌩"
            case x if 300 <= x <= 321:
                return "⛈️"
            case x if 500 <= x <= 531:
                return "🌧️"
            case x if 600 <= x <= 622:
                return "❄️"
            case x if 701 <= x <= 741:
                return "💨"
            case 762:
                return "🌋"
            case 771:
                return "💨"
            case 781:
                return "🌪️"
            case 800:
                return "☀"
            case x if 801 <= x <= 804:
                return "☁"
            case _:
                return ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather = WeatherApp()
    weather.show()
    sys.exit(app.exec_())