import time as t
from data.config import DifficultyConfigScoreManager

class TimeTracker:
    def __init__(self):
        self._start_move = 0
        self._elapsed_time = 0

    def start_move(self) -> None:
        self._start_move = t.perf_counter()

    def end_move_timing(self) -> None:
        self._elapsed_time = t.perf_counter() - self._start_move

    @property
    def time_move(self) -> round:
        return self._elapsed_time

class ScoreCalculator:
    def __init__(self, time_tracker: TimeTracker):
        self._config_manager = self._create_config()
        self._time_tracker = time_tracker
        self._total_score = 0
        self._setting = None

    @classmethod
    def _create_config(cls):
        return DifficultyConfigScoreManager

    def configure_difficulty_settings(self, difficulty: str) -> None:
        self._setting = self._config_manager[difficulty].value

    def _calculate_penalty_coefficient(self) -> round:
        return max(round(self._setting.penalty_divider / self._setting.max_attempts, 2), 1)

    def _coefficient_per_move(self) -> round:
        elapsed_time = max(self._time_tracker.time_move, 1)
        return round(60 / elapsed_time, 2)

    def calculate_move_score(self, is_correct: bool) -> tuple[round, round]:
        if not is_correct:
            self._setting.penalty_divider -= 1
            return 0, round(self._total_score)

        score = self._setting.base_score
        coefficient = self._coefficient_per_move()
        difficulty_coefficient = self._setting.multiplier_by_level
        penalty_coefficient = self._calculate_penalty_coefficient()
        point = max(0, (score * (coefficient + difficulty_coefficient) * penalty_coefficient))
        self._setting.final_points += point
        self._total_score += point

        return round(point), round(self._total_score)

    @property
    def time_tracker(self):
        return self._time_tracker

