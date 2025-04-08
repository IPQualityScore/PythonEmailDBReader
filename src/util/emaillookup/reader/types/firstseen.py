import struct
import datetime

class FirstSeen:
    def __init__(self, firstSeen=None):
        self.firstSeen = firstSeen or datetime.datetime.utcnow()
    
    def toStr(self):
        return f"Firstseen: {self.firstSeen}"
    
    def get_id(self):
        return 8

    def get_size(self):
        return 8
    
    def deserialize(self, date):
        r, = struct.unpack("<q", date)
        self.firstSeen = datetime.datetime.utcfromtimestamp(r)
