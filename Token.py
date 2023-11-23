import struct


class Token:

    def __init__(self, res_prior=1):
        self.__curr_prior = 0
        self.__sour_addr = 0
        self.__res_prior = res_prior
        self.__id = 0

    @property
    def curr_prior(self):
        return self.__curr_prior

    @curr_prior.setter
    def curr_prior(self, value):
        self.__curr_prior = value

    @property
    def sour_addr(self):
        return self.__sour_addr

    @sour_addr.setter
    def sour_addr(self, value):
        self.__sour_addr = value

    @property
    def res_prior(self):
        return self.__res_prior

    @res_prior.setter
    def res_prior(self, value):
        self.__res_prior = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def pack(self):
        format_string = 'BBBB'.format()
        return struct.pack(format_string,
                           self.__curr_prior,
                           self.__sour_addr,
                           self.__res_prior,
                           self.__id)

    def unpack(self, data):
        format_string = 'BBBB'.format()
        self.__curr_prior, self.__sour_addr, self.__res_prior, self.__id = struct.unpack(format_string, data)

