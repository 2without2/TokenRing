from window.ControlWindow import ControlWindow
from PyQt5 import QtWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    control_window = ControlWindow()
    control_window.init_ui(window)
    window.show()
    sys.exit(app.exec_())
