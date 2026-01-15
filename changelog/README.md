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