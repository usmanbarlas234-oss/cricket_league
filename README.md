# Dugout

A fantasy cricket league engine for the PSL 2026 season, written in Python.

**Author:** Usman Barlas

**Course:** Advanced Python for AI, LiveX Nano Degree, Batch 3 (UMT Lahore), Deliverable 1

## What it does

- Loads 142 PSL 2026 players from `data/players.csv`
- Builds fantasy teams (an XI of 11 players with a captain and vice-captain) from CSV files
- Checks every team against the league rules:
  - exactly 11 players
  - at most 100 credits
  - at most 7 players from one franchise
  - role limits: WK 1-2, BAT 3-5, AR 1-3, BOWL 3-5
  - a valid captain and vice-captain who are different players
  - no player picked twice
- Groups teams in a `League`, and prints a league table ranked by credits
- Raises its own errors (`PlayerNotFoundError`, `InvalidTeamError`) and keeps going when one team is bad
- Reads real PSL 2026 ball-by-ball match files (JSON) and prints a scorecard
- Saves teams to JSON and loads them back
## Project layout

| Path | What it holds |
|---|---|
| `dugout/models.py` | `Player`, `FantasyTeam` and `League` classes |
| `dugout/rules.py` | The league limits and the rule-check functions |
| `dugout/loader.py` | Reading players and teams from CSV files |
| `dugout/errors.py` | Custom errors raised by Dugout |
| `main.py` | Runs the checks and prints the report |
| `data/players.csv` | The player pool |
| `data/sample_teams.csv` | Class teams plus two test teams |
| `data/my_team.csv` | My own XI |
| `dugout/matches.py` | Reading a real match file: runs, balls, top scorers |
| `match_report.py` | Prints a scorecard from one match file |

## How to run

```
python main.py
python match_report.py data/matches/match_01.json
```

## Sample output

```
Player pool: 142 players
...
Summary: 2 legal, 6 illegal out of 8 teams

===== LEAGUE TABLE (cheapest first) =====
Ten Men            Fatima           84.5  ILLEGAL
Bowling Machine    Usman            87.5  ILLEGAL
Gully Strikers     Bilal            97.5  LEGAL
All-rounder Army   Tariq            97.5  ILLEGAL
Lahore Thunder     Usman Barlas     98.0  LEGAL
Qalandar Fans      Zainab           98.5  ILLEGAL
Twin Stars         Sana             99.0  ILLEGAL
Lahore Lions       Ayesha          100.0  LEGAL
Big Spenders       Hamza           112.0  ILLEGAL
```

## Data

Match data from [Cricsheet](https://cricsheet.org) (PSL 2026).