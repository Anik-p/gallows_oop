from dataclasses import dataclass, field

@dataclass
class CreateGameState:
    """Создает начальное состояние игры"""
    word : str
    word_spoiler : list = field(init=False)
    attempts : int = field(default=6, init=False)
    game_over : bool = field(default=False, init=False)
    game_victory : bool = field(default=False, init=False)
    used_letters : set = field(default_factory= set, init=False)

    def __post_init__(self):
        self.word_spoiler = list('█' * len(self.word))

