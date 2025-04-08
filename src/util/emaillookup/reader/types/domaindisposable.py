class disposableDomain:
    def __init__(self):
        self.disposableDomain = False # Set as false

    def __str__(self) ->str: 
        emailStatus = "disposable Email" if self.disposableDomain else "not Disposable!"  
        return emailStatus # if email disposable

    def get_id(self) -> int: 
        return 7 # Return the id 7

    def get_size(self) -> int:
        return 1 # return 1

    def deserialize(self, data: bytes):
        if len(data) < 1: # if it doesnt match 1 byte
            raise ValueError("Data must be 1 byte!") # raise error
        self.disposableDomain = data[0] == 0x01 # else 