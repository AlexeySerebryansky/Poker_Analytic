from exeptions.game_state_error import GameStateError


class HandCountError(GameStateError):

    def __init__(self, count:int):
        self.count = count

        super().__init__(
            f"Expected 2 cards in hand, detected {count}"
        )

