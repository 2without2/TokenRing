from debugwindow.DebugWindowUi import DebugWindowUi
from PyQt5.QtWidgets import QWidget


class DebugWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.UI = DebugWindowUi()
        self.UI.setupUi(self)
        self.add_function()

    def add_function(self):
        self.UI.btn_debug.clicked.connect(lambda: self.UI.txt_debug.clear())
        self.UI.btn_data.clicked.connect(lambda: self.UI.txt_data.clear())

    def logger1(self, msg: str):
        self.UI.txt_debug.append(msg)

    def logger2(self, msg: str):
        self.UI.txt_data.append(msg)
