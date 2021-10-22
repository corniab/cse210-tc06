class Console:
    """A code template for a computer console. The responsibility of this
    class of objects is to get text or numerical input and display text output.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """

    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args:
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args:
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as an integer.
        """
        response = ""

        # Initialize loop to validate input.
        while not isinstance(response, int):

            # Get input from user.
            response = input(prompt)

            # If the response can be converted to an int,
            # then return the response.
            try:
                response = int(response)
                return response
            except:
                # Tell the user to enter an integer.
                print("\nEnter an integer.")

    def write(self, text):
        """Displays the given text on the screen.

        Args:
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)
