from core.game_logic import GameEngine, WordProvider, InputValidator, LetterTracker, GameConditionChecker
from data.config import MaxAttempts
from core.score_manager import ScoreCalculator, TimeTracker
from ui.console_ui import GameRenderer
from ui.hangman_visualizer import HangmanVisualizer
from core.game_state import GameState

class GameSession:
    def __init__(self,
                 word_provider: WordProvider,
                 input_validator: InputValidator,
                 score_manager: ScoreCalculator,
                 ):

        self._word_provider = word_provider
        self._input_validator = input_validator
        self._score_manager = score_manager
        self._attempts = self._create_config()

    @classmethod
    def _create_config(cls):
        return MaxAttempts

    def start_new_game(self, difficulty: str) -> tuple[GameEngine, GameState, ScoreCalculator, GameRenderer]:
        validated_difficulty = self._input_validator.validate_difficulty(difficulty)
        word = self._word_provider.get_random_word(validated_difficulty)
        attempt = self._attempts[validated_difficulty].value
        score_manager = self._create_game_score_calculator(validated_difficulty)
        visualizer = self._create_game_visualizer(validated_difficulty)
        state = self._create_game_state(word, attempt)
        render = self._create_game_render(visualizer, state, validated_difficulty)
        engine = self._create_game_engine(state)

        return engine, state, score_manager, render

    @staticmethod
    def _create_game_score_calculator(difficulty: str) -> ScoreCalculator:
        time_tracker = TimeTracker()
        score = ScoreCalculator(time_tracker)
        score.configure_difficulty_settings(difficulty)
        return score

    @staticmethod
    def _create_game_visualizer(difficulty: str) -> HangmanVisualizer:
        return HangmanVisualizer(difficulty)

    @staticmethod
    def _create_game_state(word: str, attempt: int) -> GameState:
        return GameState.create_new_game(word, attempt)

    @staticmethod
    def _create_game_render(visualizer: HangmanVisualizer, state: GameState, difficulty: str) -> GameRenderer:
        return GameRenderer(visualizer, state, difficulty)

    def _create_game_engine(self, state: GameState) -> GameEngine:
        letter_tracker = LetterTracker(state)
        condition_checker = GameConditionChecker(state)

        return GameEngine(
            validator=self._input_validator,
            state=state,
            check_word=letter_tracker,
            check_game=condition_checker
        )
