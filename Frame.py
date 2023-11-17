import struct


# n = 8
class Frame:

    def __init__(self, data_maxsize=15):
        self.__data_maxsize = data_maxsize

        # Initializing fields
        self.__flag = (ord('z') + 8) & 0xFFFFFFFFFFFFFFFF
        self.__dest_addr = 0 & 0xFFFFFFFF
        self.__source_addr = 0 & 0xFFFFFFFF
        self.__data = b""
        self.__length = len(self.__data) & 0xFFFFFFFF
        self.__fcs = b''

    @property
    def data(self):
        return self.__data.decode('utf-8')

    @data.setter
    def data(self, data: str):
        self.__data = data.encode('utf-8')

    @property
    def fcs(self):
        return self.__fcs

    @fcs.setter
    def fcs(self, fcs: bytes):
        self.__fcs = fcs

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    def pack(self):
        format_string = 'QIII{}sc'.format(self.__length)

        return struct.pack(format_string,
                           self.__flag,
                           self.__dest_addr,
                           self.__source_addr,
                           self.__length,
                           self.__data,
                           self.__fcs)

    def unpack(self, data):
        # print(data)
        format_string = 'QIII{}sc'.format(len(data) - 21)

        self.__flag, self.__dest_addr, self.__source_addr, self.__length, self.__data, self.__fcs \
            = struct.unpack(format_string, data)
