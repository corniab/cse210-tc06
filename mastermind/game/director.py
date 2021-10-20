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

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """

    def _do_updates(self):
        """Updates the important game information for each round of play. In
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
