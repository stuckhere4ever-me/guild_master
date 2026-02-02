from __future__ import annotations
from typing import List
from guild_master.character import Character


class Guild:
    """Guild Class - Represents the entire guild that is being managed"""

    def __init__(self, name:str):
        self.__name = name
        self.available_characters = []


    def get_name(self) -> str:
        return self.__name

    def add_character(self, new_character:Character) -> None:
        self.available_characters.append(new_character)

    def remove_character(self, character_to_remove:Character) -> None:
        self.available_characters.remove(character_to_remove)


    def __eq__(self,other:object) -> bool:
        if not isinstance(other, Guild):
            return NotImplemented
        return self.__name == other.get_name()
 
    def __str__(self) -> str:
        return f"Guild {self.__name}"

    def __repr__(self) -> str:
        return f"Guild {self.__name}"