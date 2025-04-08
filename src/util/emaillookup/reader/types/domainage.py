import struct
import datetime

class DomainAge: 
    def __init__(self, domainAge=None):
        self.domainAge = domainAge or datetime.datetime.utcnow()
    
    def to_str(self):
        return f"Domainage: {self.domainAge}"
    
    def get_id(self):
        return 9
    
    def get_size(self):
        return 8

    def deserialize(self, date):
        r, = struct.unpack("<q", date)
        self.domainAge = datetime.datetime.fromtimestamp(datetime.datetime.utcnow())