from core.game_logic import GameEngine
from core.game_session import GameSession
from core.score_manager import ScoreCalculator
from ui.console_ui import ConsoleUI, GameRenderer
from core.game_state import GameState
from typing import Union

class GameFlow:
    def __init__(self, ui: ConsoleUI, game_session: GameSession):
        self._ui = ui
        self._game_session = game_session
        try:
            result = self._initialize_game()
            if not result:
                raise RuntimeError("Выход из игры")
            current_engine, current_state, current_score, render = result
            self._current_engine = current_engine
            self._current_state = current_state
            self._current_score = current_score
            self._render = render
        except Exception as e:
            raise RuntimeError(f"\n{e}")

    def start_game(self):
        self._ui.show_welcome()
        while True:
            try:
                if not self._game_process():
                    break

                if not self._handle_game_end():
                    break

                if not self._initialize_game():
                    break

            except (EOFError, KeyboardInterrupt):
                self._ui.show_goodbye()
                break

    def _initialize_game(self) -> Union[bool, tuple[GameEngine, GameState, ScoreCalculator, GameRenderer]]:
        while True:
            try:
                self._ui.show_difficulty_menu()
                difficulty = input("\nВведите уровень сложности: ")
                state = self._game_session.start_new_game(difficulty)
                self._ui.show_start_game()

                if not hasattr(self, '_current_engine') or self._current_engine is None:
                    return state
                else:
                    self._update_game_components(state)
                    return True

            except ValueError as e:
                self._ui.show_error(str(e))

            except (EOFError, KeyboardInterrupt):
                self._ui.show_goodbye()
                return False

    def _update_game_components(self, state: tuple) -> None:
        current_engine, current_state, current_score, render = state
        self._current_engine = current_engine
        self._current_state = current_state
        self._current_score = current_score
        self._render = render

    def _game_process(self) -> bool:
        print(self._render.render_game_state())
        while True:
            try:
                if not self._current_state.game_over and not self._current_state.game_victory:
                    self._current_score.time_tracker.start_move()
                    letter = input("\nВведите букву: ")
                    self._current_score.time_tracker.end_move_timing()
                    self._current_engine.make_guess(letter)
                    if letter in self._current_state.word:
                        self._ui.clear_console()
                        self._ui.show_correct_guess(letter)
                        time_move = self._current_score.time_tracker.time_move
                        score_move = self._current_score.calculate_move_score(True)
                        visualizes = self._render.render_game_state(time_move, score_move)
                        print(visualizes)
                    else:
                        self._ui.clear_console()
                        self._ui.show_incorrect_guess(letter)
                        time_move = self._current_score.time_tracker.time_move
                        score_move = self._current_score.calculate_move_score(False)
                        visualizes = self._render.render_game_state(time_move, score_move)
                        print(visualizes)

                else:
                    self._render.display_game_result()
                    return True

            except ValueError as e:
                self._ui.show_error(str(e))

            except (EOFError, KeyboardInterrupt):
                self._ui.show_goodbye()
                return False

    def _handle_game_end(self) -> bool:
        self._ui.show_restart_prompt()
        while True:
            try:
                answer = input("\nВведите ответ (д/н): ")
                value = self._current_engine.validator.validate_restart(answer)

                if value:
                    self._ui.show_restart_message()
                    self._ui.clear_console()
                    return True
                else:
                    self._ui.show_goodbye()
                    return False

            except ValueError as e:
                self._ui.show_error(str(e))

            except (EOFError, KeyboardInterrupt):
                self._ui.show_goodbye()
                return False