from guild_master.character import Character, Warrior, Adventurer
import pytest

@pytest.fixture
def character():
     return Character("Steven", 100)

@pytest.fixture
def warrior():
     return Warrior("Walton")

@pytest.fixture
def adventurer():
     return Adventurer("Barbara")

# General Character Tests
def test_create_character():
    new_char = Character(name="John",health=100)
    assert (new_char==Character(name="John",health=100))
    
def test_name():
    new_char = Character(name="John",health=100)
    assert (new_char.name=="John")

def test_health():
    new_char = Character(name="John",health=100)
    assert (new_char.health==100)   

def test_take_damage(character):
    character.take_damage(20)
    assert(character.health == 80)

# Test with fixture
def test_fixture_all(character):
    assert (character.name == "Steven")
    assert (character.health == 100)

# Testing equality
def test_equal(character):
    new_character = Character("Steven", 100)
    assert(character == new_character)

def test_not_equal(character):
    new_character = Character("John", 100)
    assert(character != new_character)



# Adventurer Tests
def test_create_adventurer():
    new_char = Adventurer(name="John")
    assert (new_char==Adventurer(name="John"))
    assert (new_char.health == 100)

def test_adventurer_take_damage(adventurer):
    adventurer.take_damage(20)
    assert(adventurer.health == 80)

def test_adventurer_deal_damage(adventurer):
    damage_dealt = adventurer.deal_damage(20)
    assert (damage_dealt == 20)
    
# Warrior Tests
def test_create_warrior():
    new_char = Warrior(name="John")
    assert (new_char==Warrior(name="John"))
    assert (new_char.health == 110)

def test_warrior_take_damage(warrior):
    warrior.take_damage(20)
    assert(warrior.health == 92)

def test_warrior_deal_damage(warrior):
    damage_dealt = warrior.deal_damage(20)
    assert (damage_dealt == 22)


# def test_name():
#     new_char = Character(name="John",health=100)
#     assert (new_char.name=="John")

# def test_health():
#     new_char = Character(name="John",health=100)
#     assert (new_char.health==100)   

# def test_take_damage(character):
#     with pytest.raises(NotImplementedError):
#         character.take_damage()


# def test_take_damage(character):
#     with pytest.raises(NotImplementedError):
#         character.take_damage()