class RecentAbuse:
    def __init__(self):
        self.recentAbuse = False # Default value

    def __str__(self) -> str:
        return "recent abuse" if self.recentAbuse else "no recent abuse"

    def get_id(self) -> int:
        return 3 # return the id of 3 

    def get_size(self) -> int:
        return 1 # get the size
        
    def deserialize(self, data: bytes):
        if len(data) <1:  # if the lens is less than 1 byte
            raise ValueError("data must be 1 byte!") # raise error
        self.recentAbuse = data[0] == 0x01