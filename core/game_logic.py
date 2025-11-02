from core.game_state import GameState
from validators.letter_validator import LetterValidator
from validators.difficulty_validator import DifficultyValidator
from validators.restart_validator import RestartValidator
from core.word_provider import Word

class WordProvider:
    def __init__(self, word: Word):
        self.word = word

    def get_random_word(self, level: str) -> str:
        return str(self.word.get_random_word(level))

class InputValidator:
    def __init__(self, validator_letter: LetterValidator,
                 validator_difficulty: DifficultyValidator,
                 validator_restart: RestartValidator):
        self.validator_letter = validator_letter
        self.validator_difficulty = validator_difficulty
        self.validator_restart = validator_restart

    def validate_difficulty(self, input_str: str) -> str:
        return self.validator_difficulty.validate(input_str)

    def validate_letter(self, input_str: str) -> str:
        return self.validator_letter.validate(input_str)

    def validate_restart(self, input_str: str) -> bool:
        return self.validator_restart.validate(input_str)

class GameConditionChecker:
    def __init__(self, state: GameState):
        self._state = state

    def is_game_lost(self) -> bool:
        return self._state.attempts == 0

    def is_game_won(self) -> bool:
        return '█' not in self._state.word_spoiler

class LetterTracker:
    def __init__(self, state: GameState):
        self._state = state

    def is_letter_in_word(self, letter: str) -> bool:
        return letter in self._state.word

    def is_letter_already_used(self, letter: str) -> bool:
        return letter in self._state.used_letters

    def add_used_letter(self, letter: str) -> None:
        self._state.used_letters.add(letter)

    def reveal_letter(self, letter: str) -> None:
        if len(letter) == 1:
            for i, value in enumerate(self._state.word):
                if letter == value:
                    self._state.word_spoiler[i] = value
        else:
            if letter == self._state.word:
                self._state.word_spoiler = list(letter)
            else:
                set_letter = all([row in self._state.word for row in sorted(set(letter))])
                if set_letter:
                    for i, value in enumerate(self._state.word):
                        if value in letter:
                            self._state.word_spoiler[i] = value

class GameEngine:
    def __init__(self, validator: InputValidator,
                 state: GameState,
                 check_word: LetterTracker,
                 check_game: GameConditionChecker):

        self.validator = validator
        self._state = state
        self.check_word = check_word
        self.check_game = check_game

    def _unsuccessful_attempt(self) -> None:
        self._state.attempts -= 1

    def make_guess(self, letter: str) -> None:
        value = self.validator.validate_letter(letter)
        if self.check_word.is_letter_already_used(value):
            if len(value) == 1:
                raise ValueError("Это буква уже была!\n")
            raise ValueError("Это слово уже было!\n")

        if self.check_word.is_letter_in_word(value):
            self.check_word.reveal_letter(value)
            self.check_word.add_used_letter(value)
            self._state.game_victory = self.check_game.is_game_won()
        else:
            self._unsuccessful_attempt()
            self.check_word.add_used_letter(value)
            self._state.game_over = self.check_game.is_game_lost()