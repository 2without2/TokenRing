import serial
from Frame import Frame
from Token import Token


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

    def CloseCOMPort(self):
        self.__portID.close()
        self.__init_flag = False

    def ReadPacketFromPort(self):
        data = self.__portID.read(32)
        accept_flag = False
        if data != b'':
            accept_flag = True
            # try:
            if len(data) <= 5:
                token: Token = Token()
                token.unpack(data)
                return token, accept_flag
            else:
                frame: Frame = Frame()
                frame.unpack(data)
                return frame, accept_flag
            # except Exception:
            #     print(f"{self.__port_name}: Reading failed")
        return Frame(), accept_flag

    def WritePacketToPort(self, obj):
        try:
            if isinstance(obj, Frame):
                frame: Frame = obj
                data = frame.pack()
                self.__portID.write(data)
            elif isinstance(obj, Token):
                token: Token = obj
                data = token.pack()
                self.__portID.write(data)
            else:
                print(f"{self.__port_name}: Token/Frame error")
        except Exception:
            print(f"{self.__port_name}: Recording failed")


    # Много разных параметров
    def SetParamCOMPort(self):
        try:
            self.__portID = serial.Serial(self.__port_name, baudrate=self.__baudrate, bytesize=8, parity='N',
                                          stopbits=1, timeout=1, xonxoff=False, rtscts=False)
            self.__init_flag = True
        except serial.SerialException as e:
            print(f"Error opening COM port: {str(e)}")
