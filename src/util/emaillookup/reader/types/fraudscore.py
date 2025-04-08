class FraudScore:
    def __init__(self):
        self.fraudScore = 0 # Default value

    def __str__(self) -> str:
        return f"fraudScore: {self.fraudScore}" # return it

    def get_id(self) -> int:
        return 1 # return the id

    def get_size(self) -> int:
        return 1 # return the size
        
    def deserialize(self, data: bytes):
        if len(data) < 1:  # if the fraudscore is less than 1 byte
            raise ValueError("data must be 1 byte!") # Raise error
        self.fraudScore = data[0] # else set fraudscore