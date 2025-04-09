#project1_bagjack_multideck.py
import random 
import copy
from project1_bagjack_cardtype import Card, Suit, Face

#Makes one deck
one_deck=[Card(face,suit) for suit in Suit for face in Face]

#Chooses random amount of decks
amount_of_decks=random.choice([2,4,6,8])

#Makes a multideck from a deepcopy oof the original so that it doesnt affect the original deck
multi_deck=[card for i in range(amount_of_decks) for card in copy.deepcopy(one_deck)]


