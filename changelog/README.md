# Changelog
This is just going to be a running list of things that change in a given commit

## Guild Class Creation
- Moved test_basic into a ref directory that was added to gitignore
- Created a src/guild.py file for the Guild Class
  - Created Constructor
  - Created get_name method
  - Created ```__str__```, ```__eq__```, ```__repr__```
- Created tests/test_guild.py
  - Created a Fixture -> Creates guild named: My Guild
  - Created a series of tests:
    - Create Guild
    - Get Name
    - Guilds Equal
    - Guilds Not Equal
- Setup pytest to only run from tests directory
- Added Changelog Readme

Commit Message: "Created Guild Class and Tests.  Cleaned up testing structure. Added Changelog"

## Character Class Creation
- Created a character.py file that includes three classes
- character is the parent class
  - init
  - get_health -> Returns health
  - take_damage -> Reduces damage by given amount.  Subclasses adjust damage number passed
  - deal_damage -> overwritten by subclasses because this may be more complex for other classes
  - eq, str, repr 
- Adenturer -> Base everything
- Warrior -> Adjusted by 10% (more damage dealt, less damage recieved)
- Created tests/test_character
  - Three Fixtures -> One for each class
  - Created a series of tests for characters

## Character List
- Created a list in the guild class that shows available characters
- Testing adding and removing from the character list
- 