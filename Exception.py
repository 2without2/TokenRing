
class StationNumberException(Exception):
    def __init__(self, number):
        self.number = number

    def error(self):
        return f"The station with the number = {self.number} already exists"


class StationPortsException(Exception):
    def __init__(self, ports: str):
        self.ports = ports

    def error(self):
        return f"The station with the port = {self.ports} already exists"


class MaxStationNumberException(Exception):
    def __init__(self, max_number):
        self.number = max_number
        pass

    def error(self):
        return f"The maximum number of stations = {self.number} has been reached"


class AlreadyStationNumberException(Exception):
    def __init__(self, station_number):
        self.station_number = station_number

    def what(self):
        return f"Station {self.station_number}: The station number is already {self.station_number}"
