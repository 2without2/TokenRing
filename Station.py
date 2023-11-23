from COMPort import COMPort
from Frame import Frame
from Token import Token
from Communicator import DebugCommunicator
from Buffer import Buffer
import threading


class Station:
    def __init__(self, number: int, input_port: str, output_port: str, communicator: DebugCommunicator,
                 function, function1, priority: int = 1):
        # var
        self.input_port: COMPort = COMPort(input_port)
        self.output_port: COMPort = COMPort(output_port)
        self.buffer: Buffer = Buffer()
        self.__number = number
        self.__address = number
        self.__priority = priority
        self.__isMonitor = False
        self.__init_token = False
        self.initStation()

        self.debug_communicator = communicator
        self.callback_function = function
        self.callback_function1 = function1

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: int):
        self.__address = address

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def isMonitor(self):
        return self.__isMonitor

    @isMonitor.setter
    def isMonitor(self, flag):
        self.__isMonitor = flag

    @property
    def init_token(self):
        return self.__init_token

    @init_token.setter
    def init_token(self, flag):
        self.__init_token = flag

    def logger(self, data, mode):
        self.debug_communicator.data_signal.emit(f"Station #{self.__number}: {data}", mode)

    def update_info(self, text: str):
        self.callback_function(text)

    def update_package_count(self):
        self.callback_function1()

    def initStation(self):
        self.input_port.SetParamCOMPort()
        self.output_port.SetParamCOMPort()
        self.accept_data()

    def closeStation(self):
        self.input_port.CloseCOMPort()
        self.output_port.CloseCOMPort()

    def send_token(self):
        token: Token = Token()
        token.curr_prior = self.__priority
        token.sour_addr = self.__number
        self.input_port.WritePacketToPort(token)
        self.logger(f"The token was sent to Station #{self.__address}", 2)

    def parse_frame(self, frame):

        print(f"Station #{self.__number}: Frame source_addr = {frame.source_addr}")
        print(f"Station #{self.__number}: Frame dest_addr = {frame.dest_addr}")
        print(f"Station #{self.__number}: Frame data = {frame.data}")

        if frame.dest_addr == self.__number:
            if frame.source_addr == self.__number:
                self.logger(f"Frame to token", 2)
                self.logger(f"The package has been deleted1", 2)
                token = frame.to_token()
                self.send_data(token)
            else:
                self.logger(f"Accept package", 2)
                self.logger(f"Send package to next station", 2)
                self.input_port.WritePacketToPort(frame)
            self.update_info(frame.data)
        elif frame.source_addr == self.__number:
            self.logger(f"Frame to token", 2)
            self.logger(f"The package has been deleted2", 2)
            token = frame.to_token()
            self.send_data(token)
        else:
            self.logger(f"Send package to next station", 2)
            self.input_port.WritePacketToPort(frame)

    def parse_token(self, token):
        if token.sour_addr == self.__number:
            if self.init_token:
                self.send_data(token)
            else:
                self.logger("The token has been deleted", 2)
        else:
            self.send_data(token)

    def send_data(self, token):

        if self.buffer.count() == 0:
            self.logger("Buffer is empty", 1)
            self.logger("Send token to next station", 2)
            self.input_port.WritePacketToPort(token)
        elif token.curr_prior > self.__priority:
            self.logger("The priority of this station is small", 1)
            self.logger("Send token to next station", 2)
            self.input_port.WritePacketToPort(token)
        if self.buffer.count() > 0 and self.__priority >= token.curr_prior:
            frame: Frame = Frame()
            frame.from_token(token)
            frame.source_addr = self.__number
            frame.dest_addr = self.__address
            frame.data = self.buffer.pop()
            self.update_package_count()
            self.logger("Token to Frame", 2)
            self.logger(f"Send package with data to Station #{frame.dest_addr}", 2)
            self.input_port.WritePacketToPort(frame)

    def accept_data(self):
        thread = threading.Thread(target=self.thread_accept_packet)
        thread.daemon = True
        thread.start()

    def thread_accept_packet(self):
        while True:
            obj, data_flag = self.output_port.ReadPacketFromPort()
            if data_flag:
                try:
                    if isinstance(obj, Frame):
                        self.parse_frame(obj)
                    elif isinstance(obj, Token):
                        self.parse_token(obj)
                    else:
                        print("Error Token/Frame")
                except Exception:
                    print("Unknown exception!!!")
