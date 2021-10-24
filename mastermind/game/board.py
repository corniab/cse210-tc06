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
        self.code = str(random.randint(1000, 10000))
        self._items = {}
        
    

    def _prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
            player (string): show the player's name
        """

        name = player.get_name()
        # code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [self.code, guess, hint]

        

    def display_board(self):
        """Sets up the board with two players and a record of their guesses and the 
        associated hints.

        Args:
            players (string): show the names of both players

        Return:
            string: board displayed as a list and properly formatted
        """
        #print(players)
        
        board_display = ('\n--------------------')
        for name, values in self._items.items():
            board_display += (f'\nPlayer {name}: {values[1]}, {values[2]}')
        board_display += '\n--------------------'

        return board_display
        
    def apply(self, player):
        """Applies a move to the playing surface. In this case, that means displaying 
        player's guesses and the associated hints.

        Args:
            self (Board): an instance of Board.
            player (Player): the active players.
        """
        hint = ''
        name = player.get_name()
        guess_string = str(player.get_move().get_guess())

        for x in range(4):
            digit = guess_string[x]
            answer = self.code[x]
            if answer == digit:
                hint += 'x'
            elif digit in self.code:
                hint += 'o'
            else:
                hint += '*' 

        self._items[name][2] = hint

    def is_guessed(self, move):
        """Determines if the code has been figured out.

        Args:
            self (Board): an instance of Board.
            move (Move): the move to apply.
        
        Returns: 
            boolean: True if the code has been correctly deciphered; false if otherwise.
        """
        if move == self.code:
            return True
        else:
            return False
   