import json
from pathlib import Path
import random
from data.config import DifficultyLevelWordProvider

class Word:
    def __init__(self, file_path='data//russian-word.json'):
        self._config = self._create_confing()
        self.file_path = Path(file_path)
        self._word_cache = None

    @classmethod
    def _create_confing(cls):
        return DifficultyLevelWordProvider

    def get_random_word(self, difficulty) -> list[str]:
        try:
            self._config[difficulty]
        except KeyError:
            raise ValueError(f"Неизвестный уровень: {difficulty}")
        words = self. _validate_json_file()
        config = self._config[difficulty].value
        suitable = [row for row in words if config['len_min'] <= len(row) <= config['len_max']]
        return random.choice(suitable)

    @staticmethod
    def _validate_json(content) -> bool:
        try:
            current_pos = content.tell()
            json.load(content)
            content.seek(current_pos)
            return True
        except (json.JSONDecodeError, ValueError):
            return False

    def  _validate_json_file(self) -> list[str]:
        """Выводит список слов из предложенного файла формата json
         или обычного текстового файла"""
        if not self.file_path.exists():
            raise FileNotFoundError(f"Файл со словами не найден: {self.file_path}")
        if not self.file_path.is_file():
            raise TypeError(f"Указанный путь не является файлом: {self.file_path}")
        try:
            if self._word_cache is None:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    if self._validate_json(f):
                        self._word_cache = json.load(f)
                    else:
                        self._word_cache = f.read().splitlines()

        except json.JSONDecodeError as e:
            raise TypeError(f"Ошибка чтения JSON файла: {e}")
        except FileNotFoundError as e:
            raise TypeError(f"Файл не найден: {e}")
        return self._word_cache