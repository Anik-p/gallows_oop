from validators.interfaces import InputValidator

class RestartValidator(InputValidator):
    def validate(self, input_str: str) -> bool:
        normalized_input = input_str.lower().strip()

        if normalized_input in ('да', 'д'):
            return True
        elif normalized_input in ('нет', 'не', 'н'):
            return False
        else:
            raise ValueError('\nНекорректный ввод!')