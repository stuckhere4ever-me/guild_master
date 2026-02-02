from guild_master.guild import Guild
from guild_master.character import Character, Adventurer, Warrior
import pytest

@pytest.fixture
def guild():
     return Guild("My Guild")

@pytest.fixture
def character():
     return Character("Steven", 100)

@pytest.fixture
def warrior():
     return Warrior("Walton")

@pytest.fixture
def adventurer():
     return Adventurer("Barbara")

def test_create_guild():
    new_guild = Guild(name="MyName")
    assert (new_guild==Guild("MyName"))
    
def test_get_name():
    new_guild = Guild(name="MyName")
    assert (new_guild.get_name()=="MyName")

def test_equal(guild):
    new_guild = Guild(name="My Guild")
    assert(guild == new_guild)

def test_not_equal(guild):
    new_guild = Guild(name="New Guild")
    assert(guild != new_guild)

def test_add_character(guild, character):
    guild.add_character(character)
    assert(guild.available_characters[0] == character)

def test_add_warrior(guild, warrior):
    guild.add_character(warrior)
    assert(guild.available_characters[0] == warrior)

def test_add_adventurer(guild, adventurer):
    guild.add_character(adventurer)
    assert(guild.available_characters[0] == adventurer)

def test_add_multiple(guild, adventurer,warrior,character):
    guild.add_character(adventurer)
    guild.add_character(warrior)
    guild.add_character(character)
    assert(guild.available_characters[0] == adventurer)
    assert(guild.available_characters[1] == warrior)
    assert(guild.available_characters[2] == character) 

def test_remove(guild, adventurer,warrior,character):
    guild.add_character(adventurer)
    guild.add_character(warrior)
    guild.add_character(character)
    assert(guild.available_characters[0] == adventurer)
    assert(guild.available_characters[1] == warrior)
    assert(guild.available_characters[2] == character)

    guild.remove_character(adventurer)
    assert(guild.available_characters[0] == warrior)

    guild.remove_character(warrior)
    assert(guild.available_characters[0] == character)

    guild.remove_character(character)
    with pytest.raises(IndexError): 
        guild.available_characters[0]

# def test_add():
#     assert add(2,3) == 5, "2+3 should be 5"
#     assert add(-1,1) == 0, "-1+1 should be 0"
#     assert add(0,0) == 0, "0+0 should be 0"

# def test_divide():
#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         divide(10,0)

# @pytest.mark.parametrize("num, expected", [
#     (1, False),
#     (2,True),
#     (3,True),
#     (4, False),
#     (17, True),
#     (18, False),
#     (19, True),
#     (25, False),
# ])
# def test_is_prime(num, expected):
#     assert is_prime(num) == expected

# def test_add_user(user_manager):
#     assert user_manager.add_user("john_doe", "john@example.com")

# def test_add_duplicate_user(user_manager):
#     user_manager.add_user("john_doe", "john@example.com")
#     with pytest.raises(ValueError):
#         user_manager.add_user("john_doe", "john@example.com")