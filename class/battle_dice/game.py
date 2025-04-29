import random 
from character import Character 



class Game:
    """Manages the Dice Battle game logic"""

    def __init__(self, player1: Character, player2: Character):
        """Initializes the same game with two players"""
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where an attacker rolls a die to determine damage dealt \n
        attacker's attack power damage enhanced by multiplier"""

        damage_multiplier=random.randint(1,6)
        attacker_damage=attacker.attack_power*damage_multiplier
        defender.health-=attacker_damage
        print(f"{attacker.name} deals {defender.name} {attacker_damage} damage! ")
        print(f"{defender.name} now has {max(0, defender.health)} health remaining.")

    def start_battle(self):
        """Starts a turn based battle loop where the players take turns attacking"""
        print(f"BATTLE START: {self.__player1} VS {self.__player2}")
        turn_counter: int = 0

        while self.__player1.health and self.__player2.health > 0:

            if turn_counter % 2 == 0:
                self.attack(self.__player1,self.__player2)
            else:
                self.attack(self.__player2,self.__player1)

            turn_counter += 1

        game_winner: Character = self.__player1 if self.__player1.health > 0 else self.__player2

        print(f"{game_winner.name} is the winner!")