from validators.interfaces import InputValidator

class DifficultyValidator(InputValidator):

    def validate(self, input_str: str) -> str:
        if input_str in ('quit', 'exit', 'q', 'выход'):
            raise EOFError("Выход из игры")

        if input_str.lower() not in ('л', 'н', 'с', 'легкий', 'нормальный', 'сложный'):
            raise ValueError('Некорректный уровень сложности!')

        return input_str[0].lower()