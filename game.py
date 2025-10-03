import core
import word_provider
import ScoreManager as Score
from validators.DifficultyValidator import DifficultyValidator
from validators.RestartValidator import RestartValidator

class Game:
    """
    Класс, управляющий игровым процессом
    Он отвечает за:
    1) Инициализацию игровой логики;
    2) Валидацию водимой буквы в начале и перезапуске игры;
    3) Обработкой и отображением исключений;
    4) Управлением игровым циклом и перезапуском;
    5) Вывод на экран графического интерфейса;
    """

    def __init__(self):

        self._difficulty_validator = DifficultyValidator()

        self._restart_validator = RestartValidator()

        self._word_provider = word_provider.GetWord()

        self._core = None

        self._word = None

        self._score = None


    @staticmethod
    def _print_start_game():
        print (
                f"\nВыберите уровень сложности:\n"
                f"(л) ---> Легкий\n"
                f"(н) ---> Нормальный\n"
                f"(с) ---> Сложный\n"
                f"Для выхода из игры введите: (quit', 'exit', 'q', 'выход')\n"
        )





    def _value_input_validate(self, title: str) -> str:
        """Проверяет на корректность ввода"""
        return self._difficulty_validator.validate(title)

    def _return_start_game(self, level: str) -> str:
        """Выводит случайное слово из набора"""
        return self._word_provider.get_word(level)

    def _instance_core(self, title: str):
        """Инициализирует игровую логику"""
        self._core = core.Core(title)

    def _instance_score(self, level):
        """Инициализатор подсчет очков"""
        self._score = Score.ScoreManager(level)

    def start_game(self):

        self._print_start_game()
        while True:
            try:
                user_input = input("\nВведите уровень сложности: ")
                value_validate = self._value_input_validate(user_input)
                self._instance_score(value_validate)
                title = self._return_start_game(value_validate)
                self._word = title
                self._instance_core(title)


                return True
            except FileNotFoundError as f:
                print(f"\n⚠️ {f}")
                return None
            except TypeError as t:
                print(f"\n⚠️ {t}")
                return None
            except ValueError as e:
                print(f"\n⚠️ {e}")
            except EOFError:
                print("\n\nЗавершение работы...")
                return None
            except KeyboardInterrupt:
                print("\n\nПрервано пользователем")
                return None

    def game_proses(self):
        print(f"\nИгра началась!\n")
        print(self._core.visualizer())
        while True:
            try:

                self._score.start_move()
                user_input = input("\nВведите букву: ")
                visualizer = self._core.make_guess(user_input)
                self._score.end_move()
                print(visualizer)

                attempts = self._core.output_of_attempts()
                point = round(self._score.scoring(attempts))
                final_points = round(self._score.final_points)
                print(f"Получено очков за ход: {point}")
                print(f"Итого: {final_points} очков")

                if self._core.game_over is True:


                    print(f"\n💀 Игра окончена! Вы проиграли!")
                    print(f"💡 Загаданное слово: {''.join(self._word)}")

                    return True

                elif self._core.game_victory is True:


                    print(f"\n🎉 Поздравляем! Вы выиграли!")

                    return True

            except ValueError as e:
                print(f"\n⚠️ {e}")
            except EOFError:
                print("\n\nЗавершение работы...")
                return None
            except KeyboardInterrupt:
                print("\n\nПрервано пользователем")
                return None


    def reset(self):
        print(f"\nВы хотите продолжить игру?\n"
              f"да/нет (д/н)\n")
        while True:
            try:
                user_input = input("\nВведите ответ: ")
                return self._restart_validator.validate(user_input)
            except ValueError as e:
                print(f"\n⚠️ {e}")
            except EOFError:
                print("\n\nЗавершение работы...")
                return None
            except KeyboardInterrupt:
                print("\n\nПрервано пользователем")
                return None


