import struct
from Token import Token


class Frame:

    def __init__(self):
        # Initializing fields
        self.__dest_addr = 0
        self.__source_addr = 0
        self.__data = b""
        self.__length = len(self.__data)
        # TOKEN
        self.__token_source_addr = 0
        self.__token_priority = 0
        self.__token_reserv_priority = 0
        self.__id = 1

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

    def to_token(self):
        token: Token = Token()
        token.sour_addr = self.__token_source_addr
        token.res_prior = self.__token_reserv_priority
        token.curr_prior = self.__token_priority
        token.id = 0
        return token

    def from_token(self, token):
        self.__token_source_addr = token.sour_addr
        self.__token_priority = token.curr_prior
        self.__token_reserv_priority = token.res_prior
        self.__id = 1

    def pack(self):
        format_string = 'ii{}sbbbbb'.format(self.__length)

        return struct.pack(format_string,
                           self.dest_addr,
                           self.source_addr,
                           self.__data,
                           self.__length,
                           self.__token_source_addr,
                           self.__token_priority,
                           self.__token_reserv_priority,
                           self.__id)

    def unpack(self, data):
        format_string = 'ii{}sbbbbb'.format(len(data) - 13)
        self.__dest_addr, self.__source_addr, self.__data, self.__length, self.__token_source_addr, self.__token_priority, self.__token_reserv_priority, self.__id = struct.unpack(format_string, data)
