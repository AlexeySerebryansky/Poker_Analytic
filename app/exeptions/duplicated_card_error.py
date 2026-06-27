from exeptions.exeptions import GameStateError


class DuplicatedCardError(GameStateError):
    def __init__(self, cards: list[str]):

        self.cards = cards

        super().__init__(f"Duplicate cards detected: {cards}")
