from validators.interfaces import InputValidator

class RestartValidator(InputValidator):
    def validate(self, input_str: str) -> bool:

        if input_str in ('да', 'д'):
            return True

        elif input_str in ('нет', 'не', 'н'):
            return False

        else:
            raise ValueError('\nНекорректный ввод!')