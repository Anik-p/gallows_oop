from typing import Type
from ui.hangman_visualizer import HangmanVisualizer
from core.game_state import GameState
from data.config import MaxAttempts
from datetime import timedelta

class ConsoleUI:

    @staticmethod
    def clear_console():
        print('\n' * 50)

    @staticmethod
    def show_welcome():
        print("\nДобро пожаловать в игру 'Виселица'!\n")

    @staticmethod
    def show_restart_message():
        print("\n\nПерезапуск игры...")

    @staticmethod
    def show_goodbye():
        print("\nСпасибо за игру!")

    @staticmethod
    def show_difficulty_menu():
        print (
                "\nВыберите уровень сложности:\n"
                "(л) ---> Легкий\n"
                "(н) ---> Нормальный\n"
                "(с) ---> Сложный\n"
                "Для выхода из игры введите: (quit', 'exit', 'q', 'выход')\n"
        )

    @staticmethod
    def show_start_game():
        print("\nИгра началась!\n")

    @staticmethod
    def show_restart_prompt():
        print("\nВы хотите продолжить игру?\n"
          "да/нет (д/н)\n")

    @staticmethod
    def show_correct_guess(letter: str):
        if len(letter) == 1:
            print(f"✅ Буква '{letter}' есть в слове!")
        else:
            print(f"✅ '{letter}' есть в слове!")

    @staticmethod
    def show_incorrect_guess(letter: str):
        if len(letter) == 1:
            print(f"❌ Буквы '{letter}' нет в слове")
        else:
            print(f"❌ '{letter}' нет в слове")

    @staticmethod
    def show_error(message: str):
        print(f"⚠️  {message}")


class GameRenderer:
    def __init__(self,visualizer: HangmanVisualizer, state: GameState, level: str):
        self._visualizer = visualizer
        self._state = state
        self._confing = self._create_confing()
        self._level = level

    @classmethod
    def _create_confing(cls) -> Type[MaxAttempts]:
        return MaxAttempts

    def get_hangman_art(self, attempt: int) -> str:
        return self._visualizer.get_visualization(attempt)

    def render_game_state(self, time=0, score=(0, 0)) -> str:
        used_letters = ', '.join(sorted(self._state.used_letters))
        attempt = self._state.attempts
        visualizer = self.get_hangman_art(attempt)
        word_display = ' '.join(self._state.word_spoiler)
        score_move, total_score = score
        difficulty_level = self._confing[self._level].value
        return (f"{visualizer}"
                f"\nЗатрачено времени: {timedelta(seconds=round(time))}"
                f"\nПолучено очков: {score_move}"
                f"\nВсего очков: {total_score}"
                f"\nСлово: {word_display}"
                f"\nИспользованные буквы/слова: {used_letters}"
                f"\nКоличество попыток: {difficulty_level} / {self._state.attempts}")

    def display_game_result(self):
        if self._state.game_victory:
            print("\n🎉 Поздравляем! Вы выиграли!")
        else:
            print("\n💀 К сожалению, вы проиграли!\n")
            print(f"Загаданное слово: {''.join(self._state.word)}\n")