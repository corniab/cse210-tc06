from game.console import Console
from game.roster import Roster
from game.player import Player
from game.board import Board
from game.guess import Guess
from game.colors import Colors


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
        print(self._board.code)
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
            self._board._prepare(player)
            
            

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play.
        Args:
            self (Director): An instance of Director.
        """
        # get current player
        player = self._roster.get_current()
        name = player.get_name()
        player_name = Colors(name)
        
        


        # prepare board
        self._console.write(self._board.display_board())

        # Ask for next player's guess.
        self._console.write(f"{player_name.get_name()}'s turn:")
        input = self._console.read("What is your guess? ")

        # Instantiate another class to store the guess
        guess = Guess(input)

        # Assign the guess to the player
        player.set_move(guess)

        

    def _do_updates(self):
        """Updates the important game information for each round of play.
        Args:
            self (Director): An instance of Director.
        """
        # Get the current player
        player = self._roster.get_current()
        
        self._board.apply(player)
        

    def _do_outputs(self):
        """Outputs the important game information for each round of play.
        Args:
            self (Director): An instance of Director.
        """

        player = self._roster.get_current()
        move = player.get_move().get_guess()
        name = player.get_name()

        
        # Check if there is a winning combination on the board
        if self._board.is_guessed(move):
            print(f"\n{name} won!")
            self._keep_playing = False
            # If there is no winning combination get the next player
        else:
            self._roster.next_player()