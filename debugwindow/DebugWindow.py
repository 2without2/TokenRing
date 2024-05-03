from debugwindow.DebugWindowUi import DebugWindowUi
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore


class DebugWindow(QWidget):

    def __init__(self, communicator):
        super().__init__()
        self._UI = DebugWindowUi()
        self._UI.setupUi(self)
        self.add_function()

        self.communicator = communicator
        self.communicator.data_signal.connect(self.logger)

    def add_function(self):
        self._UI.btn_debug.clicked.connect(lambda: self._UI.txt_debug.clear())
        self._UI.btn_data.clicked.connect(lambda: self._UI.txt_data.clear())

    @QtCore.pyqtSlot(str, int)
    def logger(self, msg: str, mode: int):
        if mode == 1:
            self._UI.txt_debug.append(msg)
        elif mode == 2:
            self._UI.txt_data.append(msg)

