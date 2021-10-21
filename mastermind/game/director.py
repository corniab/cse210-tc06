from game.console import Console
from game.roster import Roster
from game.player import Player


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
        board = ('board')#self.-boardclass.displayboard-()
        self._console.write(board)
        # Ask for next player's guess.
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number('What is your guess? ')
        # Instantiate another class to store the guess

        # Assign the guess to the player

    def _do_updates(self):
        """Updates the important game information for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        # Get the current player

        # Get their move

        # Apply the move to the board

    def _do_outputs(self):
        """Outputs the important game information for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        # Check if there is a winning combination on the board

        # If there is no winning combination get the next player
