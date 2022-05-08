from game.card import Card
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.card = Card()
        

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        
        hilo_guess = input("Wanna try Hilo guess? [y/n] \n")
        self.is_playing = (hilo_guess.lower() == "y")
        print("==================================================================================================================")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            print("Thanks for trying our Hilo guess game. See you later!")
            return 
 
        # Call the guessCard function from the card library
        self.card.guessCard()
    
    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            print("Thanks for trying our Hilo guess game. See you later!")
            return
        print("\n==================================================================================================================")
        # Print current score
        print(f"Your current score is: {self.card.points}")
        print("==================================================================================================================\n")

        # Keep playing as long the score is above 0
        self.is_playing == (self.score > 0)