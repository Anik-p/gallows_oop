from abc import ABC, abstractmethod
from typing import Union


class InputValidator(ABC):
    """Базовый интерфейс для всех валидаторов"""
    @abstractmethod
    def validate(self, input_str: str) -> Union[str, bool]:
        pass


