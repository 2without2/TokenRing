from debugwindow.DebugWindow import DebugWindow
from stationwindow.StationWindow import StationWindow
from PyQt5.QtWidgets import QApplication
import sys
from Communicator import DebugCommunicator

if __name__ == "__main__":
    app = QApplication(sys.argv)

    communicator = DebugCommunicator()

    debug_window = DebugWindow(communicator)

    station_window_1 = StationWindow(communicator, 0, "COM11", "COM16")
    station_window_2 = StationWindow(communicator, 1, "COM13", "COM12")
    station_window_3 = StationWindow(communicator, 2, "COM15", "COM14")

    debug_window.show()
    station_window_1.show()
    station_window_2.show()
    station_window_3.show()

    sys.exit(app.exec_())

