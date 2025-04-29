#project1_bagjack_cardtype.py
from enum import Enum
from dataclasses import dataclass

#Enumerates different suits for cards
class Suit(Enum):
    SPADES="♠️"
    HEARTS="♥️"
    DIAMONDS= "♦️"
    CLUBS= "♣️"

#Enumerates different faces for cards
class Face(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

    def card_value(self) -> int:                            #Gives card values for Aces, Jacks, Queens, Kings
        if self in {Face.JACK, Face.QUEEN, Face.KING}:
            return 10
        elif self == Face.ACE:
            return 11
        else:
            return int(self.value)

@dataclass
class Card:                                                 #Gives hashable format of attributes of the class 
    face: Face
    suit: Suit

    def __hash__(self) -> int:
        return hash(self.face.name)* hash(self.suit.name)
    
    def __str__(self) -> str:
        return f"[{self.face.value}{self.suit.value}]"

