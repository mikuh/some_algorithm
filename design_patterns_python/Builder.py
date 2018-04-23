class Room(object):

    def __init__(self, nwindows=2, doors=1, direction='s'):
        self.nwindows = nwindows
        self.doors = doors
        self.direction = direction

    def __str__(self):
        return "Room <facing:%s, windows=#%d>" %(self.direction, self.nwindows)


class Proch(object):

    def __init__(self, ndoors=2, direction='w'):
        self.ndoors = ndoors
        self.direction = direction

    def __str__(self):
        return "Proch <facing:%s, doors=#%d>" % (self.direction, self.ndoors)


class LegoHouse(object):

    def __init__(self, nrooms=0, nwindows=0, nporches=0):
        self.nwindows = nwindows
        self.nporches = nporches
        self.nrooms = nrooms
        self.rooms = []
        self.porches = []

