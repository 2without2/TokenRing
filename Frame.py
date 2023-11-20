import struct


# n = 8
class Frame:

    def __init__(self, data_maxsize=15):
        self.__data_maxsize = data_maxsize

        # Initializing fields
        self.start_delim = 0
        self.access_control = 0
        self.frame_control = 0
        self.__dest_addr = 0 & 0xFFFFFFFF
        self.__source_addr = 0 & 0xFFFFFFFF
        self.__data = b""
        self.length = len(self.data)
        self.fcs = 0
        self.end_delim = 0
        self.frame_status = 0
        self.inter_frame_gap = 0

    @property
    def data(self):
        return self.__data.decode('utf-8')

    @data.setter
    def data(self, data: str):
        self.__data = data.encode('utf-8')
        self.length = len(self.__data)

    @property
    def dest_addr(self):
        return self.__dest_addr

    @dest_addr.setter
    def dest_addr(self, dest_addr: int):
        self.__dest_addr = dest_addr # & 0xFFFFFFFF

    @property
    def source_addr(self):
        return self.__source_addr

    @source_addr.setter
    def source_addr(self, source_addr: int):
        self.__source_addr = source_addr # & 0xFFFFFFFF

    def updateFS_bitA(self):
        self.frame_status = self.frame_status | (1 << 0)
        self.frame_status = self.frame_status | (1 << 4)

    def updateFS_bitC(self):
        self.frame_status = self.frame_status | (1 << 1)
        self.frame_status = self.frame_status | (1 << 5)


    def pack(self):
        format_string = 'BBBII{}sBBBBB'.format(self.length)

        return struct.pack(format_string,
                           self.start_delim,
                           self.access_control,
                           self.frame_control,
                           self.dest_addr,
                           self.source_addr,
                           self.__data,
                           self.length,
                           self.fcs,
                           self.end_delim,
                           self.frame_status,
                           self.inter_frame_gap)

    def unpack(self, data):
        format_string = 'BBBII{}sBBBBB'.format(len(data) - 17)
        self.start_delim, self.access_control, self.frame_control, self.dest_addr, self.source_addr, self.__data, self.length, self.fcs, self.end_delim, self.frame_status, self.inter_frame_gap = struct.unpack(format_string, data)

