import struct
from typing import List, BinaryIO
from functools import reduce
from util.emaillookup.reader.types.interface import Interface
from util.emaillookup.reader.types.domaindisposable import disposableDomain
from util.emaillookup.reader.types.domainvelocity import DomainVelocity
from util.emaillookup.reader.types.domaincommon import DomainCommon
from util.emaillookup.reader.types.fraudscore import FraudScore
from util.emaillookup.reader.types.leaked import Leaked 
from util.emaillookup.reader.types.unknown import Unknown
from util.emaillookup.reader.types.uservelocity import UserVelocity
from util.emaillookup.reader.types.base import Base
from util.emaillookup.reader.types.recentabuse import RecentAbuse

class Header:
    def __init__(self):
        self.header = b"IPQS" # Declare the header
        self.version = 0 # Declare the version
        self.type = 0 # Declare the type
        self.creationTime = 0 # declare the creation time
        self.headers: List[Interface] = [] # list the interface

    def get_size(self) -> int: # Get the size
        return 4 + 1 + 1 + 8 + 1 + len(self.headers) * 2 # math for the size

    def deserialize(self, file: BinaryIO): # Deeserialize it
        file.seek(0) # Seek the file
        buffer = file.read(4) # Read it with 4 bytes
        if buffer != b"IPQS": # if the buffer doesnt = the given
            raise ValueError(f"invalid header in: {file.name}!") # Raise invalid header
        self.header = buffer # Declare the header
        self.version = struct.unpack("B", file.read(1))[0] # Unpack the struct and read it
        if self.version != 0x01: # If the version does not = 0x01
            raise ValueError(f"invalid version in: {file.name}!") # raise exception and tell the version it got
        self.type = struct.unpack("B", file.read(1)) # Unpack the struct
        self.creationTime = struct.unpack("<Q", file.read(8))[0] # declare the creation time by unpacking the struct
        count = struct.unpack("B", file.read(1))[0] # more unpacking 
        self.header = [] # Delcare the header
        possibleHeaders = [
            Base(), FraudScore(), Leaked(), RecentAbuse(), UserVelocity(), DomainVelocity(), DomainCommon(), disposableDomain()
        ] # All the possible headers
        offset = 15 # Set the offset
        for _ in range(count): # For in range
            file.seek(offset) # Seek the offset
            idByte, sizeByte = struct.unpack("BB", file.read(2)) # Set the id and size byte
            found = False # Set found as false
            for possibleHeader in possibleHeaders: # For headers in header
                if possibleHeader.get_id() == idByte: # If the header id == the wanted id
                    self.headers.append(possibleHeader) # append it
                    found = True # The header has been found
                    break # Break
            if not found: # if not
                self.headers.append(Unknown(sizeByte)) # append with a unknown size
            offset += 2
