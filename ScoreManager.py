import time as t


class ScoreManager:
    """
    Система подсчета очков для игры Виселица.

    Вычисляет баллы на основе:
    - Времени, затраченного на ход;
    - Количества ошибок (неверных попыток);
    - Выбранного уровня сложности;
    - Базового значения очков.

    Формула: очки = базовые_очки × (временной_коэффициент + коэффициент_сложности) × коэффициент_ошибок
    """
    __score_it_level = {'л': 1.3,
                        'н': 1.8,
                        'с': 2.5}

    __error_rate = 6

    __point = 100

    __attempts = 6

    def __init__(self, level):
        self.__start_move = None # начало хода
        self.__end_move = None # конец хода
        self.__time_move = None # затраченное время
        self.__penalty_coefficient = None # коэффициент ошибок
        self.__coefficient = None # коэффициент за ход
        self.__difficulty_coefficient = None # коэффициент за сложность игры
        self.final_points = 0 # итоговые очки
        self.level = level


    def start_move(self):
        """Запускает счетчик времени"""
        self.__start_move = t.perf_counter()

    def end_move(self):
        """Останавливает счетчик времени"""
        self.__end_move = t.perf_counter()

    def __error_rate_value(self, attempts):
        """Подсчет коэффициента ошибок"""
        self.__penalty_coefficient = round(attempts / self.__error_rate, 2)

    def __output_difficulty_coefficient(self):
        """Вводит коэффициент сложности"""
        self.__difficulty_coefficient = self.__score_it_level[self.level]

    def __time_counting(self):
        """Подсчет потраченного времени"""
        self.__time_move = self.__end_move - self.__start_move

    def __coefficient_per_move(self):
        """Подсчет временного коэффициента"""
        self.__coefficient = round(60 / self.__time_move, 2)

    def __score(self):
        """Подсчет очков за один ход"""
        point = (self.__point
            * (self.__coefficient + self.__difficulty_coefficient)
            * self.__penalty_coefficient)
        self.final_points += point
        return round(point)

    def scoring(self, attempts):
        """
        Рассчитывает итоговый счет игрока на основе:
        - затраченного времени
        - сложности игры
        - количества ошибок (попыток)

        Возвращает: рассчитанные очки [int, round]
        """
        self.__time_counting()
        self.__output_difficulty_coefficient()
        if attempts < self.__attempts:
            self.__error_rate_value(attempts)
            self.__attempts = attempts
            return 0
        self.__error_rate_value(attempts)
        self.__coefficient_per_move()
        return round(self.__score())

