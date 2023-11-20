from PyQt5 import QtCore


class DebugCommunicator(QtCore.QObject):
    data_signal = QtCore.pyqtSignal(str, int)

