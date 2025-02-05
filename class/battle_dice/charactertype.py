from enum import Enum

class CharacterType(Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ROGUE = "Rogue"

from charactertype import CharacterType


#Instantiating an Enum Number 
my_character_type= CharacterType.WARRIOR

#Accessing name and value 
print(my_character_type)
print(my_character_type.name)
print(my_character_type.value)