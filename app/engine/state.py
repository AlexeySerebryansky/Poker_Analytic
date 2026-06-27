from dataclasses import dataclass, field


@dataclass(frozen=True)
class GameState:
    hand: tuple[str, ...] = field(default_factory=tuple)
    board: tuple[str, ...] = field(default_factory=tuple)


    @property
    def all_cards(self):
        return self.hand + self.board
