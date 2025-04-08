import struct 
from typing import Optional, BinaryIO
from util.emaillookup.reader.header import Header
from util.emaillookup.reader.data import Data

class Reader:
    def __init__(self, file: BinaryIO):
        self.file = file # Declare the file
        self.header = Header() # Declare the header
        self.header.deserialize(file) # Deserialize it

    def btoi64(self,val: bytes) -> int:
        return int.from_bytes(val, byteorder="little", signed=True) # Return the int in a specific format

    def contains_offset(self, hash_value: int, offset: int) -> Optional[Data]:
        self.file.seek(offset) # Seek the file
        leaf = struct.unpack("B", self.file.read(1))[0] == 0x01 #unpack the struct and read the file 
        offset += 1 # Declare offset
        bN = self.file.read(8) # Read it with 8 bytes
        offset += 8 # Declare offset
        N = self.btoi64(bN) # declare btoi
        for i in range(N): # for loop for data range
            key = Data() # Declare the key
            key.data = [type(v)() for v in self.header.headers] # Declare the key data by grabbing headers
            b1 = self.file.read(key.get_size()) # Read the file and get the key size
            key.deserialize(b1) # Deseralize it
            offset += key.get_size() # Get the size of the offset
            if hash_value == key.hash: # if it matches the hash
                return key # return the key
            if hash_value < key.hash: # else
                if leaf: # return none
                    return None
                offset += 8 * (i - 1) # do offset math
                self.file.seek(offset) # seek the offset
                pos = self.file.read(8) # read the file
                offset = self.btoi64(pos) # get the btoi
                if offset == 0: # if the offset is 0 
                    return None # return nothing
                return self.contains_offset(hash_value, offset) # return the offset
            return None # else return none
            
    def close_file(self): # close the file clean
        try:
            self.file.close()
        except Exception as e:
            print(e)                