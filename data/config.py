from enum import Enum
from dataclasses import dataclass, field

class DifficultyValidatorLevel(Enum):
    EASY = 'л'
    MEDIUM = 'н'
    HARD = 'с'

    @classmethod
    def get_input_mapping(cls):
        return {
            'л' : DifficultyValidatorLevel.EASY,
            'н' : DifficultyValidatorLevel.MEDIUM,
            'с' : DifficultyValidatorLevel.HARD,
            'легкий' : DifficultyValidatorLevel.EASY,
            'нормальный' : DifficultyValidatorLevel.MEDIUM,
            'сложный' : DifficultyValidatorLevel.HARD
        }

class DifficultyLevelWordProvider(Enum):
    EASY = {'len_min': 3, 'len_max': 5}
    MEDIUM = {'len_min': 6, 'len_max': 8}
    HARD = {'len_min': 9, 'len_max': 20}

@dataclass
class DifficultySettings:
    max_attempts: int
    multiplier_by_level: float
    base_score: int
    penalty_divider: int
    final_points: float = field(default=0.0)

class DifficultyConfigScoreManager(Enum):
    EASY = DifficultySettings(
    max_attempts= 8,
    multiplier_by_level= 1.3,
    base_score= 100,
    penalty_divider=8)

    MEDIUM = DifficultySettings(
    max_attempts= 6,
    multiplier_by_level= 1.8,
    base_score= 150,
    penalty_divider=6)

    HARD = DifficultySettings(
    max_attempts= 4,
    multiplier_by_level= 2.5,
    base_score= 200,
    penalty_divider=4)

#    CUSTOM = DifficultySettings(
#    max_attempts= 6,
#    multiplier_by_level= 1.5,
#    base_score= 100,
#    penalty_divider=6)

class HangmanVisualizerLevel(Enum):
    EASY = [0,1,1,2,2,3,4,5,6] #8
    MEDIUM = [0,1,2,3,4,5,6] #6
    HARD = [0,2,4,5,6] #4

class MaxAttempts(Enum):
    EASY = 8
    MEDIUM = 6
    HARD = 4

