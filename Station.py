from COMPort import COMPort
from Frame import Frame
from Communicator import DebugCommunicator
import threading


class Station:
    def __init__(self, number: int, input_port: str, output_port: str, communicator: DebugCommunicator,
                 function, priority: int = 1):
        # var
        self.input_port: COMPort = COMPort(input_port)
        self.output_port: COMPort = COMPort(output_port)
        self.__number = number
        self.__address = number
        self.debug_communicator = communicator
        self.__priority = priority
        self.callback_function = function
        self.initStation()

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def address(self):
        return self.__number

    @address.setter
    def address(self, address: int):
        self.__address = address

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    def logger(self, data, mode):
        self.debug_communicator.data_signal.emit(f"Station #{self.__number}: {data}", mode)

    def update_info(self, text: str):
        self.callback_function(text)

    def initStation(self):
        self.input_port.SetParamCOMPort()
        self.output_port.SetParamCOMPort()
        self.accept_data()

    def closeStation(self):
        self.input_port.CloseCOMPort()
        self.output_port.CloseCOMPort()

    # input_port
    def send_data(self, data: str):
        frame = Frame()
        frame.data = data
        frame.source_addr = self.__number
        frame.dest_addr = self.__address
        self.input_port.WritePacketToPort(frame)
        self.logger(f"The package was sent to Station #{self.__address}", 2)

    # output_port
    def accept_data(self):
        thread = threading.Thread(target=self.thread_accept_packet)
        thread.daemon = True
        thread.start()

    def thread_accept_packet(self):
        while True:
            frame, data_flag = self.output_port.ReadPacketFromPort()
            if data_flag:
                if frame.dest_addr == self.__number:
                    if frame.source_addr == self.__number: # тут мы достигли станции отправителя source_addr
                        self.logger(f"The package has been deleted", 2)
                    else: # тут мы обрабатываем dest_addr
                        self.logger(f"Send package to next station", 2)
                        self.input_port.WritePacketToPort(frame)
                    self.update_info(frame.data)
                elif frame.source_addr == self.__number:
                    self.logger(f"The package has been deleted", 2)
                else:
                    self.logger(f"Send package to next station", 2)
                    self.input_port.WritePacketToPort(frame)


