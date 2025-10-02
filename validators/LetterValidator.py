from validators.interfaces import InputValidator

class LetterValidator(InputValidator):
    def validate(self, input_str: str) -> str:

        if input_str in ('quit', 'exit', 'q', 'выход'):
            raise EOFError("Выход из игры")

        if not isinstance(input_str, str) or len(input_str) != 1:
            raise ValueError('Введите одну букву!')

        if input_str.lower() not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
            raise ValueError('Буквы должны быть из русского алфавита!')

        return input_str.lower()