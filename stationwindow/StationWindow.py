from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from stationwindow.StationWindowUi import StationWindowUi
from Station import Station
from Exception import AlreadyStationNumberException


class StationWindow(QWidget):

    def __init__(self, communicator, station_number, input_port, output_port):
        super().__init__()
        self.UI = StationWindowUi()
        self.initUI(input_port, output_port, station_number)
        # VAR
        self.station = Station(station_number, input_port, output_port, communicator, self.update_output_info)

    def initUI(self, input_port, output_port, station_number):
        self.UI.setupUi(self)
        self.UI.lbl_input_port.setText(input_port)
        self.UI.lbl_output_port.setText(output_port)
        self.update_station_number(station_number)
        self.add_function()

    def update_station_number(self, number):
        self.UI.lbl_station_number.setText(f"#{number}")

    def update_output_info(self, text):
        self.UI.txt_output.append(text)

    def get_station_number(self):
        try:
            number = int(self.UI.le_station_number.text())
        except ValueError:
            self.station.logger("The station number is not correct", 1)
        else:
            self.update_station_number(number)
            if number != self.station.number:
                self.station.logger(f"New station number is {number}", 1)
            else:
                self.station.logger(f"The station number is already {self.station.number}", 1)
            self.station.number = number
        finally:
            self.UI.le_station_number.clear()

    def get_address(self):
        try:
            address = int(self.UI.le_address.text())
        except ValueError:
            self.station.logger("The station address is not correct", 1)
        except AlreadyStationNumberException(self.station.number) as e:
            self.station.logger(e.what(), 1)
        else:
            self.station.address = address
            self.station.logger(f"The address of the receiver station is {address}", 1)

    def get_priority(self):
        try:
            priority = int(self.UI.cmb_priority.currentText())
        except ValueError:
            self.station.logger("The station priority is not correct", 1)
            pass
        else:
            self.station.priority = priority
            self.station.logger(f"The station priority is {priority}", 1)

    def get_message(self):
        try:
            text = self.UI.txt_input.toPlainText()
        except Exception:
            self.station.logger("Unknown error", 1)
        else:
            while True:
                if len(text) < 15:
                    self.station.send_data(text)
                    break
                else:
                    text_part = text[0:15]
                    text = text.replace(text_part, "")
                    self.station.send_data(text_part)
        finally:
            self.UI.txt_input.clear()

    def eventFilter(self, obj, event):
        if obj == self.UI.txt_input and event.type() == event.KeyPress:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.get_message()
                return True

        return super().eventFilter(obj, event)

    def add_function(self):
        self.UI.le_station_number.returnPressed.connect(lambda: self.get_station_number())
        self.UI.le_address.returnPressed.connect(lambda: self.get_address())
        self.UI.cmb_priority.activated.connect(lambda: self.get_priority())
        self.UI.txt_input.installEventFilter(self)
