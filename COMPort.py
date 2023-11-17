import serial
from Frame import Frame


class COMPort:
    __portID: serial.Serial = None
    __port_name: str = None
    __baudrate: int = None
    __init_flag: bool

    def __init__(self, port_name: str, baudrate: int = 9600):
        self.__port_name = port_name
        self.__baudrate = baudrate
        self.__init_flag = False

    @property
    def port_name(self):
        return self.__port_name

    @port_name.setter
    def port_name(self, port_name: str):
        self.__port_name = port_name

    @property
    def baudrate(self):
        return self.__baudrate

    @baudrate.setter
    def baudrate(self, baudrate: int):
        self.__baudrate = baudrate

    @property
    def init_flag(self):
        return self.__init_flag

    @init_flag.setter
    def init_flag(self, init_flag: bool):
        self.__init_flag = init_flag

    def InitCOMPort(self):
        self.__portID = serial.Serial(self.__port_name, baudrate=self.__baudrate)
        self.__init_flag = True

    def CloseCOMPort(self):
        self.__portID.close()
        self.__init_flag = False

    def ReadFromPort(self):
        data = self.__portID.read(10)
        return data

    def ReadPacketFromPort(self):
        data = self.__portID.read(36)
        temp_frame: Frame = Frame()
        if data != b'':
            temp_frame.unpack(data)
        return temp_frame

    def ReadBytesFromPort(self):
        data = self.__portID.read(36)
        return data

    def WriteToPort(self, message: str):
        sends = bytes(message, 'utf-8')
        self.__portID.write(sends)

    def WritePacketToPort(self, frame: Frame):
        data = frame.pack()
        self.__portID.write(data)

    # Много разных параметров
    def SetParamCOMPort(self):
        try:
            self.__portID = serial.Serial(self.__port_name, baudrate=self.__baudrate, bytesize=8, parity='N', stopbits=1,
                                      timeout=1, xonxoff=False, rtscts=False)
            self.__init_flag = True
        except serial.SerialException as e:
            print(f"Error opening COM port: {str(e)}")
