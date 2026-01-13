# Guildmaster Ledger

Guildmaster Ledger is a TUI management game where you run a small adventurer guild.  
The focus is decision pressure, not content volume: pick contracts, balance risk, rotate a limited roster, and spend scarce resources on recovery and upgrades.

## What you can do
- Manage a roster with condition (fatigue, stress, injuries)
- Choose from a rotating contract board with tradeoffs
- Review post-mission reports and track outcomes across a season
- Spend limited resources on recovery and guild improvements

## Requirements
- Python 3.11+
- uv

## Install (developer workflow)
Create or update the project virtual environment and install dependencies:

```bash
uv sync
```

Notes:
- `.venv/` is the project virtual environment directory used by uv.
- `uv.lock` is the lockfile created by uv’s project workflow and is commonly committed for reproducible installs.

## Run
If the console script is configured in `pyproject.toml`:

```bash
uv run guild-master
```

Alternative (runs the package as a module, which executes `guild_master.__main__`):

```bash
uv run python -m guild_master
```

Console scripts are defined under `[project.scripts]` in `pyproject.toml` (set to: `guild-master = "guild_master.__main__:main"`).

## Tests
Run the test suite:

```bash
uv run pytest
```

## Dependency notes
- Runtime dependencies live in `[project].dependencies`.
- Dev tools live in `[dependency-groups].dev` (added via `uv add --dev ...`).