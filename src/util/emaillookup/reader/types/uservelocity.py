class UserVelocity:
    def __init__(self):
        self.userVelocity = 0 # Declare default value

    def __str__(self) -> str:
        return f"userVelocity = {self.userVelocity:02x}" # return the user velocity

    def get_id(self) -> int:
        return 4 # return the id

    def get_size(self) -> int:
        return 1 # return the size
        
    def deserialize(self, data: bytes):
        if len(data) <1:  # if the data is less than a byte 
            raise ValueError("data must be 1 byte!") # raise error 
        self.userVelocity = data[0] # else set velocity