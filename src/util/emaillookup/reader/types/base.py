class Base:
    def __init__(self):
        # Declares all the stuff
        self.valid = False #
        self.disposable = False
        self.suspect = False
        self.catchAll = False
        self.smtpScore = 0
        self.deliverability = 0

    def get_id(self) -> int:
        return 0 # Return 0 for the id

    def get_size(self) -> int:
        return 3 # 1 for valid, disposable, suspect and catchall. 1 byte for score, 1 byte for deliverability
        
    def deserialize(self, data: bytes):
        if len(data)< 3: # if the data in the lens is less than 3 or not 3 
            raise ValueError("Data must be 3 bytes!")  # Raise error
        self.valid = (data[0] & (1 << 0)) >> 0 == 1  
        self.disposable = (data[0] & (1 << 1)) >> 1 == 1
        self.suspect = (data[0] & (1 << 3)) >> 3 == 1 
        self.smtpScore = data[1] 
        self.deliverability = data[2]
    def __str__(self) -> str:
        return f"Valid: {self.valid}, Disposable: {self.disposable}, Suspect: {self.suspect}, SmtpScore = {self.smtpScore}, Deliverability = {self.deliverability}" # Return the level per each option