from __future__ import annotations
import uuid
import math

import guild_master.utils.constants as constants


class Character:
    """Generic Character Class"""

    def __init__(self, name:str, health:int):
        self.name = name
        self.health = health
        self.character_id = uuid.uuid5(uuid.NAMESPACE_URL, name)
        self.level = 1
        self.accumlated_xp = 0
        self.abilities = []
        self.injuries = []
        
    def get_health(self) -> int:
        '''Returns Characters current health'''
        return self.health

    # Must be implemented by Child
    def take_damage(self, damage) -> None:
        self.health -= damage
    



    def __eq__(self,other:object) -> bool:
        if not isinstance(other, Character):
            return NotImplemented
        return (self.character_id == other.character_id)
 
    def __str__(self) -> str:
        return f'Character: {self.name}\nHealth: {self.health}\nInjuries: {self.injuries}'

    def __repr__(self) -> str:
        return f'ID: {self.character_id}\nCharacter: {self.name}\nHealth: {self.health}\nInjuries: {self.injuries}'
    

class Adventurer(Character):
    def __init__(self, name: str):
        super().__init__(name, constants.BASE_HEALTH*constants.HEALTH_MULTIPLIIERS['ADVENTURER'])
        self.abilities.append("Attack")
        
    def take_damage(self, damage) -> None:
        updated_damage = damage / constants.DEFENSE_MULTIPLIIERS['ADVENTURER']
        super().take_damage(damage=updated_damage)

    def deal_damage(self, damage) -> int:
        return damage * constants.PHYSICAL_DAMAGE_MULTIPLIIERS['ADVENTURER']



class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name, math.floor(constants.BASE_HEALTH*constants.HEALTH_MULTIPLIIERS['WARRIOR']))
        self.abilities.append("Attack")
        
    def take_damage(self, damage) -> None:
        updated_damage = math.floor(damage / constants.DEFENSE_MULTIPLIIERS['WARRIOR'])
        super().take_damage(damage=updated_damage)

    def deal_damage(self, damage) -> int:
        return damage * constants.PHYSICAL_DAMAGE_MULTIPLIIERS['WARRIOR']
