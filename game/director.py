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
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """

        last = self.card.face
        print(f"The card is: {last}")
        #make sure only h or l
        self.choice = input("Higher or lower? [h/l] ")
        pass
        
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            print("Thanks for trying our Hilo guess game. See you later!")
            return

        self.card.draw()

        newCard = self.card.face
        oldCard = self.card.lastCard

        while newCard == oldCard:
            self.card.draw()
            newCard = self.card.face
            oldCard = self.card.lastCard

        print(f"The new card is: {self.card.face}")

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
        if not self.is_playing:
            print("Thanks for trying our Hilo guess game. See you later!")
            return
             # Print current score
        print(f"Your current score is: {self.score}\n")
        
        # Keep playing as long the score is above 0
        if self.score > 0:
            pass
        else:
            self.is_playing = False
            print("You lose!")
            return