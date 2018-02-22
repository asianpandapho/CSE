class Room(object):
    def __init__ (self, name, description, north, south, west, east, northeast, northwest, southeast, southwest):
        self.name = name
        self.description = description
        self.n = north
        self.s = south
        self.w = west
        self.e = east
        self.ne = northeast
        self.nw = northwest
        self.se = southeast
        self.sw = southwest

