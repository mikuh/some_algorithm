class Engine(object):
    """An Engine class
    """

    def __init__(self, name, bhp, rpm, volume, cylibders=4, type='petrol'):
        self.name = name
        self.bhp = bhp
        self.rpm = rpm
        self.volume = volume
        self.cylibders = cylibders
        self.type = type

    def start(self):
        print("Engine start")


    def stop(self):
        print("Engine stopped")


class Transmission(object):
    """

    """

