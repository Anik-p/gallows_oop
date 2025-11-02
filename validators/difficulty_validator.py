from validators.interfaces import InputValidator
from data.config import DifficultyValidatorLevel


class DifficultyValidator(InputValidator):
    def __init__(self):
        self._confing = self._create_confing()

    @classmethod
    def _create_confing(cls):
        return DifficultyValidatorLevel

    def validate(self, input_str: str) -> str:

        normalized_input = input_str.lower().strip()

        if normalized_input in ('quit', 'exit', 'q', 'выход'):
            raise EOFError("Выход из игры")

        russian_to_enum = self._confing.get_input_mapping()

        if normalized_input not in russian_to_enum:
            raise ValueError('Некорректный уровень сложности!')

        return russian_to_enum[normalized_input].name