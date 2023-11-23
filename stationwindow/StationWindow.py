from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from stationwindow.StationWindowUi import StationWindowUi
from Station import Station
from Exception import AlreadyStationNumberException


class StationWindow(QWidget):

    def __init__(self, communicator, station_number, input_port, output_port):
        super().__init__()
        self.UI = StationWindowUi()
        self.initUI(input_port, output_port, station_number)
        # VAR
        self.station = Station(station_number, input_port, output_port, communicator, self.update_output_info,
                               self.update_package_count)

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

    def update_package_count(self):
        self.UI.lbl_package_count.setText(str(self.station.buffer.count()))

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
            self.station.logger(f"The address of the receiver station is {self.station.address}", 1)

    def get_priority(self):
        try:
            priority = int(self.UI.cmb_priority.currentText())
        except ValueError:
            self.station.logger("The station priority is not correct", 1)
            pass
        else:
            self.station.priority = priority
            self.station.logger(f"The station priority is {self.station.priority}", 1)

    def get_message(self):
        try:
            text = self.UI.txt_input.toPlainText()
        except Exception:
            self.station.logger("Unknown error", 1)
        else:
            while True:
                if len(text) < 15:
                    self.station.buffer.add(text)
                    break
                else:
                    text_part = text[0:15]
                    text = text.replace(text_part, "")
                    self.station.buffer.add(text_part)
        finally:
            self.UI.txt_input.clear()

    def eventFilter(self, obj, event):
        if obj == self.UI.txt_input and event.type() == event.KeyPress:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.get_message()
                self.update_package_count()
                return True

        return super().eventFilter(obj, event)

    def generate_token(self):
        if self.station.isMonitor:
            if not self.station.init_token:
                # send token
                self.station.send_token()
                self.station.init_token = True
                self.UI.lbl_token_status.setText("TRUE")
                self.station.logger("The token has been generated", 2)
            else:
                self.station.logger("The token has already been created", 1)
        else:
            self.station.logger(f"The station is not a monitor station", 1)

    def delete_token(self):
        if self.station.isMonitor:
            if self.station.init_token:
                self.station.init_token = False
                self.UI.lbl_token_status.setText("FALSE")
            else:
                self.station.logger("The token was not created", 1)
        else:
            self.station.logger(f"The station is not a monitor station", 1)

    def get_monitor_flag(self, state):
        if state == 2:
            self.station.isMonitor = True
            self.station.logger(f"Station-Monitor is enable", 1)
        else:
            self.station.isMonitor = False
            self.station.logger(f"Station-Monitor is disable", 1)

    def add_function(self):
        # usually
        self.UI.le_station_number.returnPressed.connect(lambda: self.get_station_number())
        self.UI.le_address.returnPressed.connect(lambda: self.get_address())
        self.UI.cmb_priority.activated.connect(lambda: self.get_priority())
        self.UI.txt_input.installEventFilter(self)
        # modify
        self.UI.btn_generate.clicked.connect(lambda: self.generate_token())
        self.UI.btn_delete.clicked.connect(lambda: self.delete_token())
        self.UI.chb_monitor.stateChanged.connect(self.get_monitor_flag)
