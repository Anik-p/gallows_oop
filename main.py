
import game



class StartGame:
    def __init__(self):

        self.game_instance = game.Game()

    @staticmethod
    def _clear_console():
        """Очистка консоли"""
        print('\033[H\033[J', end='')


    def main(self):
        print(f"\nДобро пожаловать в игру 'Виселица'!\n")
        while True:



            start_result = self.game_instance.start_game()

            if start_result is None:
                break

            self._clear_console()

            process_result = self.game_instance.game_proses()

            if process_result is None:
                break

            self._clear_console()

            restart = self.game_instance.reset()

            if not restart:
                print("\nСпасибо за игру!")
                break

            print(f"\n\nПерезапуск игры...")








if __name__ == '__main__':
    start = StartGame()
    start.main()
