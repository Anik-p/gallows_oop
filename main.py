from core.game_flow import GameFlow, GameSession
from core.game_logic import WordProvider, InputValidator
from core.score_manager import TimeTracker, ScoreCalculator
from core.word_provider import Word
from validators.letter_validator import LetterValidator
from validators.difficulty_validator import DifficultyValidator
from validators.restart_validator import RestartValidator
from ui.console_ui import ConsoleUI

def setup_dependencies():
    letter_validator = LetterValidator()
    difficulty_validator = DifficultyValidator()
    restart_validator = RestartValidator()

    input_validator = InputValidator(
        validator_letter=letter_validator,
        validator_difficulty=difficulty_validator,
        validator_restart=restart_validator
    )

    word = Word()
    word_provider = WordProvider(word)
    time_tracker = TimeTracker()
    score_calculator = ScoreCalculator(time_tracker)

    game_session = GameSession(
        word_provider=word_provider,
        input_validator=input_validator,
        score_manager=score_calculator,
    )

    ui = ConsoleUI()
    game_flow = GameFlow(ui, game_session)
    return game_flow

def main():
    try:
        game_flow = setup_dependencies()

        game_flow.start_game()

    except RuntimeError as e:
        print(e)

    except Exception as e:
        print(f"\nКритическая ошибка при запуске: {e}")

    finally:
        print("\nИгра завершена")

if __name__ == '__main__':
    main()