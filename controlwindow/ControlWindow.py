from controlwindow.ControlWindowUi import ControlWindowUi
from Exception import (StationPortsException, StationNumberException, MaxStationNumberException)
from PyQt5 import QtWidgets

MAX_STATION_NUMBER = 5


def choose_ports(ports):
    if ports == "COM1 <-> COM2":
        return "COM1", "COM2"
    elif ports == "COM3 <-> COM4":
        return "COM3", "COM4"
    elif ports == "COM5 <-> COM6":
        return "COM5", "COM6"
    elif ports == "COM7 <-> COM8":
        return "COM7", "COM8"
    elif ports == "COM9 <-> COM10":
        return "COM9", "COM10"


def create_id(dict: dict):
    for id in range(0, MAX_STATION_NUMBER):
        if id in dict:
            continue
        else:
            return id

    raise MaxStationNumberException(MAX_STATION_NUMBER)


def update_station_list(dict, txt):
    html: str = """
    <table width="100%" style="width:100%;">
        <tr>
            <th align="center">ID</th>
            <th align="center">Station number</th>
            <th align="center">Input port</th>
            <th align="center"> Output port</th>
        </tr>
    """

    for key, value in dict.items():
        input_port, output_port = choose_ports(value[1])
        html += f"""
        <tr>
            <td align="center">{key}</td>
            <td align="center">{value[0]}</td>
            <td align="center">{input_port}</td>
            <td align="center">{output_port}</td>
        </tr>
        """

    html += "</table>"

    txt.setHtml(html)


class ControlWindow:

    def __init__(self):
        self.UI = ControlWindowUi()
        self.station_dict = dict()

    def init_ui(self, window):
        self.UI.setupUi(window)
        self.add_function()

    def create_window(self):
        try:
            id = create_id(self.station_dict)
            ports = self.UI.cmb_box_ports.currentText()
            station_number = int(self.UI.le_create.text())

            if self.station_dict:
                for value in self.station_dict.values():
                    if value[0] == station_number:
                        raise StationNumberException(value[0])
                    if value[1] == ports:
                        raise StationPortsException(value[1])

            input_port, output_port = choose_ports(self.UI.cmb_box_ports.currentText())

        except ValueError:
            self.UI.txt_debug.append(f"The station number is not correct")
        except StationPortsException as e:
            self.UI.txt_debug.append(e.error())
        except StationNumberException as e:
            self.UI.txt_debug.append(e.error())
        except MaxStationNumberException as e:
            self.UI.txt_debug.append(e.error())

        # create ControlWindow
        else:
            self.UI.txt_debug.append(f"The station with id = {id} has been created")
            self.UI.bar_maxnumb.setValue(self.UI.bar_maxnumb.value() + int(100 / MAX_STATION_NUMBER))
            self.station_dict[id] = [station_number, ports]
            update_station_list(self.station_dict, self.UI.txt_stations)
        finally:
            self.UI.le_create.clear()

    def delete_window(self):
        try:
            station_number = int(self.UI.le_delete.text())
            id: int = -1

            for key, value in self.station_dict.items():
                if value[0] == station_number:
                    id = key
                    break

            if id == -1:
                raise KeyError

        except ValueError:
            self.UI.txt_debug.append(f"The station number is not correct")
        except KeyError:
            self.UI.txt_debug.append(f"The station with the number = {station_number} does not exist")

        # delete ControlWindow
        else:
            self.UI.txt_debug.append(f"The station with id = {id} has been deleted")
            self.UI.bar_maxnumb.setValue(self.UI.bar_maxnumb.value() - 100 / MAX_STATION_NUMBER)
            del self.station_dict[id]
            update_station_list(self.station_dict, self.UI.txt_stations)

        finally:
            self.UI.le_delete.clear()

    def add_function(self):
        self.UI.btn_create.clicked.connect(lambda: self.create_window())
        self.UI.btn_delete.clicked.connect(lambda: self.delete_window())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    control_window = ControlWindow()
    control_window.init_ui(window)
    window.show()
    sys.exit(app.exec_())
