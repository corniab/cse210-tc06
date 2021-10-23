from game.console import Console
from game.roster import Roster
from game.player import Player
from game.board import Board
from game.guess import Guess


class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:

    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()
        self._board = Board()
        self._guess = None

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.

        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play.

        Args:
            self (Director): An instance of Director.
        """
        # Display game board.
        board = self._board.display_board()
        self._console.write(board)
        # Ask for next player's guess.
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number('What is your guess? ')
        # Instantiate another class to store the guess
        move = Guess(guess)
        # Assign the guess to the player
        player.set_move(move)

    def _do_updates(self):
        """Updates the important game information for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        # Get the current player
        player = self._roster.get_current()
        # Get their move
        move = player.get_move()
        # Apply the move to the board
        self._board.apply(move)

    def _do_outputs(self):
        """Outputs the important game information for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        # Check if there is a winning combination on the board
        if self._board.is_guessed():
            winner = self.roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
            # If there is no winning combination get the next player
        else:
            self._roster.next_player()