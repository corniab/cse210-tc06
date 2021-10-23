from colorama import init, Fore, Back, Style

"""This class is designed to adjust the color of each player and the board"""
class Colors:

    def __init__(self, name, board):
        self._player_name = name
        self._player_count = []
        self._board = board

    @property
    def name(self):
        return self._player_name
    
    @name.setter
    def name(self, new_name):
        if len(self._player_count) == 0:
            self._player_count.append(new_name)
            self._player_name = Fore.LIGHTGREEN_EX + Style.BRIGHT + new_name
        else:
            self._player_name = Fore.LIGHTCYAN_EX + Style.BRIGHT + new_name
            self._player_count.clear
    
    @name.deleter
    def name(self):
        del self._player_name

    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, new_board):
        self._board = Fore.BLUE + Style.DIM + new_board
    