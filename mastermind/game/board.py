import random


class Board:
    """A code template for the game board, or designated playing surface.
    The responsibility of this class of objects is to keep track of the pieces
    in play as the secret code is revealed.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        _items (list): The player's name. (Tied to their associated code, guess, hint.)
    """

    def __init__(self):
        """The class constructor. Declares and initializes instance attributes
        with their default values.

        Args:
            self (Board): an instance of Board.
        """
        self._items = {}
        self.code = str(random.randint(1000, 10000))

    def prepare(self, name):
        """Sets up the board with an entry for each player.

        Args:
            self (Board): an instance of Board.
        """
        
        guess = "----"
        hint = "****"
        self._items[name] = [self.code, guess, hint]

    def display_board(self, name):
        # returns a printable board from the prepare set up(string)
        list = []
        for item in self._items[name]:
            list.append(item)
        
        pboard = (f'Player {name}: {list[0]}, {list[1]}, {list[2]} ')
        return pboard

    def apply(self, move):
        # applies guess to board
        pass

    def is_guessed(self):
        # check to see if player guessed the answer
        # return boolean
        return False

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
