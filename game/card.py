import random


class Card:
    """A card from value 1 to 13.

    The responsibility of Card is to keep track of which card of the 'deck' is drawn and determine point value.
   
    Attributes:
        face (int): The card's face (and apparent value)
        lastCard (int): The last card's face
    """

    def __init__(self):
        self.face = 0
        self.lastCard = 0

    def draw(self):
        """Generates a new random card face and compares it to the last card
        """

        self.lastCard = self.face

        self.face = random.randint(1, 14)

        

        #Can write this way too
       