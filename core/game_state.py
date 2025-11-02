from dataclasses import dataclass, field

@dataclass
class GameState:
    word : str
    word_spoiler : list = field(init=False)
    attempts : int = field(default=6)
    game_over : bool = field(default=False, init=False)
    game_victory : bool = field(default=False, init=False)
    used_letters : set = field(default_factory=set, init=False)

    def __post_init__(self):
        self.word_spoiler = list('█' * len(self.word))

    @classmethod
    def create_new_game(cls, word: str, max_attempts: int = 6) -> "GameState":
        return cls(
            word=word,
            attempts=max_attempts
        )