class Leaked:
    def __init__(self):
        self.leaked = False # Default value

    def __str__(self) -> str:
        return "leaked" if self.leaked else "not leaked!"

    def get_id(self) -> int:
        return 2 # return the id

    def get_size(self) -> int:
        return 1 # return the size
        
    def deserialize(self, data: bytes):
        if len(data) <1: # if the byte is less than 1 
            raise ValueError("Data must be 1 byte!") # raise error
        self.leaked = data[0] == 0x01