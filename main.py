
import game



class StartGame:
    def __init__(self):

        self.game_instance = game.Game()

    @staticmethod
    def _clear_console():
        """Очистка консоли"""
        print('\n' * 50)

    @staticmethod
    def _initial_greeting():
        print(f"\nДобро пожаловать в игру 'Виселица'!\n")

    @staticmethod
    def _print_game_restart():
        print(f"\n\nПерезапуск игры...")

    @staticmethod
    def _final_conclusion():
        print("\nСпасибо за игру!")

    def main(self):

        self._initial_greeting()

        while True:

            start_result = self.game_instance.start_game()

            if start_result is None:
                break

            self._clear_console()

            process_result = self.game_instance.game_proses()

            if process_result is None:
                break

            restart = self.game_instance.reset()

            if not restart:
                self._final_conclusion()
                break

            self._clear_console()
            self._print_game_restart()








if __name__ == '__main__':
    start = StartGame()
    start.main()
