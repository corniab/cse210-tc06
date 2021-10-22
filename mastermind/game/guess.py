class Guess:
    ''' 
    The responsibility of guess is to track each players guess.

    Stereo type: information holder

    Attributes:
        _guess(integer): The players four digit guess
    '''

    def __init__(self, guess):
        '''
        The class constructor.
        
        Args:
            self (Guess): an instance of Guess.
        
        '''
        self._guess = guess
    

    def get_guess(self, guess):
        '''
        Recieve the players four digit guess
        
        Args:
            self (Guess): an instance of Guess.

        Returns:
            Players guess
        '''
        
        return self._guess 