from validators.interfaces import InputValidator

class LetterValidator(InputValidator):
    def validate(self, input_str: str) -> str:
        normalized_input = input_str.lower().strip()

        if normalized_input in ('quit', 'exit', 'q', 'выход'):
            raise EOFError("Выход из игры")

        if not isinstance(normalized_input, str) or not normalized_input:
            raise ValueError('Введите букву или слово!')

        russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        set_normalized_input = [True if row in russian_alphabet else False for row in normalized_input]

        if not all(set_normalized_input):
            raise ValueError('Буквы должны быть из русского алфавита!')

        return normalized_input