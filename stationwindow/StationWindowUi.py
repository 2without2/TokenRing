from PyQt5 import QtCore, QtGui, QtWidgets


class StationWindowUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 485)
        Form.setMinimumSize(QtCore.QSize(660, 485))
        Form.setMaximumSize(QtCore.QSize(660, 485))
        Form.setStyleSheet("background-color: rgb(232, 232, 170);\n""")
        self.txt_input = QtWidgets.QTextEdit(Form)
        self.txt_input.setGeometry(QtCore.QRect(30, 40, 291, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_input.setFont(font)
        self.txt_input.setStyleSheet("background-color: rgb(255, 255, 180);")
        self.txt_input.setObjectName("txt_input")
        self.txt_output = QtWidgets.QTextBrowser(Form)
        self.txt_output.setGeometry(QtCore.QRect(339, 40, 291, 192))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_output.setFont(font)
        self.txt_output.setStyleSheet("background-color: rgb(255, 255, 180);")
        self.txt_output.setObjectName("txt_output")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(125, 5, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(445, 5, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lbl_input_port = QtWidgets.QLabel(Form)
        self.lbl_input_port.setGeometry(QtCore.QRect(190, 400, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_input_port.setFont(font)
        self.lbl_input_port.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_input_port.setObjectName("lbl_input_port")
        self.lbl_output_port = QtWidgets.QLabel(Form)
        self.lbl_output_port.setGeometry(QtCore.QRect(190, 440, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_output_port.setFont(font)
        self.lbl_output_port.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_output_port.setObjectName("lbl_output_port")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(50, 400, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(50, 440, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(370, 240, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.chb_monitor = QtWidgets.QCheckBox(Form)
        self.chb_monitor.setGeometry(QtCore.QRect(350, 280, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chb_monitor.setFont(font)
        self.chb_monitor.setObjectName("chb_monitor")
        self.btn_generate = QtWidgets.QPushButton(Form)
        self.btn_generate.setGeometry(QtCore.QRect(350, 360, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet("background-color: rgb(220, 212, 147);")
        self.btn_generate.setObjectName("btn_generate")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(370, 320, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setGeometry(QtCore.QRect(490, 360, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("background-color: rgb(220, 212, 147);")
        self.btn_delete.setObjectName("btn_delete")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(350, 400, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.lbl_token_status = QtWidgets.QLabel(Form)
        self.lbl_token_status.setGeometry(QtCore.QRect(500, 400, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_token_status.setFont(font)
        self.lbl_token_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_token_status.setObjectName("lbl_token_status")
        self.le_station_number = QtWidgets.QLineEdit(Form)
        self.le_station_number.setGeometry(QtCore.QRect(190, 280, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le_station_number.setFont(font)
        self.le_station_number.setObjectName("le_station_number")
        self.le_address = QtWidgets.QLineEdit(Form)
        self.le_address.setGeometry(QtCore.QRect(190, 320, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le_address.setFont(font)
        self.le_address.setObjectName("le_address")
        self.lbl_station_number = QtWidgets.QLabel(Form)
        self.lbl_station_number.setGeometry(QtCore.QRect(270, 5, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_station_number.setFont(font)
        self.lbl_station_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_station_number.setObjectName("lbl_station_number")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(50, 360, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.cmb_priority = QtWidgets.QComboBox(Form)
        self.cmb_priority.setGeometry(QtCore.QRect(190, 360, 113, 31))
        self.cmb_priority.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cmb_priority.setFont(font)
        self.cmb_priority.setObjectName("cmb_priority")
        self.cmb_priority.addItem("")
        self.cmb_priority.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "StationForm"))
        self.label.setText(_translate("Form", "Input"))
        self.label_2.setText(_translate("Form", "Output"))
        self.lbl_input_port.setText(_translate("Form", "COM11"))
        self.lbl_output_port.setText(_translate("Form", "COM16"))
        self.label_5.setText(_translate("Form", "Station number:"))
        self.label_6.setText(_translate("Form", "Address to send:"))
        self.label_7.setText(_translate("Form", "Station Settings:"))
        self.label_8.setText(_translate("Form", "Input port:"))
        self.label_9.setText(_translate("Form", "Output port:"))
        self.label_11.setText(_translate("Form", "Monitor Station Settings:"))
        self.chb_monitor.setText(_translate("Form", "Enable/Disable monitor function"))
        self.btn_generate.setText(_translate("Form", "Generate token"))
        self.label_12.setText(_translate("Form", "Token settings:"))
        self.btn_delete.setText(_translate("Form", "Delete token"))
        self.label_13.setText(_translate("Form", "Token status:"))
        self.lbl_token_status.setText(_translate("Form", "FALSE"))
        self.lbl_station_number.setText(_translate("Form", "#0"))
        self.label_15.setText(_translate("Form", "Priority level:"))
        self.cmb_priority.setItemText(0, _translate("Form", "1"))
        self.cmb_priority.setItemText(1, _translate("Form", "2"))
