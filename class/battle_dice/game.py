import random 
from character import Character 



class Game:
    """Manages the Dice Battle game logic"""

    def __init__(self, player1: Character, player2: Character):
        """Initializes the same game with two players"""
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where an attacker rolls a die to determine damage dealt"""
        turn_counter=1

        if turn_counter %2 !=0:
            attacker=self.__player1
            defender=self.__player2
        else:
            attacker=self.__player2
            defender=self.__player1

        Roll_values=[1,2,3,4,5,6]
        random_roll=random.choice(Roll_values)
        defender.health= defender.health-(attacker.attack_power*random_roll)
        print(defender.health)
        

    def start_battle(self):
        """Starts a turn based battle loop where the players take turns attacking"""
        while self.__player1.health and self.__player2.health 0:
            self.attack()