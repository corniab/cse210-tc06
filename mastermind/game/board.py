import random


class Board:
    """A code template for the game board, or designated playing surface.
    The responsibility of this class of objects is to keep track of the pieces
    in play as the secret code is revealed.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        _items (self.list): The player's name. (Tied to their associated code, guess, hint.)
    """

    def __init__(self):
        """The class constructor. Declares and initializes instance attributes
        with their default values.

        Args:
            self (Board): an instance of Board.
        """
        
        self._items = {}
        
    

    def _prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
            player (string): show the player's name
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

        

    def display_board(self, players):
        # returns a printable board from the prepare set up(string)

        '''
        Args:
            players (string): show the names of both players
        Return:
            string: board displayed as a list and properly formatted
        '''
        #print(players)
        
        
        board_display = ('\n--------------------')
        for player in players:
            board_display += (f'\nPlayer {player}:') # {self._items[player][1]}, {self._items[player][2]}')
        board_display += '\n--------------------'

        return board_display
        
    '''
    def apply(self, move):
        #applies guess to board
        pass


    def is_guessed(self):
        # check to see if player guessed the answer
        # return boolean
        return False
    '''
    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

