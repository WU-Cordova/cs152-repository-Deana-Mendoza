#project1_bagjack_game.py
import random 
from datastructures.bag import Bag
from project1_bagjack_multideck import multi_deck



class Bagjack_Game:                                     

    def __init__(self) -> None:
        #Initiallized values and lists to keep track of player/dealer scores and cards
        self.player_hand = []
        self.player_score=0
        self.dealer_hand = []
        self.dealer_score=0


    def initializing_round(self):

        self.deck_bag = Bag(*multi_deck)

        #round initialization: grabs initial cards using distinct item lists and
        #using bag remove method it removes player initial cards from multideck

        player_initial_cards = random.sample(list(self.deck_bag.distinct_items()), 2)
        for card in player_initial_cards:
            self.deck_bag.remove(card)

        self.player_hand.append(player_initial_cards)
        self.player_hand=player_initial_cards

        #calculates score for only one of the player's initial cards, keeping the hidden card value hidden 

        player_score=sum(card.face.card_value() for card in player_initial_cards)
        self.player_score=player_score

        print(f"Initial Deal:")
        print(f"Player's Hand: {"".join(str(card) for card in player_initial_cards)} | Score: {player_score}")

        #round initialization: grabs initial cards using distinct item lists and
        #using bag remove method it removes dealer initial cards from multideck

        dealer_initial_cards= random.sample(list(self.deck_bag.distinct_items()), 2)
        for card in dealer_initial_cards:
            self.deck_bag.remove(card)

        self.dealer_hand.append(dealer_initial_cards)
        self.dealer_hand=dealer_initial_cards

        #calculates score for only one of the dealers initial cards, keeping the hidden card value hidden

        dealer_score=sum(card.face.card_value() for card in [dealer_initial_cards[0]])
        self.dealer_score=dealer_score

        print(f"Dealer's Hand: {"".join(str(card) for card in [dealer_initial_cards[0]])} [hidden] | Score: {dealer_score}")
    
        #Checks to see if player has already won with initial hand 

        if player_score == 21:
            print(f"You are the winner!")
            self.play_again()
        elif player_score < 21:
            self.players_turn()
        else:
            print(f"You busted! Dealer wins! :(")
            self.play_again()
            
    #Decides whether player wants to hit or stay
    def players_turn(self):
        decision = input("Would you like to (H)it or (S)tay?")
        if decision == "S":
            self.dealer_turn()
        elif decision == "H":
            self.player_hit()

    #what happens when player decides to hit, draws random card from multideck, removes it and calcuates new score of player's hand
    #If there score is less than 21 will continues to ask if they would like to hit again
    def player_hit(self):
        new_player_card=random.sample(list(self.deck_bag.distinct_items()), 1)
        for card in new_player_card:
            self.deck_bag.remove(card)
            self.player_hand+=new_player_card
            self.player_score=sum(card.face.card_value() for card in self.player_hand)
            print(f"Player's Hand: {"".join(str(card) for card in self.player_hand)} | Score: {self.player_score}")
        

        if self.player_score<=21:    
            self.players_turn()
        else:
            self.game_winner()

    #Turn that occurs if player decides to stay, shows the second card that was initially hidden as well as score
    def dealer_turn(self):
        self.dealer_score=sum(card.face.card_value() for card in self.dealer_hand)
        print(f"Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.dealer_score}")
        self.dealer_hit()

    #What happens when dealer hits until they reach at least 17. They hit a random card, remove that card from multideck and calcuates new score
    def dealer_hit(self):
        while self.dealer_score <17:
            new_card=random.sample(list(self.deck_bag.distinct_items()), 1)
            for card in new_card:
                self.deck_bag.remove(card)
            self.dealer_hand+=new_card
            self.dealer_score=sum(card.face.card_value() for card in self.dealer_hand)
            print(f"Dealer's Hand: {"".join(str(card) for card in self.dealer_hand)} | Score: {self.dealer_score}")
        self.game_winner()
    
    #Decides who the game winner is based on score
    def game_winner(self):
        if self.dealer_score > self.player_score and self.dealer_score <= 21:
            print(f"Dealer is the winner! You lose! :(")
            self.play_again()
        elif self.dealer_score > 21:
            print(f"Dealer busted! You win!")
            self.play_again()
        elif self.dealer_score < self.player_score and self.player_score <= 21:
            print(f"You are the winner!")
            self.play_again()
        elif self.player_score > 21:
            print(f"You busted! Dealer wins! :(")
            self.play_again()
        elif self.dealer_score == self.player_score:
            print(f"You tied!")
            self.play_again()

    #Asks if player would like to play again. If yes it initializes another round
    def play_again(self):
        replay=input(f"Would you like to play again? (Y)es or (N)o:")
        if replay == "Y":
            self.initializing_round()
        elif replay == "N":
            print(f"Game over! Thanks for playing!")
        




