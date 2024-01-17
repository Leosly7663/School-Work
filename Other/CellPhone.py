

class CellPhone:

    def __init__(self):
        self.__carrier = "unknown"
        self.__type = "unknown"
        self.__speed = 0.0
        self.__memory = 0.0
        self.__num_apps = 0

    @property  # decorator to tag this method as a getter
    def carrier(self):
        return self.__carrier

    @carrier.setter  # decorator to tag this method as a setter
    def carrier(self, carrier):
        self.__carrier = carrier


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    @property
    def num_aps(self):
        return self.__num_aps

    @num_aps.setter
    def num_aps(self, num_aps):
        self.__num_aps = num_aps

