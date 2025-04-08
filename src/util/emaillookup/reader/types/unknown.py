class Unknown:
    def __init__(self):
        self.size = 0
        
        def __str__(self) -> str:
            return ""

        def get_id(self) -> int:
            return 255

        def get_size(self) -> int:
            return self.size
            
        def deserialize(self, data: bytes):
            pass