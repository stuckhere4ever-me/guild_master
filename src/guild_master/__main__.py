from guild_master.character import Character, Warrior, Adventurer

def test_warrior():
    warrior = Warrior("John")
    print(warrior)
    warrior.take_damage(20)
    

def main():
    pass
    # test_warrior()

if __name__ == 'main':
    main()