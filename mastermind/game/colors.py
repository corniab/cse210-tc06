from colorama import init, Fore, Back, Style


class Colors:
    """This class is designed to look at the inputs of the players and the board, and adjust the color
    depending on the player and make the code more visual to interact with"""

    def __init__(self, name, board):
        """This is the class constructor, the values will take the name of the player, 
        have a count of the players and the board"""
        self._player_name = name
        self._player_count = []
        self._board = board


    @property
    #Returns the player name in color
    def name(self):
        return self._player_name
    
    @name.setter
    #sets the player color depending on if they are player 1 or 2
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
    #returns the board in color
    def board(self):
        return self._board
    
    @board.setter
    #changes the color from the normal white text to blue
    def board(self, new_board):
        self._board = Fore.BLUE + Style.DIM + new_board

    @board.deleter
    def board(self):
        del self._board