# Scratchpad

This is my scratchpad that will basically just be stream of conciousness on anything I'm working on with some regularity.

It'll include how I setup stuff, things I learned, things I need to remember, and just general thoughts.


## Things to remember
Go lookup why I would use SysExit(main()) for python code

## Things I did
Setup the entire thing as a module.  So I could handle imports better
uv init --package guild_master
uv add --dev pytest

Then I setup the directory to look like this:
```bash
guild_master/
├── pyproject.toml
├── src/
│   └── guild_master/
│       ├── __init__.py
│       ├── __main__.py
│       └── utils/
│           ├── __init__.py
│           └── basic.py
└── tests/
    └── test_basic.py
```

Now to test I will do this:
uv run pytest and it'll grab everything from the tests directory

Since I build the entire thing as a package, there is no 'main' so I made a dunder main so I could potentially consider this as a means to import into a larger program later.

In reality that won't happen, but it's at least a reasonable consideration. 
I updated project.toml:

```bash
[project.scripts]
guild-master = "guild_master.__main__:main"
```

so we can run the project like this:
uv run guild-master

Next - 

I wrote some basic functions:
```python
# Just to figure out pytest.  This entire thing is just mockup code, it'll disappear eventually
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True

    def get_user(self, username):
        return self.users.get(username)

def get_weather(temp):
    if temp > 20:
        return 'hot'
    else:
        return 'cold'
    
def add(a,b):
    return a+b

def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
And some basic pytests:
```python
# Setting up pytest.  Just testing basic functionlity. 
from guild_master.utils.basic import get_weather, add, divide, is_prime, UserManager
import pytest

@pytest.fixture
def user_manager():
    return UserManager()

def test_get_weather():
    assert get_weather(21) == 'hot'

def test_add():
    assert add(2,3) == 5, "2+3 should be 5"
    assert add(-1,1) == 0, "-1+1 should be 0"
    assert add(0,0) == 0, "0+0 should be 0"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10,0)

@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2,True),
    (3,True),
    (4, False),
    (17, True),
    (18, False),
    (19, True),
    (25, False),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected

def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com")

def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "john@example.com")
```

To get some pytesting working ad really just understand how it works.
Did some youtubing and some google sleuthing to figure thus one out in detail.