import json
from pathlib import Path
import random

class GetWord:

    _level_game = {'л': {'len_min': 3, 'len_max': 5},
                      'н': {'len_min': 6, 'len_max': 8},
                      'с': {'len_min': 9, 'len_max': 20}}

    def __init__(self, file_path='russian-word.json'):
        self.file_path = Path(file_path)
        self._word_cache = None


    def get_word(self, difficulty):
        """Выводит случайное слово исходя от выбранного уровня сложности"""
        if difficulty not in self._level_game:
            raise ValueError(f"Неизвестный уровень: {difficulty}")

        words = self._load_words()
        config = self._level_game[difficulty]

        suitable = random.choice(list(filter(
                lambda row: config['len_min'] <= len(row) <= config['len_max'], words)))

        return list(suitable)

    def _load_words(self) -> list[str]:
        """Выводит список слов из предложенного файла формата json"""

        if not self.file_path.exists():
            raise FileNotFoundError(f"Файл со словами не найден: {self.file_path}")

        if not self.file_path.is_file():
            raise TypeError(f"Указанный путь не является файлом: {self.file_path}")

        try:
            if self._word_cache is None:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    self._word_cache = json.load(f)
        except json.JSONDecodeError as e:
            raise TypeError(f"Ошибка чтения JSON файла: {e}")

        return self._word_cache