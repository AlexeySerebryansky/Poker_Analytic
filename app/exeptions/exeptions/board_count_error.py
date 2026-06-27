class BoardCountError(Exception):

    def __init__(self, count: int):
        self.count = count

        super().__init__(
            f"Detected invalid count cards on the board: {count}"
        )