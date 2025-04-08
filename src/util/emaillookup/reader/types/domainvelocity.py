class DomainVelocity:
    def __init__(self):
        self.domainVelocity = 0 # set domain velocity

    def __str__(self) -> str:
        domainVelocityStatus = f'domainVelocity: {self.domainVelocity:02x}'
        return domainVelocityStatus # return the domain velocity
        
    def get_id(self) -> int:
        return 5 # Return 5
        
    def get_size(self) -> int():
        return 1 # return 1
        
    def deserialize(self, data: bytes):
        if len(data) < 1 : # if the data isnt 1 byte
            raise ValueError("Data must be 1 byte!") # raise error
        self.domainVelocity = data[0] 