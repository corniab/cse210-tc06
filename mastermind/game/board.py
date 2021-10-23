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
        self.code = str(random.randint(1000, 10000))
        self.list = []

    def prepare(self, name):
        """Sets up the board with an entry for each player.

        Args:
            self (Board): an instance of Board.
        """
        # self.code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [self.code, guess, hint]
        for item in self._items[name]:
            self.list.append(item)

    def display_board(self, name):
        # returns a printable board from the prepare set up(string)
        
        pboard = (f'Player {name}: {self.list[0]}, {self.list[1]}, {self.list[2]} ')
        return pboard

    def apply(self, guess):
        # self.list.pop(1)
        # self.list.insert(1, guess.get_guess(guess))
        
        hint = ''
        guess_string = str(guess._guess)
        # place = -1
        # for digit in guess_string:
        #     for answer in self.code:
        for x in range(4):
            digit = guess_string[x]
            answer = self.code[x]
            if answer == digit:
                hint += 'x'
            elif digit in self.code:
                hint += 'o'
            else:
                hint += '*'
        return hint
        #for num in self.list[0]:
        #    place += 1
        #    if num == self.list[1][place]:
        #        hint += 'X'
        #    elif num in self.list[1]:
        #        hint += 'O'
        #    else:
        #        hint += '*'
        # return self.list[0][2]

    def is_guessed(self):
        # check to see if player guessed the answer
        # return boolean
        
        return False

    def _create_hint(self,  guess):
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
            if self.list[0][index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

