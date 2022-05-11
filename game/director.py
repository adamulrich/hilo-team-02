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
        self.score = 300
        self.card = Card()
        self.card.draw()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        print("\nWelcome to Hilo! Each round you'll guess whether the next card will be higher or lower than the last one!")
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        print(f"Thanks for playing! Your final score was {self.score}")

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """

        last = self.card.face
        print(f"\nThe card is: {last}")
        
        
        self.choice = input("Higher or lower? [h/l] ")
        while (self.choice.lower() != "h") and (self.choice.lower() != "l"):
            self.choice = input("Higher or lower? [h/l] ")
        pass
        
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
      
        self.card.draw()

        newCard = self.card.face
        oldCard = self.card.lastCard

        while newCard == oldCard:
            self.card.draw()
            newCard = self.card.face
            oldCard = self.card.lastCard

        print(f"\nThe new card is: {self.card.face}")

        if newCard > oldCard:
            if self.choice.lower() == "h":
                self.score += 100
                print("You guessed correctly!")
            else:
                self.score -= 75
                print("You guessed wrong!")
        else:
            if self.choice.lower() == "l":
                self.score += 100
                print("You guessed correctly!")
            else:
                self.score -= 75
                print("You guessed wrong!")

    
    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
       
             # Print current score
        print(f"Your current score is: {self.score}\n")
        
        # Keep playing as long the score is above 0
        if self.score > 0:

            playing = input("Wanna keep playing? [y/n] ")
            while (playing.lower() != "y") and (playing.lower() != "n"):
                playing = input("Wanna keep playing? [y/n] ")
            self.is_playing = (playing.lower() == "y")
            pass
            
        else:
            self.is_playing = False
            print("You lose!")
            return