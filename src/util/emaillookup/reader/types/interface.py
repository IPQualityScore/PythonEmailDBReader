class Interface:
    def get_id(self) -> int:
        pass

    def get_size(self) -> int:
        pass

    def deserialize(self, data: bytes):
        pass

    def __str__(self) -> str:
        pass
    