class DomainCommon:
    def __init__(self):
        self.DomainCommon = False # Declare domain as false

    def __str__(self) -> str:
        return "Common domain" if self.DomainCommon else "Domain not common!" # If the domain is common
        
    def get_id(self)-> int:
        return 6 # Return the id

    def get_size(self) -> int:
        return 1 # Return the size
        
    def deserialize(self, data: bytes):
        if len(data)< 1: # if the lens is less than 1
            raise ValueError("Data must be 1 byte!") # raise error
        self.DomainCommon = data[0] == 0x01 