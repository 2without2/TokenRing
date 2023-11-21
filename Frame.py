import struct


# n = 8
class Frame:

    def __init__(self, data_maxsize=15):
        self.__data_maxsize = data_maxsize

        # Initializing fields
        self.__start_delim = 0
        self.__access_control = 0
        self.__frame_control = 0
        self.__dest_addr = 0 & 0xFFFFFFFF
        self.__source_addr = 0 & 0xFFFFFFFF
        self.__data = b""
        self.__length = len(self.data)
        self.__fcs = 0
        self.__end_delim = 0
        self.__frame_status = 0
        self.__inter_frame_gap = 0

    @property
    def data(self):
        return self.__data.decode('utf-8')

    @data.setter
    def data(self, data: str):
        self.__data = data.encode('utf-8')
        self.__length = len(self.__data)

    @property
    def dest_addr(self):
        return self.__dest_addr

    @dest_addr.setter
    def dest_addr(self, dest_addr: int):
        self.__dest_addr = dest_addr

    @property
    def source_addr(self):
        return self.__source_addr

    @source_addr.setter
    def source_addr(self, source_addr: int):
        self.__source_addr = source_addr

    def updateFS_bitA(self):
        self.__frame_status = self.__frame_status | (1 << 0)
        self.__frame_status = self.__frame_status | (1 << 4)

    def updateFS_bitC(self):
        self.__frame_status = self.__frame_status | (1 << 1)
        self.__frame_status = self.__frame_status | (1 << 5)

    def update_frame_status(self):
        self.updateFS_bitA()
        self.updateFS_bitC()

    def pack(self):
        format_string = 'BBBII{}sBBBBB'.format(self.__length)

        return struct.pack(format_string,
                           self.__start_delim,
                           self.__access_control,
                           self.__frame_control,
                           self.dest_addr,
                           self.source_addr,
                           self.__data,
                           self.__length,
                           self.__fcs,
                           self.__end_delim,
                           self.__frame_status,
                           self.__inter_frame_gap)

    def unpack(self, data):
        format_string = 'BBBII{}sBBBBB'.format(len(data) - 17)
        self.__start_delim, self.__access_control, self.__frame_control, self.__dest_addr, self.__source_addr, self.__data, self.__length, self.__fcs, self.__end_delim, self.__frame_status, self.__inter_frame_gap = struct.unpack(format_string, data)
