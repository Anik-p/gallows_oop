import hangman_visualizer
import State
from validators.LetterValidator import LetterValidator


class Core:
    """
    Класс, управляющий основной логикой (механикой) игры 'Виселица'
    Он отвечает за:
    1) Инициализацию игрового состояния и загрузку слова;
    2) Валидацию водимой буквы;
    3) Отслеживание прогресса игры;
    4) Возращение состояния игры графическим интерфейсом (кек);
    5) Определение условия победы или поражения;
    6) Управление игровой механикой (ходы, штрафы).
    """
    def __init__(self, word):

        self._state = State.CreateGameState(word=word)

        self._validator_proses = LetterValidator()

        self._visualizer = hangman_visualizer.HangmanVisualizer()


    @staticmethod
    def _clear_previous_lines():
        print('\n' * 50)

    @property
    def game_over(self):
        return self._state.game_over

    @property
    def game_victory(self):
        return self._state.game_victory

    def value_input(self, letter: str) -> str:
        """Проверяет ввод и возвращает нормализованную букву"""
        return self._validator_proses.validate(letter)

    def state_game_attempts(self) -> bool:
        """Проверяет, проиграна ли игра"""
        return self._state.attempts == 0

    def check_for_guessed_words(self) -> bool:
        """Проверяет, выиграна ли игра"""
        return '█' not in self._state.word_spoiler

    def checking_the_progress(self, letter: str) -> bool:
        """Проверяет, есть ли буква в загаданном слове"""
        return letter in self._state.word

    def letter_check_to_game(self, letter: str) -> bool:
        """Проверяет, была ли буква уже использована"""
        return letter in self._state.used_letters

    def successful_attempt(self, letter: str):
        """Открывает букву в слове"""
        for i, value in enumerate(self._state.word):
            if letter == value:
                self._state.word_spoiler[i] = value

    def mark_letter_used(self, letter: str):
        """Добавляет букву в набор"""
        self._state.used_letters.add(letter)

    def unsuccessful_attempt(self):
        """Уменьшает количество попыток"""
        self._state.attempts -= 1

    def  word_output(self) -> str:
        """Возвращает слово для отображения"""
        return ' '.join(self._state.word_spoiler)

    def output_of_attempts(self) -> int:
        """Возвращает количество попыток"""
        return self._state.attempts

    def hangman_visualizer(self, attempts: int) -> str:
        """Возвращает изображение игровой 2D модельки (кек)"""
        return self._visualizer.visualizer[attempts]

    def output_of_used_words(self) -> str:
        """Возвращает использованные слова"""
        return ', '.join(sorted(self._state.used_letters))

    def visualizer(self) -> str:
        """Возвращает изображение состояния хода"""
        attempts = self.output_of_attempts()
        visualizer = self.hangman_visualizer(attempts)
        word = self.output_of_used_words()
        return (f"{visualizer}"
               f"\nСлово: {self.word_output()}"
               f"\nИспользованные буквы: {word}"
               f"\nКоличество попыток: 6 / {attempts}")


    def make_guess(self, letter: str) -> str:
        """
                Возвращает состояние игры.

                Выполняет:

                - Валидацию вводимой буквы
                - Проверку буквы в загаданном слове
                - Проверку ранее написанной буквы игроком
                - Возращение сообщения выполненной проверки
                - Возращение графического изображения

        """
        value = self.value_input(letter)

        if self.letter_check_to_game(value):
            raise ValueError(f"Это буква уже была!\n")

        if self.checking_the_progress(value):
            self.successful_attempt(value)
            self.mark_letter_used(value)
            self._state.game_victory = self.check_for_guessed_words()
            self._clear_previous_lines()
            return (f"✅ Правильно!\n"
                    f"{self.visualizer()}")

        else:
            self.unsuccessful_attempt()
            self.mark_letter_used(value)
            self._state.game_over = self.state_game_attempts()
            self._clear_previous_lines()
            return (f"❌ Такой буквы нет!\n"
                    f"{self.visualizer()}")







