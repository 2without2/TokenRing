import struct


class Token:

    def __init__(self, req_prior=1):
        self.__start_delim = 0
        self.__curr_prior = 0
        self.__sour_addr = 0
        self.__req_prior = req_prior
        self.__end_delim = 0

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
    def req_prior(self):
        return self.__req_prior

    @req_prior.setter
    def req_prior(self, value):
        self.__req_prior = value

    def pack(self):
        format_string = 'BBBBB'.format()
        return struct.pack(format_string,
                           self.__start_delim,
                           self.__curr_prior,
                           self.__sour_addr,
                           self.__req_prior,
                           self.__end_delim)

    def unpack(self, data):
        format_string = 'BBBBB'.format()
        self.__start_delim, self.__curr_prior, self.__sour_addr, self.__req_prior, self.__end_delim \
            = struct.unpack(format_string, data)

