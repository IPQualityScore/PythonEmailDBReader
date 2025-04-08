from typing import List
from functools import reduce
from util.emaillookup.reader.types import (
    base as Base,
    domaincommon as DomainCommon,
    domaindisposable as DomainDisposable,
    domainvelocity as DomainVelocity,
    recentabuse as RecentAbuse,
    uservelocity as UserVelocity,
    fraudscore as FraudScore,
    leaked as Leaked,
    interface as Interface,
    firstseen as FirstSeen, 
    domainage as DomainAge
)
class Data:
    def __init__(self):
        self.hash = 0 # Declare the hash
        self.data: List[Interface] = [] # list the interface

    def btoi(self,val: bytes) -> int:
        return int.from_bytes(val, byteorder="big") # Return the int in btoi

    def get_size(self) -> int:
        return 32 + sum(v.get_size() for v in self.data)  # Return the size in int

    def deserialize(self, b: bytes): # Deserialize function
        if len(b) < 32: # If the len is less than 32
            raise ValueError("data must be 32 bytes !") # The data must be 32 bytes!

        self.hash = self.btoi(b[:32]) # declare the hash with the btoi
        offset = 32 # Set the offset
        self.data = []
        while offset < len(b):
            objType = self.identity_type(b[offset:])
            if objType:
                ob = objType()
                ob.deserialize(b[offset:])
                self.data.append(ob)
                offset += ob.get_size()
            else:
                break
            
    def base(self):
        return next((v for v in self.data if isinstance(v, Base)), None) # Return the next value in self data

    def domainCommon(self):
        return next((v for v in self.data if isinstance(v, DomainCommon)), None)# Return the next value in self data
        
    def domainDisposable(self):
        return next((v for v in self.data if isinstance(v, DomainDisposable)), None)# Return the next value in self data

    def domainVelocity(self):
        return next((v for v in self.data if isinstance(v, DomainVelocity)), None)# Return the next value in self data

    def fraudScore(self):
        return next((v for v in self.data if isinstance(v, FraudScore)), None)# Return the next value in self data

    def leaked(self):
        return next((v for v in self.data if isinstance(v, Leaked)), None)# Return the next value in self data

    def recentAbuse(self):
        return next((v for v in self.data if isinstance(v, RecentAbuse)), None)# Return the next value in self data

    def userVelocity(self):
        return next((v for v in self.data if isinstance(v, UserVelocity)), None)# Return the next value in self data

    def firstSeen(self):
        return next((v for v in self.data if isinstance(v, FirstSeen)), None)# Return the next value in self data
        
    def domainAge(self):
        return next((v for v in self.data if isinstance(v, DomainAge)), None)# Return the next value in self data
        
        
    

    